# BitKart E-Cart

A simple e-cart application that allows to CRUD operations on clients, products, facilities and orders. Process orders 

The entry test for bitgray running:
 * [Python 3](https://www.python.org/) for backend.
 * [PostgreSQL](http://www.postgresql.org/) for data storage.
 * [React](https://facebook.github.io/react/) for frontend visualization.

This application is currently running in this [link](http://bitgrayekart.herokuapp.com).

Api: 
* [Django](https://www.djangoproject.com/) for the API construction.
* Urls follows Rest syntax for web services. 
* Responses are provided via JSON.

web UI:
* Uses [JQuery](https://jquery.com/) for asynchronous queries.
* [Bootstrap](http://getbootstrap.com/) for quick css styles

## Instructions

### API

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

And access [localhost](http://localhost:8000) API from your tester.

### web UI

Go to the frontent code and Install server npm modules:
    
    $ cd bitgaryEKart_Front
    $ npm install

run server:

    $ grunt

And access [localhost](http://localhost:9000) Web from our web browser.