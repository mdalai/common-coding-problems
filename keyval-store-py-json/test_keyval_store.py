from unittest.main import main
from keyval_store import KeyValueStore
import unittest


class TestKeyValueStore(unittest.TestCase):

    def test_store_path_not_exist(self):
        store_path = "/non/exist/filepath"
        keyValueStore = KeyValueStore(store_path)        

        self.assertDictEqual({}, keyValueStore.keyvalue_pairs)

    def test_store_file_not_json(self):
        store_path="/tmp/a_not_json_file"
        with open(store_path, 'w') as f:
            f.write("hello world!")

        keyValueStore = KeyValueStore(store_path)        
        self.assertDictEqual({}, keyValueStore.keyvalue_pairs)   


if __name__ == '__main__':
    unittest.main()