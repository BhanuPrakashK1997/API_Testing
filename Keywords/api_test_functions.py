import requests
import json

class ApiFunctions:

    def __init__(self):
        pass


    def get_method(self, url):
        """
        get the user data in using get_method in api website 'https://reqres.in/api'
        and its return the response will json() format.
        param: url:
        return:
        """

        res = requests.get(url)

        try:
            """ check if an error has occurred"""
            res.raise_for_status()
            print(res.status_code)
            json_obj = res.json()
            print(json_obj)
        except requests.exceptions.HTTPError as e:
            print("Error: "+str(e))
            return


    def post_method(self, url, data):
        """
        user_details assigning the payload_data
        new user_registration and login already existing user using post_method in api web site.
        return the reponse in json()format
        param: url:
        param: data:
        return:
        """
        res = requests.post(url, data)
        try:
            """ check if an error has occurred"""
            res.raise_for_status()

            print(res.status_code)
            json_obj = res.json()
            print(json_obj)
        except requests.exceptions.RequestException as e:
            print("Error: "+str(e))


    def put_method(self, url, data):
        """
        user_details assigning the payload_data variable and
        user data upadte the some required places in in using put_method in api web site
        retrurn the response in json format
        param: url:
        param: data:
        return:
        """

        res = requests.put(url, data)
        try:
            """ check if an error has occurred"""
            res.raise_for_status()

            print(res.status_code)
            json_obj = res.json()
            print(json_obj)
        except requests.exceptions.RequestException as e:
            print("Error: "+str(e))
            return
    def delete_method(self,url):
        """
        find the required user url and delete the user in using delete_method in api website
        and return status code.
        param: url:
        return:
        """
        res = requests.delete(url)
        try:
            """ check if an error has occurred"""
            res.raise_for_status()
            print(res.status_code)
        except requests.exceptions.HTTPError as e:
            print("Error: "+str(e))
            return



    def patch_method(self, url, data):
        """
        user_details assigning the payload_data variable and
        user data upadte the some required places in in using patch_method in api web site
        retrurn the response in the json() format
        param: url
        param: data
        return:
        """
        res = requests.patch(url, data)
        try:
            res.raise_for_status()

            print(res.status_code)
            json_obj = res.json()
            print(json_obj)

        except requests.exceptions.RequestException as e:
            print("Error: "+str(e))

