#!/usr/bin/python
'''
weeklyReport.py

Sends the last week activities to mail with the following info:
  - Average difference, maximum and minimum prices in Product and Order tables.
  - Number of orders.
  - Total Revenues.
  - Average purchases per minute.
'''
import psycopg2
import sqlite3
import sys
import os

def sqliteConnect(address='bitgrayEkart/bitKart.sqlite3'):
    '''
    Handles the connection to SQLITE database.
    This is for development environment
    '''
    try:
        connection = sqlite3.connect(address)
    except sqlite3.Error, e:
        print ("Error connecting to sqlite database.")
        sys.exit(0)
    finally:
        return connection, connection.cursor()

def postgresConnect(host='localhost', dbname='bitKart', user='', password=''):
    '''
    Handles the postgres connection
    '''
    conn_string = "host='%s' dbname='%s' user='%s' password='%s'" % (host, dbname, user, password)
    
    try:
        connection = psycopg2.connect(conn_string)
    except:
        print ("Error connecting to postgreSQL database.")
        sys.exit(0)

    return (connection, connection.cursor())    # The cursor to perform queries


def dbConnect():
    '''
    Connects to the database

    '''
    host = 'localhost'
    dbname = 'bitKart'
    user = 'postgres'
    password = 'secret'

    print ('Connecting to database.')

    #if os.getenv('DEBUG', True):
    #    connection, cursor = sqliteConnect()
    #else : 
    connection, cursor = postgresConnect()
    return (connection, cursor)


def averageProductsPrice(cursor):
    '''
    '''
    cursor.execute("SELECT PRODUCTO, AVG(PRECIO) FROM PRODUCTOS \
                    WHERE FECHA > current_date - interval '7days' \
                    GROUP BY PRODUCTO")
    return cursor.fetchone()

def averageOrdersPrice(cursor):
    '''
    '''
    cursor.execute("SELECT AVG(PRECIO) FROM COMPRAS\
                    WHERE FECHA > current_date - interval '7days'")
    return cursor.fetchone()

def totalOrders(cursor):
    '''
    Get the total orders purchased.
    Point 10.B.
    '''
    cursor.execute("SELECT count(*) FROM COMPRAS\
                    WHERE FECHA > current_date - interval '7days'")
    return cursor.fetchone()

def totalRevenues(cursor):
    '''
    Get the totals incomes in orders.
    Point 10.C.
    '''
    cursor.execute("SELECT SUM(PRECIO) FROM COMPRAS \
                    WHERE FECHA > current_date - interval '7days'")
    return cursor.fetchone()

def averagePurchasesMinute(cursor):
    '''
    Gets the average orders per minute.
    Point 10.D.
    '''
    cursor.execute("SELECT date_trunc('minute', FECHA) \
                    COUNT(*) FROM COMPRAS \
                    GROUP BY date_trunc('minute', FECHA)")
    return cursor.fetchone()


def main():
    '''
    '''
    connection, cursor = dbConnect()

    dateRange = "current_date - interval '7days'"
    totalOrders = totalOrders()
    print (totalOrders)
    print("Weekly report process finished succesfully.")
    sys.exit(0)

if __name == "__main__":
    main()