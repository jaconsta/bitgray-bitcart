from django.test import TestCase, Client
import json

# This tests are not functional only for reference
class ClientCrud(TestCase):
    def setUp(self):
        pass
    def clientPost(self):
        clientJson = json.dumps({
                    "name":"Javier",
                    "identification":10,
                    "details":"jaja"
                 })
        url = '/clients/'

        # Make web reqeust
        client = Client()
        client.post(url, clientJson, 'application/json')

    def clientGet(self):
        url = '/clients/' + self.clientId
        client.get(url)
