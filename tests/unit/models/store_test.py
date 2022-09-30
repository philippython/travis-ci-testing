import unittest
from models.store import StoreModel
from models.item import ItemModel

class StoreUnitTest(unittest.TestCase):

    def test_store_init(self):

        store = StoreModel("Starbucks")

        self.assertEqual(store.name, "Starbucks")

if __name__ == "__main__":
    unittest.main()