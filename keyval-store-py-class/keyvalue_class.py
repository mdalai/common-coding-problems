import os


class KeyValueStore:
    '''Store/Retrive key value from a file storage
    '''
    def __init__(self, filepath: str):
        if not os.path.exists(filepath): 
            print(f"Storage: {filepath} not exist. Creating ...")
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            open(filepath,'a').close()
        self.filepath = filepath
        self.keyvals = self.get_keyvals(filepath)


    def get_keyvals(self, filepath=None):
        if filepath:
            with open(filepath) as f:
                lines = f.readlines()
            kv_list = [line.strip("\n").split("=") for line in lines]
            return [KeyValue(k, v) for k,v in kv_list]
        else:
            return self.keyvals

    
    def get_value(self, key):
        for kv in self.keyvals:
            if kv.get_key() == key:
                return kv.get_value()

    def set_value(self, key, value):
        found = 0
        for kv in self.keyvals:
            if kv.get_key() == key:
                kv.set_value(value)
                found = 1
        if not found:
            self.keyvals.append(KeyValue(key, value))

    
    def print_keyvals(self):
        for kv in self.keyvals:
            print(f"{kv.get_key()}: {kv.get_value()}")

    def save_keyvals(self):
        with open(self.filepath, 'w') as f:
            for kv in self.keyvals:
                f.write(kv.get_key() + "=" + kv.get_value() + "\n")


class KeyValue:

    def __init__(self, key, value):
        self.key = key
        self.value = value 

    def get_key(self):
        return self.key
    
    def get_value(self):
        return self.value

    def set_key(self, key):
        self.key = key
        
    def set_value(self, value):
        self.value = value


def main():

    keyvaluePaires = KeyValueStore('keyval.store')
    keyvaluePaires.print_keyvals()

    name = keyvaluePaires.get_value('name')
    print(f"Name: {name}")

    keyvaluePaires.set_value('name','foo')
    name = keyvaluePaires.get_value('name')
    print(f"Name: {name}")

    keyvaluePaires.set_value('mode', 'angry')
    keyvaluePaires.set_value('machine', 'Mac')

    keyvaluePaires.save_keyvals()



if __name__ == '__main__':
    main()

