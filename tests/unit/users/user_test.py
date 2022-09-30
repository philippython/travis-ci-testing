import unittest
from models.user import UserModel

class UsersUnitTest(unittest.TestCase):
    def test_create_user(self):
        user = UserModel('Test', 'test1234')

        self.assertEqual(user.username, 'Test')
        self.assertEqual(user.password, 'test1234')



if __name__ == '__main__':
    unittest.main()