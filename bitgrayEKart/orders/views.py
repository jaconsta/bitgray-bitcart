from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

import json

from .models import Order
from clients.models import Client
from products.models import Product
from offices.models import Office

class NotExists(Exception):
    '''
    Exception
    '''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def clientExists(clientId):
    '''
    Validate if the Client pk exists and return the Client object
    '''
    try: 
        client = Client.objects.get(pk=clientId)
    except ObjectDoesNotExist:
        return None
    return client

def productExists(productId):
    '''
    Validate if the Product pk exists and return the Product object
    '''
    try:
        product = Product.objects.get(pk=productId)
    except ObjectDoesNotExist:
        return None
    return product

def officeExists(officeId):
    '''
    Validate if the Office pk exists and return the Office object
    '''
    try:
        office = Office.objects.get(pk=officeId)
    except ObjectDoesNotExist:
        return None
    return office

def foreignsValidate(orderFields):
    '''
    Validates that the Foreigns Key provided do exist and are valid
    '''
    client = clientExists(orderFields['client'])
    if client == None:
        raise NotExists('client')
    product = productExists(orderFields['product'])
    if product == None:
        raise NotExists('product')
    office = officeExists(orderFields['office'])
    if office == None:
        raise NotExists('product')
    # All values exists and are valid 
    return (client, product, office)

def getAll(total=10):
    '''
    Gets n=TOTAL orders
    Serializes the result
    '''
    orders = Order.objects.all()[:total]
    orderJson = map(lambda order: order.toJson(), orders)
    return list(orderJson)

def getFromUserCardId(userDocId):
    '''
    Gets the total user's Orders from his id card
    '''
    orders = Order.objects.filter(client__identification = userDocId)
    orderJson = map(lambda order: order.toJson(), orders)
    return list(orderJson)

def create(orderFields, client, product, office):
    '''
    CRUD Element: Create.
    '''
    order = Order(
                client=client,
                product=product,
                office=office,
                price=orderFields['price'],
                description=orderFields['description']
                  )
    order.save()
    return order

def read(orderId):
    '''
    CRUD Element: Read.
    '''
    try:
        order = Order.objects.get(pk=orderId)
    except ObjectDoesNotExist:
        order = None
    return order

def update(order, orderFields):
    '''
    CRUD Element: Update.
    '''
    if 'client' in orderFields:
        order.client = clientExists(orderFields['client'])
        if order.client == None:
            raise NotExists('client')
    if 'product' in orderFields:
        order.product = productExists(orderFields['product'])
        if product == None:
            raise NotExists('product')
    if 'office' in orderFields:
        order.office = officeExists(orderFields['office'])
        if order.office == None:
            raise NotExists('product')
    if 'price' in orderFields:
        order.price = orderFields['price']
    if 'description' in orderFields:
        order.description = orderFields['description']
    order.save()

def delete(order):
    '''
    CRUD Element: Delete.
    '''
    order.delete()

####################
####################
@csrf_exempt
def index(request):
    '''
    '''
    if request.method == 'POST':
        import sys
        try:
            # Read and parse the Json
            orderFields = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return JsonResponse({'error': 'Incorrect office object.'}, status=400)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return JsonResponse({'error': 'Misssing or incorrect office.'}, status=400)
        # Validate and foreign Keys
        try:
            client, product, office = foreignsValidate(orderFields)
        except NotExists as e:
            return JsonResponse({'error': '%s incorrect or does not exist.' % e.value})

        # Save the order
        order = create(orderFields, client, product, office)
        return JsonResponse({'message': 'order Posted.', 'order': order.toJson()})
    else: 
        # Validate if client cardID comes 
        userId = request.GET.get('userId', False)
        if userId:
            orders = getFromUserCardId(userId)
        else :
            orders = getAll()
        return JsonResponse({'orders': orders})

@csrf_exempt
def crud(request, orderId):
    '''
    Http Methods available:
        Read: Get the product
        Update: Update the product
        Delete: Delete the product
    '''
    # Validates the order exists
    order = read(orderId)
    if order == None:
        return JsonResponse({'error': 'Order does not exist.'}, status=400)

    if request.method == 'PUT':
        # Update the record.
        try:
            # Read and parse the Json
            orderFields = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return JsonResponse({'error': 'Incorrect order object.'}, status=400)
        except:
            return JsonResponse({'error': 'Misssing or incorrect order Json.'}, status=400)

        order = update(order, orderFields)
        return JsonResponse({'message':'Order updated.'})
    elif request.method == 'DELETE':
        # Delete the record.
        delete(order)
        return JsonResponse({'message': 'Order deleted.'})
    elif request.method == 'POST':
        # Post is not supported here.
        return JsonResponse({'error': 'Cannot POST'}, status=400)
    else:
        # Get the record.
        return JsonResponse({'message': 'Order', 'order': order.toJson()})