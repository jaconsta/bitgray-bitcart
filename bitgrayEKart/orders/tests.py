from django.test import TestCase, Client
import json

# This tests are not functional only for reference
class ClientCrud(TestCase):
    def setUp(self):
        pass
    def clientPost(self):
        orderJson = json.dumps({
                    "product":"Bottle",
                    "price":1000,
                    "details":"Round and plastic"
                 })
        url = '/orders/'

        # Make web reqeust
        client = Client()
        client.post(url, orderJson, 'application/json')

    def clientGet(self):
        url = '/orders/' + self.clientId
        client.get(url)
