from django.test import TestCase, Client
import json

# This tests are not functional only for reference
class Office(TestCase):
    def setUp(self):
        pass
    def officePost(self):
        officeJson = json.dumps({
                    "office":"Teusaquillo",
                    "address":"Calle 116 # 45- 44"
                 })
        url = '/offices/'

        # Make web reqeust
        client= Client()
        client.post(url, officeJson, 'application/json')

    def officeGet(self):
        url = '/offices/' + self.officeId
        office.get(url)
