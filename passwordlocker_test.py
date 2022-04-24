import unittest #importing the unittest module
from passwordlocker import User
from passwordlocker import Credentials

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('CalebKabaya', 'Mbuguack')

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.name,'CalebKabaya')
        self.assertEqual(self.new_user.password,'Mbuguack')

    def test_save_user(self):
        """
        test if a new user instance has been saved in the User list
        """  
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)

    def test_show_user(self):
        """
        test to show a user from User list
        """ 
        self.assertEqual(User.show_user(),User.user_list)

    def test_delete_user(self):
        """
        test to delete a user from User list
        """ 
        self.new_user.save_user()
        
        
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),0)

class TestCredentials(unittest.TestCase):
    """
    a class to test and validate user  credentials
    """  
    def setUp(self):
        """
        a method before the other rest run
        """
        self.new_credential= Credentials('email','CalebKabaya','Mbuguack')
    
    def test_init_(self):
        """
        a test to initalize the new credential instance
        """
        self.assertEqual(self.new_credential.account,'email')
        self.assertEqual(self.new_credential.name,'CalebKabaya')
        self.assertEqual(self.new_credential.password,'Mbuguack')
    
    def test_save_credential(self):
        """
        test if the credatial are saved in the sredential list
        """
        self.new_credential.save_datails()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_many_accounts(self):
        """
        test to check if we can save multiple credentials to our credentials list
        """
        self.new_credential.save_datails()
        test_credential= Credentials("Spotify","calebm","121212")
        test_credential.save_datails()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        """
        test method to delete credential
        """
        self.new_credential.save_datails()
        test_credential= Credentials("Spotify","calebm","121212")
        test_credential.save_datails()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials(self):
        """
        test to find the credentials
        """
        self.new_credential.save_datails()
        test_credential= Credentials("Spotify","calebm","121212")
        test_credential.save_datails()

        my_credential=Credentials.find_credential("Spotify")
        self.assertEqual(my_credential.account,test_credential.account)
  
    def test_credential_exists(self):
        """
        test is a credential exists in the credential list
        """
        self.new_credential.save_datails()
        test_credential= Credentials("Spotify","calebm","121212")
        test_credential.save_datails()
        
        credential_search =Credentials.credential_exist("spotfiy")
        self.assertTrue(credential_search)
     
    def test_display_saved_credential(self):
        """
        test if we can desplay all the credentials saved
        """

        self.assertEqual(Credentials.display_credentials,Credentials.credentials_list)
        
if __name__ == '__main__':
    unittest.main()        