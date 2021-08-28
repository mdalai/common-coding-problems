
class KeyValuePairs:
    def __init__(self, filepath):
        self.filepath = filepath
        self.keyvals = {}
        if filepath:
            self.keyvals = self.get_keyvals(filepath)


    def get_keyvals(self, filepath=None):
        if filepath:
            with open(filepath) as f:
                lines = f.readlines()
            kv_list = [line.strip("\n").split("=") for line in lines]
            return {k:v for k,v  in kv_list}
        else:
            return self.keyvals

    
    def get_value(self, key):
        return self.keyvals[key]

    def set_value(self, key, value):
        self.keyvals[key] = value
  
    def print_keyvals(self):
        for k,v in self.keyvals.items():
            print(f"{k}: {v}")

    def save_keyvals(self):
        with open(self.filepath, 'w') as f:
            for k,v in self.keyvals.items():
                f.write(k + "=" + v + "\n")



def main():

    keyvaluePaires = KeyValuePairs('keyval.store')
    keyvaluePaires.print_keyvals()

    name = keyvaluePaires.get_value('name')
    print(f"Name: {name}")

    keyvaluePaires.set_value('name','foo')
    name = keyvaluePaires.get_value('name')
    print(f"Name: {name}")

    keyvaluePaires.set_value('mode', 'angry')
    keyvaluePaires.set_value('machine', 'PC')
    keyvaluePaires.set_value('action', 'sleep')

    keyvaluePaires.save_keyvals()



if __name__ == '__main__':
    main()

