
from genericpath import exists
import unittest
import os

import keyvalue_class



class TestKeyValueStore(unittest.TestCase):

    def test_init_filepath_none(self):
        with self.assertRaises(TypeError):
            keyValStore = keyvalue_class.KeyValueStore()

    def test_filepath_not_exist(self):
        filepath='/tmp/pyunittest/kv.store'
        keyValStore = keyvalue_class.KeyValueStore(filepath)

        self.assertTrue(os.path.exists(filepath))
        self.assertListEqual([], keyValStore.keyvals)


    def test_keyvalue_store(self):
        expected = [['name', 'foo'], ['age', '10'], ['sex', 'female']]
        filepath = '/tmp/pyunittest/test_kv.store'
        utils = Utils()
        utils.create_test_file(expected, filepath)

        keyValueStore = keyvalue_class.KeyValueStore(filepath)
        observed = [ [keyval.get_key(), keyval.get_value()] for keyval in keyValueStore.keyvals]
        
        self.assertListEqual(expected, observed)
        self.assertEqual(keyValueStore.get_value('age'), '10')
        keyValueStore.set_value('age','11')
        self.assertEqual(keyValueStore.get_value('age'), '11')
        keyValueStore.set_value('name', 'bar')
        keyValueStore.save_keyvals()

        keyValueStore2 = keyvalue_class.KeyValueStore(filepath)
        observed2 = [ [keyval.get_key(), keyval.get_value()] for keyval in keyValueStore2.keyvals]
        expected2 = [['name', 'bar'], ['age', '11'], ['sex', 'female']]
        self.assertListEqual(expected2, observed2)





class Utils:
    def __init__(self) -> None:
        pass

    def create_test_file(self, keyvals, filepath):
        lines = [ k + "=" + v for k,v in keyvals]
        with open(filepath, 'w') as f:
            for line in lines:
                f.write(line + '\n')

        




if __name__ == '__main__':
    unittest.main()