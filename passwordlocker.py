import pyperclip
import random
import string

from requests import delete


class User :
    """"
     my class which i will use to craeat new instances
     """
    user_list = []

    def __init__(self,name,password):
      self.name = name
      self.password  = password

    def save_user(self):
      """
       a method to save a new user to the list
       """

#       User.user_list.append(self)
    
#     @classmethod
#     def show_user(cls):
#         return cls.user_list

#     def delete_user(self):
#       """
#       method to delete user from  the list
#       """
#       User.user_list.remove(self)


# class Credentials:
#     """
#     Create credentials  class
#     """
#     credentials_list = []
#     def __init__(self,account,name, password):
#         """
#         method that defines user credentials to be stored
#         """
#         self.account = account
#         self.name = name
#         self.password = password

#     def save_datails(self):
#         """
#          a method to save the credentials
#         """
#         Credentials.credentials_list.append(self)

#     def delete_credentials(self):
#          """
#          delete the credentials method
#          """
#          Credentials.credentials_list.remove(self)
#     @classmethod     
#     def find_credential(cls,account):
#       """
#       method to find the credentials from the credential list
#       """
#       for credential in cls.credentials_list:
#         if credential.account == account:
#           return credential
#     @classmethod
#     def credential_exist(cls, account):
#         """
#         Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
#         """
#         for credential in cls.credentials_list:
#             if credential.account == account:
#                 return True
#         return False
#     @classmethod
#     def verfiy_user(clas,name,password):
#       """
#       verift user credentials 
#       """     
#       user_login=""
#       for user in User.user_list:
#         if (user.name==name and user.password==password):
#           user_login == user.name
#           return user_login
    
#     @classmethod
#     def display_credentials(cls):
#       """
#       method to shaw all saved credentials
#       """
#       return cls.credentials_list

#     @classmethod
#     def copy_credentials(cls,account):
#         my_credential= Credentials.find_credential(account)
#         pyperclip.copy(my_credential.password)


#     def generatePassword(stringLength=8):
#         """
#         Generate a random password for the user
#         """
#         password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
#         return ''.join(random.choice(password) for i in range(stringLength))    