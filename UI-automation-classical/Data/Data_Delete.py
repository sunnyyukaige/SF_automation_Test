from API.requestHttp import BaseRequest

class Data_Delete:

    def _init_(self):
        headers={}
        self.baseRequest=BaseRequest(headers)

    def delete_customer(self,id):
        self.baseRequest.get()