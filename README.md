# BitKart E-Cart application

A simple e-cart application that allows to CRUD operations on clients, products, facilities and orders. Process orders 

The entry test for bitgray running:
 * Python 3 for backend.
 * PostgreSQL for data storage.
 * Angular for frontend visualization.

This application is currently running in this [link](http://bitgrayekart.herokuapp.com).

Api: 
* Urls follows Rest syntax for web services. 
* Responses are provided via JSON.

## Instructions

Set The Virtual Environment:
    $ python -m venv myenv
    $ source myenv/bin/activate # If Linux
    $ myenv\Scripts\activate.bat # If Windows
And install from requirements:
	$ pip install  -r requirements.txt # --no-index

Create a database with name *bitKart* and run
    $ python manage.py migrate

To run the server locally:
    $ cd bitgrayEKart
    $ python manage.py runserver 0.0.0.0:8000
And access [localhost](http://localhost:8000).