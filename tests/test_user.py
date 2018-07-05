import unittest
from app.models import User
class UserModelTest(unittest.Testcase):
    def setUp(self):
        '''
        class that runs before any test
        '''
        self.new_user=User(password='lambalolo')
    def test_pass_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    def test_no_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
    def test_pass_verification(self):
        self.assertTrue(self.new_user.verify_password('lambalolo'))
