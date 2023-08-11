import unittest
from main_page import *



######FOR SIGNIN FUCTION#################################
class TestSignIn(unittest.TestCase):
    def test_signin_valid_credentials(self):
        # Enter valid credentials for testing
        user = "test_user"
        code = "test_password"
        
        # Call the function with valid credentials
        self.assertEqual(signin(user, code), True)
        
    def test_signin_invalid_credentials(self):
        # Enter invalid credentials for testing
        user = "invalid_user"
        code = "invalid_password"
        
        # Call the function with invalid credentials
        self.assertEqual(signin(user, code), False)

######FOR SIGNUP_COMMAND FUNCTION##############################        
class TestSignUpCommand(unittest.TestCase):
    def test_signup_command_valid_credentials(self):
        # Enter valid credentials for testing
        user = "test_user"
        code = "test_password"
        confirm_code = "test_password"
        
        # Call the function with valid credentials
        self.assertEqual(signup_command(user, code, confirm_code), True)
        
    def test_signup_command_invalid_credentials(self):
        # Enter invalid credentials for testing
        user = "test_user"
        code = "test_password"
        confirm_code = "invalid_password"
        
        # Call the function with invalid credentials
        self.assertEqual(signup_command(user, code, confirm_code), False)

#############FOR ENCODE FUNCTION##############################
class TestEncode(unittest.TestCase):
    def test_encode_valid_message(self):
        # Enter valid message and key for testing
        message = "test_message"
        key = "test_key"
        
        # Call the function with valid message and key
        self.assertEqual(Encode(key, message), "JGdqZGdzbWVnbQ==")
        
    def test_encode_invalid_message(self):
        # Enter invalid message and key for testing
        message = ""
        key = "test_key"
        
        # Call the function with invalid message and valid key
        self.assertEqual(Encode(key, message), "")
 
########FOR DECODE FUNCTION####################
class TestDecode(unittest.TestCase):
    def test_decode_valid_message(self):
        # Enter valid message and key for testing
        message = "JGdqZGdzbWVnbQ=="
        key = "test_key"
        
        # Call the function with valid message and key
        self.assertEqual(Decode(key, message), "test_message")
        
    def test_decode_invalid_message(self):
        # Enter invalid message and key for testing
        message = ""
        key = "test_key"
        
        # Call the function with invalid message and valid key
        self.assertEqual(Decode(key, message), "")

        
unittest.main()
