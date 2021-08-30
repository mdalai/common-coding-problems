import json
import os
from typing import Dict
import logging


logging.basicConfig(filename=f'{__name__}.log', format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)


class KeyValueStore(object):

    def __init__(self, store_path) -> None:
        self.store_path = store_path

        try:    
            self.keyvalue_pairs = self.get_key_values(store_path)
        except Exception as e:
            print(f"Set to {{}} because of following error >>> {e.__class__.__name__}: {e}")
            logging.error(f"Throws Exception >>> {e.__class__.__name__}: {e}")
            self.keyvalue_pairs = {}

    def get_key_values(self, json_filepath: str) -> Dict:
        with open(json_filepath, 'r') as f:
            data = json.load(f)

        return data



    def get_value(self, key: str) -> str:
        ret_val = None
        try:
            ret_val = self.keyvalue_pairs[key]
        except KeyError:
            ret_val = None

        return ret_val

    def set_value(self, key: str, value: str) -> None:
        self.keyvalue_pairs[key] = value


    def store_key_values(self) -> None:
        if not os.path.exists(os.path.dirname(self.store_path)):
            os.makedirs(os.path.dirname(self.store_path))
        
        with open(self.store_path, 'w', encoding='utf-8') as f:
            json.dump(self.keyvalue_pairs, f)



if __name__ == '__main__':
    store_path = 'data/test.json'
    
    keyvalstore = KeyValueStore(store_path)
    print(f"StorePath: {keyvalstore.store_path}, KeyVals: {keyvalstore.keyvalue_pairs}")

    print(keyvalstore.get_value('name'))
    keyvalstore.set_value('name', 'foo')
    keyvalstore.set_value('age', '100')

    print(f"StorePath: {keyvalstore.store_path}, KeyVals: {keyvalstore.keyvalue_pairs}")
    print(keyvalstore.get_value('name'))
    print(type(keyvalstore.keyvalue_pairs))

    keyvalstore.store_key_values()






