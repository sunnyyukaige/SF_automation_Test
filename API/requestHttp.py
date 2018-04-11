import requests
import unittest


class BaseRequest(unittest.TestCase):
    def __init__(self,headers):
        self.headers=headers

    def get(self,url):
        response= requests.get(url,headers=self.headers)
        if response.ok:
            return response.json()
        else:
            self.fail(response.status_code)


    def post(self,url,body):
        response= requests.post(url,headers=self.headers,json=body)
        if response.ok:
           return response.json()
        else:
            self.fail(response.status_code)