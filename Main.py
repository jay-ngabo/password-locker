#!/usr/bin/env python3.8
from passwordlocker import User,Credentials
def create_new_user(name,password):
     """
     create new user function
     """
     new_user=User(name,password)
     return new_user

def save_user(user):
    """
    save new user function
    """
    user.save_user()

def dispay_user():
    """
    display an existing user
    """ 
    return User.show_user()

def login_user(name,password):
    """
    user login function
    """   
    check_user = Credentials.verfiy_user(name,password)
    return check_user

def create_new_credential(account,name,password):
    """
    create new credentials 
    """
    new_credentials= Credentials(account,name,password)
    return new_credentials
    
# def save_credentials(credentials):
#     """
#     save credentials to the credentials list
#     """
#     credentials.save_datails()

# def display_accounts_details():
#     """
#     show all the saved credential.
#     """
#     return Credentials.display_credentials()

# def delete_credential(credentials):
#     """
#     delete a credentials from credentials list
#     """
#     credentials.delete_credentials()

# def find_credential(account):
#     """
#     find a credential from the credential list using account
#     """
#     return Credentials.find_credential(account)

# def check_credendtials(account):
#     """
#     check if the credentials entere exist in the list
#     """
#     return Credentials.credential_exist(account)

# def generate_Password():
#     '''
#     generates a random password for the user.
#     '''
#     generated_new_password=Credentials.generatePassword()
#     return generated_new_password

# def copy_credentials(account):
#     """
#     A function that copies the credentials using the pyperclip
#     """
#     return Credentials.copy_credentials(account)

# def main():
#     print("Hello Welcome to PassWord Locker...\n Use these short codes:\n ca-- To Create New Account.\n login---to log in to your account if you already have an account.\n ")
#     short_code=input("").lower().strip()
#     if short_code == 'ca':
#         print("Sigh Up")
#         print('*'* 40)
#         name =input("User_name:")
#         while True:
#                 print(" Use\n  input --to input you password:\n GP--to auto generate a new password")
#                 user_choice= input().lower().strip()
#                 if user_choice =="input":
#                     password= input("Enter Password\n")
#                     break
#                 elif user_choice == 'gp':
#                     password=generate_Password()
#                     break
#                 else:
#                     print("Please enter a valid password")
#         save_user(create_new_user(name,password)) 
#         print("*"*85)  
#         print(f"Hello {name}, Your account has was created succesfully! Your password is: {password}")
#         print("*"*85) 
#     elif short_code == "login":
#         print("*"*50)
#         print("Please enter you name and password")
#         print("*"*50)
#         name= input("name")
#         password= input("password")
#         login=login_user(name,password)
#         if login_user==login:
#             print(f"Hello{name}. Welcome To Password Locker")
#             print('\n')
#     while True:
#         print("Use these  codes:\n create -To Create a new credential \n display -To Display Credentials \n find - Find a credential \n generate - Generate A randomn password \n delete - Delete credential \n exit - Exit the application \n")
#         short_code = input().lower()
#         if short_code == "create":
#             print("Create New Credential")
#             print("."*20)
#             print("Account name ....")
#             account = input().lower()
#             print("Your Account username")
#             name = input()
#             while True:
#                 print(" TP - To type your own pasword if you already have an account:\n GP - To outo generate random Password")
#                 password_Choice = input().lower().strip()
#                 if password_Choice == 'tp':
#                     password = input("Enter Your Own Password\n")
#                     break
#                 elif password_Choice == 'gp':
#                     password = generate_Password()
#                     break
#                 else:
#                     print("Invalid password please try again")
#             save_credentials(create_new_credential(account,name,password))
#             print('\n')
#             print(f"Account Credential for: {account} - UserName: {name} - Password:{password} created succesfully")
#             print('\n')
#         elif short_code == 'displdisplayay':
#             if display_accounts_details():
#                 print("This are all your Accounts: ")
                 
#                 print('*' * 30)
#                 print('_'* 30)
#                 for account in display_accounts_details():
#                     print(f" Account:{account.account} \n User Name:{name}\n Password:{password}")
#                     print('_'* 30)
#                 print('*' * 30)
#             else:
#                 print("No credentials saved!. Use CREATE to Create a new credential")
#         elif short_code == 'find':
#             print("Enter the Account Name you want to search for")
#             search_name = input().lower()
#             if find_credential(search_name):
#                 search_credential = find_credential(search_name)
#                 print(f"Account Name : {search_credential.account}")
#                 print('-' * 50)
#                 print(f"User Name: {search_credential.name} Password :{search_credential.password}")
#                 print('-' * 50)
#             else:
#                 print("The Credential does not exist")
#                 print('\n')
#         elif short_code == 'delete':
#             print("Enter the account name of the Credentials you want to delete")
#             search_name = input().lower()
#             if find_credential(search_name):
#                 search_credential = find_credential(search_name)
#                 print("_"*50)
#                 search_credential.delete_credentials()
#                 print('\n')
#                 print(f"The credentials: {search_credential.account}  has been successfully deleted!!!")
#                 print('\n')
#             else:
#                 print("That Credential you want to delete does not exist")
#         elif short_code == 'generate':

#             password = generate_Password()
#             print(f" {password} Has been generated succesfull")
#         elif short_code == 'exit':
#             print("You Are About To Exit The APP!!!\n Thank you for using the App")
#             break
#         else:
#             print("Wrong Code ... Check your Code to see if it matches the ones in the menu")

#     else:
#          print("Please enter a valid input to continue")

# if __name__ == '__main__':
#     main()