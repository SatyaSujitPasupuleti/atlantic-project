from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse as drf_reverse
class TestCustomerOrder(APITestCase):
    def test_post(self):
        customer_order = {
            "customer": {
                "id": "1234",
                "first_name": "Satya",
                "last_name": "Pasupuleti",
                "address_1": "Address",
                "address_2": "",
                "city": "City",
                "state": "NJ",
                "postal_code": "33043",
                "subscription": {
                    "id": "135652",
                    "plan_name": "print & digital",
                    "price": "5999",
                },    
                "gifts":[
                    {
                        "id": "235235",
                        "plan_name": "digital",
                        "price": "4999",
                        "recipient_email": "mark@twain.com"
                    },
                    {
                        "id": "234636",
                        "plan_name": "digital",
                        "price": "4999",
                        "recipient_email": "jane@austin.com"
                    },
                ]
            }
        }
        url = drf_reverse(
            'customerorder-list'
        )
        r = self.client.post(url,customer_order,format='json')
        self.assertEqual(r.status_code,status.HTTP_201_CREATED)
    def test_same_customer_order(self):
        customer_order = {
            "customer": {
                "id": "1234",
                "first_name": "Satya",
                "last_name": "Pasupuleti",
                "address_1": "Address",
                "address_2": "",
                "city": "City",
                "state": "NJ",
                "postal_code": "33043",
                "subscription": {
                    "id": "135652",
                    "plan_name": "print & digital",
                    "price": "5999",
                },    
                "gifts":[
                    {
                        "id": "235235",
                        "plan_name": "digital",
                        "price": "4999",
                        "recipient_email": "mark@twain.com"
                    },
                    {
                        "id": "234636",
                        "plan_name": "digital",
                        "price": "4999",
                        "recipient_email": "jane@austin.com"
                    },
                ]
            }
        }
        url = drf_reverse(
            'customerorder-list'
        )
        r = self.client.post(url,customer_order,format='json')
        self.assertEqual(r.status_code,status.HTTP_201_CREATED)

        r2 = self.client.post(url,customer_order,format='json')
        self.assertEqual(r2.status_code,status.HTTP_400_BAD_REQUEST)

# Create your tests here.
