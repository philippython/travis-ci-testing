from models.store import StoreModel
from tests.base_test import BaseTest
import unittest , json

class StoreTest(BaseTest):
    
    def test_create_store(self):
        with self.app_context() :
            with self.test_client() as client :
                request = client.post('/store/AppleStore', data={'name':'AppleStore'}, headers= { "content-Type": "application/json"})

                self.assertEqual(request.status_code, 201)
                self.assertDictEqual(json.loads(request.data), {'name': 'AppleStore', 'items':[]})
    
    def test_create_duplicate_store(self):
        with self.app_context() :
            with self.test_client() as client :
                client.post('/store/AppleStore', data={'name':'AppleStore'}, headers= { "content-Type": "application/json"})
                request = client.post('/store/AppleStore', data={'name':'AppleStore'}, headers= { "content-Type": "application/json"})
                
                self.assertDictEqual(json.loads(request.data), {'message': f"A store with name 'AppleStore' already exists."})


    def test_delete_store(self):
        with self.app_context() :
            with self.test_client() as client :
                client.post('/store/AppleStore', data={'name':'AppleStore'}, headers= { "content-Type": "application/json"})

                request = client.delete('/store/AppleStore')
                self.assertEqual(request.status_code, 200)
                self.assertDictEqual(json.loads(request.data), {'message':'Store deleted'})

    def test_find_store(self):
        with self.app_context() :
            with self.test_client() as client :
                client.post('/store/AppleStore', data={'name':'AppleStore'}, headers= { "content-Type": "application/json"})

                request = client.get('/store/AppleStore')
                self.assertEqual(request.status_code, 200)
                self.assertDictEqual(json.loads(request.data), {'name':'AppleStore',  'items': []})

                client.delete('/store/AppleStore')
                request = client.get('/store/AppleStore')
                self.assertEqual(json.loads(request.data), {'message': 'Store not found'})


#
# if __name__ == "__main__":
#     unittest.main()