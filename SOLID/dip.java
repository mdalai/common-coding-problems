import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

// Dependency Inversion Principle


interface Repository {
    public String get(String key);
    public void set(String key, String value);
}

class FileRepository implements Repository {
    private File file;
    public FileRepository(File file) {
        this.file = file;
    }

    @Override
    public String get(String key) {    
        return getValueFromFile(key);
    }

    @Override
    public void set(String key, String value) {
        saveValueToFile(key, value);        
    }

    private String getValueFromFile(String key) {
        try {
            Scanner reader = new Scanner(this.file);
            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                
                // split with delimeter to key, value
                // if key exist, return value
                // else: continue

            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    private void saveValueToFile(String key, String value) {
        // read file first, if key is already exist, update value
        // save key value to the file
    }

}

class DbRepository implements Repository {

    @Override
    public String get(String key) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public void set(String key, String value) {
        // TODO Auto-generated method stub
        
    }
    
}


// This class stays same if you use different repositories
class KeyValueStore {
    private Repository repository;

    public KeyValueStore (Repository repository) {
        this.repository = repository;
    }

    public void save(String key, String value) {
        this.repository.set(key, value);
    }

    public String getVal(String key) {
        return this.repository.get(key);
    }
}


public static void main(String[] args) {
    File file = new File("key.store");
    Repository repository = new FileRepository(file);

    KeyValueStore keyValueStore = new KeyValueStore(repository);
    keyValueStore.getVal("key1");
    keyValueStore.save("key1", "value1");

}