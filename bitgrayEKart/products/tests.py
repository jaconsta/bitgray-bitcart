from django.test import TestCase, Client
import json

# This tests are not functional only for reference
class ClientCrud(TestCase):
    def setUp(self):
        pass
    def clientPost(self):
        productJson = json.dumps({
                    "product":"Bottle",
                    "price":1000,
                    "details":"Round and plastic"
                 })
        url = '/product/'

        # Make web reqeust
        client = Client()
        client.post(url, productJson, 'application/json')

    def clientGet(self):
        url = '/products/' + self.clientId
        client.get(url)
