from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

import json

from .models import Office

def getAll(total=10):
    '''
    Gets n=TOTAL office
    Serializes the result
    '''
    office = Office.objects.values()[:total]
    return list(office)

def create(officeFields):
    '''
    CRUD Element: Create.
    '''
    office = Office(office=officeFields['office'] if 'office' in officeFields else None,
                    address=officeFields['address'] if 'address' in officeFields else None)
    office.save()
    return office

def read(officeId):
    '''
    CRUD Element: Read.
    '''
    try:
        office = Office.objects.get(pk=officeId)
    except ObjectDoesNotExist:
        office = None
    return office

def update(office, officeFields):
    '''
    CRUD Element: Update.
    '''
    if 'office' in officeFields:
        office.office = officeFields['office']
    if 'address' in officeFields:
        office.address= officeFields['address']
    office.save()

def delete(office):
    '''
    CRUD Element: Delete.
    '''
    office.delete()


####################
####################
@csrf_exempt   # Temporary
def index (request):
    '''
    Http Methods available:
        Create: Create the new office
        Read: Gets 10 offices
    '''
    if request.method == 'POST':
        import sys
        try:
            # Read and parse the Json
            print (request.body)
            officeFields = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return JsonResponse({'error': 'Incorrect office object.'}, status=400)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return JsonResponse({'error': 'Misssing or incorrect office.'}, status=400)
        # Create the office
        create(officeFields)
        return JsonResponse({'message': 'Office created.'})
    else:
        # Get a list of available offices
        return JsonResponse({'offices':getAll()})

@csrf_exempt   # Temporary
def crud(request, officeId):
    '''
    Http Methods available:
        Read: Get the office
        Update: Update the office
        Delete: Delete the office
    '''
    # Validates the office exists
    office = read(officeId)
    if office == None:
        return JsonResponse({'error': 'office does not exist.'}, status=400)

    if request.method == 'PUT':
        # Update the record.
        try:
            # Read and parse the Json
            officeFields = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return JsonResponse({'error': 'Incorrect office object.'}, status=400)
        except:
            return JsonResponse({'error': 'Misssing or incorrect office Json.'}, status=400)

        office = update(office, officeFields)
        return JsonResponse({'message':'office updated'})
    elif request.method == 'DELETE':
        # Delete the record.
        delete(office)
        return JsonResponse({'message': 'office deleted.'})
    elif request.method == 'POST':
        # Post is not supported here.
        return JsonResponse({'error': 'Cannot POST'}, status=400)
    else:
        # Get the record.
        return JsonResponse({'message': 'office', 'office': office.toJson()})
