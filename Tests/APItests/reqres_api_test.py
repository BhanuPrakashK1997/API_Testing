import requests

from Keywords.api_test_functions import ApiFunctions
import json

""" 
Keywords dorectory change to the module
and import modyle keywords
ApiFunctions() assigning the new variable that is rfunction
"""
rfunction = ApiFunctions()

# with open('../TestData/data.json','r+') as file:
#     j_data = json.loads(file)



""" 
API TEST USING GET_METHOD() IT IS CALLING BY KEYWORD IN ApiFunctions()
get the all user list in using get_method is contains url in api website 
return the response json() format 
"""
rfunction.get_method('https://reqres.in/api/users?page=2')




"""
USER NOT FOUND GET_METHOD() CALLING ON KEYWORD IN ApiFunctions()
 get the all user list in using get_method is contains url in api website 
 but thi case post_request url is not valid and raise an Errors NotFoundUrl
 """
rfunction.get_method('https://reqres.in/api/users/233')





"""
 GET SINGLE USER DATA FAILED CASE TESING GET_METHOD() CALLING ON KEYWORD IN ApiFunctions()
get the single_user list in using get_method is contains url in api website 
but it will be post_request the  request the url is not valid  raise an Errors NotFoundUrl 
 
 """
rfunction.get_method('https://reqres.in/api/users/23')






"""
 GET ALL UNKNOWN USER DATA USING GET_METHOD() CALLING ON KEYWORD IN ApiFunctions()
get the all unkown_user list in using get_method is contains url in api website 
return the data son() format 
return the response json() format 
"""
rfunction.get_method('https://reqres.in/api/unknown')





""" 
 GET SINGLE UNKNOWN USER DATA USING GET_METHOD() CALLING ON KEYWORD IN ApiFunctions() 
get the single unkown_user list in using get_method is contains url in api website 
return the response json() format 
"""
rfunction.get_method('https://reqres.in/api/unknown/2')





"""
 GET SINGLE UNKNOWN USER DATA NOT FOUND CASE USING GET_METHOD() CALLING ON KEYWORD IN ApiFunctions()
get the single unkown_user list in using get_method is contains in_valid_url in api website 
but it will be post request the  request the url is not valid  raise an Errors NotFoundUrl 
 """
rfunction.get_method('https://reqres.in/api/unknown/23')

"""get delay response"""
rfunction.get_method('https://reqres.in/api/users?delay=5')





""" API TEST USING POST METHOD """

"""
user registration succesful using post_METHOD calling by Keyword  IN ApiFunctions()
payload file named is user_register and 
request the register user in using_post method its may contains url and data of api website
return data from json() format
"""
user_register = {
    "email": "eve.holt@reqres.in",
    "password": "python"
    }
rfunction.post_method('https://reqres.in/api/register',data=user_register)




""" 
user registration unsuccesful using post_method  calling by kaywords IN ApiFunctions()
request the register user in using_post method its may contains url and data of api website
 payload details is not fullfill of the registration requirment and that case to registraion of user unsuccfel
 """

user_unregister = {
    "email": "krishna@fife"
    }
rfunction.post_method('https://reqres.in/api/register',data=user_unregister)





""" 
login the user using post_method  calling by kaywords IN ApiFunctions()
user_credentials assign to user_login variable 
and request the login user in using_post method its may contains url and data of api website
return the data from json() format  
 """
user_login = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }
rfunction.post_method('https://reqres.in/api/login',data=user_login)





""" 
loginfail the user using post_method() calling by keywords IN ApiFunctions()
request the login user in using_post method its may contains url and data of api website
 payload credintials is not fill of the login requirment and that case to login of user unsuccful eas failed
 """
user_loginfail = {
    "email": "eve.holt@reqres.in"
    }
rfunction.post_method('https://reqres.in/api/login',data=user_loginfail)






""" API TEST USING PUT METHOD """



""" 
user data update using put_method() calling by keywords IN ApiFunctions()
user_details assigning the payload_data variable and
user data upadte the required user in in using put_method in api web site
retrurn the response in json format
"""
put_data = {
    "name": "morpheus",
    "job": "Python Selenium"
    }
rfunction.put_method('https://reqres.in/api/users/2',data=put_data)






#
""" API TEST USING PATCH METHOD """

"""
user data update using patch_method() calling by keywords IN ApiFunctions()
user_details assigning the payload_data variable and
user data upadte the required_user in some  places in  using patch_method in api web site
retrurn the response in the json() format
param: url
"""
patch_data = {
    "name": "Bhanu",
    "job": "QA team"
    }
rfunction.patch_method('https://reqres.in/api/users/2',data=patch_data)





""" API TEST USING DELETE METHOD """

""" 
delete data in user using DELEtE_method() calling by keywords IN ApiFunctions()
find the required user url and delete the user in using delete_method in api website
and return status code.
"""
rfunction.delete_method('https://reqres.in/api/users/2')

