import requests
import json

class ApiFunctions:

    def __init__(self):
        """
        """
        self.response = requests


    def get_method(self, url):
        """

        """
        res_json = self.response.get(url)
        print(res_json.json())



    def post_method(self, url, data):
        """

        """
        res = self.response.post(url, data)
        print(res.status_code)
        print(res.json())

    def put_method(self, url, data):
        """

        """
        res = self.response.put(url, data)
        print(res.status_code)
        print(res.json())

    def delete_method(self,url):
        """

        """
        res = self.response.delete(url)
        print(res.status_code)

    def patch_method(self, url, data):
        """
        """
        res = self.response.patch(url, data)
        print(res.status_code)
