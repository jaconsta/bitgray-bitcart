from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

import json 

from .models import Client

def comesPk(clientId):
    return True if 'clientId' in locals() else False
    
def getAll(total=10):
    '''
    Gets n=TOTAL clients
    Serializes the result 
    '''
    client = Client.objects.values()[:total]
    return list(client) 

def create(clientFields):
    '''
    CRUD Element: Create.
    '''
    client = Client(identification=clientFields['identification'], 
                    name=clientFields['name'], 
                    details=clientFields['details'])
    client.save()
    return client

def read(clientId):
    '''
    CRUD Element: Read.
    '''
    try:
        client = Client.objects.get(pk=clientId)
    except ObjectDoesNotExist:
        client = None
    return client

def update(clientId, clientFields):
    '''
    CRUD Element: Update.
    '''
    client = read (clientId)
    if client == None:  # Client doesn't exists
        return None

    if 'identification' in clientFields:
        client.identification = clientFields['identification']
    if 'name' in clientFields:
        client.name = clientFields['name']
    if 'details' in clientFields:
        client.details = clientFields['details']
    client.save()

def delete(clientId):
    '''
    CRUD Element: Delete.
    '''
    Client.objects.get(pk=clientId).delete()

####################
####################
@csrf_exempt   # Temporary
def index (request):
    '''
    Http Methods available:
        Create: Create the new Client
        Read: Gets 10 clients
    '''
    if request.method == 'POST':
        import sys
        try:
            # Read and parse the Json
            print (request.body)
            clientFields = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return JsonResponse({'error': 'Incorrect client object.'}, status=400)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return JsonResponse({'error': 'Misssing or incorrect client.'}, status=400)
        create(clientFields)
        return JsonResponse({'message': 'Client created.'})
    else:
        # Get a list of available clients
        return JsonResponse({'clients':getAll()})

@csrf_exempt   # Temporary
def crud(request, clientId):
    '''
    Http Methods available:
        Read: Get the client 
        Update: Update the client
        Delete: Delete the client
    '''
    # Validates the client exists
    client = read(clientId)
    if client == None:
        return JsonResponse({'error': 'Client does not exists.'}, status=400)

    if request.method == 'PUT':
        # Update the record.
        try:
            # Read and parse the Json
            clientFields = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return JsonResponse({'error': 'Incorrect client object.'}, status=400)
        except:
            return JsonResponse({'error': 'Misssing or incorrect client Json.'}, status=400)

        client = update(clientId, clientFields)
        if client == None:
            return JsonResponse({'error': 'Client does not exists.'}, status=400)
        return JsonResponse({'message':'Client updated'})
    elif request.method == 'DELETE':
        # Delete the record.
        delete(clientId)
        return JsonResponse({'message': 'Client deleted.'})
    elif request.method == 'POST':
        return JsonResponse({'error': 'Cannot POST'}, status=400)
    else:
        # Get the record.
        return JsonResponse({'message': 'Client', 'client': client.toJson()})