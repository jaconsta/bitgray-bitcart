from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

import json

from .models import Product

def getAll(total=10):
    '''
    Gets n=TOTAL product
    Serializes the result
    '''
    product = Product.objects.values()[:total]
    return list(product)

def create(productFields):
    '''
    CRUD Element: Create.
    '''
    product = Product(product=productFields['product'] if 'product' in productFields else None,
                    price=productFields['price'] if 'price' in productFields else None,
                    details=productFields['details'] if 'details' in productFields else None)
    product.save()
    return product

def read(productId):
    '''
    CRUD Element: Read.
    '''
    try:
        product = Product.objects.get(pk=productId)
    except ObjectDoesNotExist:
        product = None
    return product

def update(product, productFields):
    '''
    CRUD Element: Update.
    '''
    if 'product' in productFields:
        product.product = productFields['product']
    if 'price' in productFields:
        product.price = productFields['price']
    if 'details' in productFields:
        product.details = productFields['details']
    product.save()

def delete(product):
    '''
    CRUD Element: Delete.
    '''
    product.delete()


####################
####################
@csrf_exempt   # Temporary
def index (request):
    '''
    Http Methods available:
        Create: Create the new product
        Read: Gets 10 products
    '''
    if request.method == 'POST':
        import sys
        try:
            # Read and parse the Json
            print (request.body)
            productFields = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return JsonResponse({'error': 'Incorrect product object.'}, status=400)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return JsonResponse({'error': 'Misssing or incorrect product.'}, status=400)
        # Create the product
        create(productFields)
        return JsonResponse({'message': 'product created.'})
    else:
        # Get a list of available products
        return JsonResponse({'products':getAll()})

@csrf_exempt   # Temporary
def crud(request, productId):
    '''
    Http Methods available:
        Read: Get the product
        Update: Update the product
        Delete: Delete the product
    '''
    # Validates the product exists
    product = read(productId)
    if product == None:
        return JsonResponse({'error': 'product does not exist.'}, status=400)

    if request.method == 'PUT':
        # Update the record.
        try:
            # Read and parse the Json
            productFields = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return JsonResponse({'error': 'Incorrect product object.'}, status=400)
        except:
            return JsonResponse({'error': 'Misssing or incorrect product Json.'}, status=400)

        product = update(product, productFields)
        return JsonResponse({'message':'product updated'})
    elif request.method == 'DELETE':
        # Delete the record.
        delete(product)
        return JsonResponse({'message': 'product deleted.'})
    elif request.method == 'POST':
        # Post is not supported here.
        return JsonResponse({'error': 'Cannot POST'}, status=400)
    else:
        # Get the record.
        return JsonResponse({'message': 'product', 'product': product.toJson()})
