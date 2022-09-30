import unittest
from models.user import UserModel
from tests.base_test  import BaseTest

class UsersTest(BaseTest):

    def test_crud(self):
        with self.app_context():
            user = UserModel('Test', 'test1234')

            self.assertIsNone(UserModel.find_by_id(1))
            self.assertIsNone(UserModel.find_by_username('Test'))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_id(1))
            self.assertIsNotNone(UserModel.find_by_username('Test'))


if __name__ == '__main__':
    unittest.main()