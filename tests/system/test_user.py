from models.user import UserModel
from tests.base_test import BaseTest
import unittest , json

class UserTest(BaseTest):
    
    def test_register_user(self):
        data = {'username' : 'Test','password' : 'Test1234'}
        headers = { "content-Type": "application/json"}
        with self.test_client() as client:
            with self.app_context() :
                response = client.post('/register', data=json.dumps(data), headers=headers)
                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('Test'))
                self.assertDictEqual(json.loads(response.data), {"message": "User created successfully."})

    def test_register_and_login(self):
        data = {'username' : 'Test','password' : 'Test1234'}
        headers = { "content-Type": "application/json"}
        with self.test_client() as client:
            with self.app_context() :
                client.post('/register', data=json.dumps(data), headers=headers)
                auth_request = client.post('/auth', data=json.dumps(data), headers=headers)

                self.assertIn('access_token', json.loads(auth_request.data).keys())
    
    def test_register_duplicate_user(self):
        data = {'username' : 'Test','password' : 'Test1234'}
        headers = { "content-Type": "application/json"}
        with self.test_client() as client:
            with self.app_context() :
                client.post('/register', data=json.dumps(data), headers=headers)
                response = client.post('/register', data=json.dumps(data), headers=headers)

                self.assertDictEqual({"message": "A user with that username already exists"}, json.loads(response.data))
                self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()