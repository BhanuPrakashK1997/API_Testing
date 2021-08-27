from Keywords.api_test_functions import ApiFunctions
import json

rfunction = ApiFunctions()
#
# with open('../TestData/data.json','r+') as file:
#     j_data = json.loads(file)

""" API TEST USING GET METHOD """
""" user list """
rfunction.get_method('https://reqres.in/api/users?page=2')

"""user not found """
rfunction.get_method('https://reqres.in/api/users/23')


"""get single uer data """
rfunction.get_method('https://reqres.in/api/users/2')

"""get unknown user list """
rfunction.get_method('https://reqres.in/api/unknown')

""" get single user data """
rfunction.get_method('https://reqres.in/api/unknown/2')

"""get single user data not found  """
rfunction.get_method('https://reqres.in/api/unknown/23')

"""get delay response"""
rfunction.get_method('https://reqres.in/api/users?delay=5')



""" API TEST USING POST METHOD """

""" user registration succesful using post method """
user_register = {
    "email": "eve.holt@reqres.in",
    "password": "python"
    }
rfunction.post_method('https://reqres.in/api/register',data=user_register)


""" user registration unsuccesful using post method """
user_unregister = {
    "email": "krishna@fife"
    }
rfunction.post_method('https://reqres.in/api/register',data=user_unregister)

""" login the user using post method """
user_login = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }
rfunction.post_method('https://reqres.in/api/login',data=user_login)

""" loginfail the user using post method """
user_loginfail = {
    "email": "eve.holt@reqres.in"
    }
rfunction.post_method('https://reqres.in/api/login',data=user_loginfail)





""" API TEST USING PUT METHOD """

""" user data update using put method """
put_data = {
    "name": "morpheus",
    "job": "Python Selenium"
    }
rfunction.put_method('https://reqres.in/api/users/2',data=put_data)



""" API TEST USING PATCH METHOD """

""" user data update using patch method """
patch_data = {
    "name": "Bhanu",
    "job": "QA team"
    }
rfunction.patch_method('https://reqres.in/api/users/2',data=patch_data)



""" API TEST USING DELETE METHOD """

""" delete data in user using DELEtE method"""
rfunction.delete_method('https://reqres.in/api/users/2')

