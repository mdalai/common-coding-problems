package jsonstore

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"

	repo "github.com/mdalai/repository-go/repository"
)

type KeyValueJsonFileRepository struct {
	jsonFilepath string
}

func New(filepath string) *KeyValueJsonFileRepository {
	kvRepo := &KeyValueJsonFileRepository{}
	kvRepo.jsonFilepath = filepath
	return kvRepo
}

func (kv KeyValueJsonFileRepository) GetVal(_ context.Context, key string) (string, error) {
	return kv.getVal(key)
}

func (kv *KeyValueJsonFileRepository) SetKeyVal(_ context.Context, key string, val string) error {

	kv.setKeyVal(key, val)
	return nil
}

func (kv KeyValueJsonFileRepository) getVal(key string) (string, error) {
	kvals, _ := kv.readJsonFile()
	var val string
	for _, kval := range kvals {
		if kval.Key == key {
			val = kval.Value
			break
		}
	}
	return val, nil
}

func (kv KeyValueJsonFileRepository) setKeyVal(key string, val string) {
	kvals, _ := kv.readJsonFile()

	keyNotExist := true
	for _, kval := range kvals {
		if kval.Key == key {
			keyNotExist = false
			break
		}
	}

	if keyNotExist {
		newKeyVal := repo.KeyVal{
			Key:   key,
			Value: val,
		}
		newKeyVals := append(kvals, newKeyVal)
		kv.writeJsonFile(newKeyVals)
	}
}

func (kv *KeyValueJsonFileRepository) readJsonFile() ([]repo.KeyVal, error) {
	data, err := ioutil.ReadFile(kv.jsonFilepath)
	if err != nil {
		fmt.Println("error: ", err)
		return nil, errors.New("Read Json file failed!")
	}

	var keyvals repo.KeyValPairs
	err = json.Unmarshal(data, &keyvals)
	if err != nil {
		fmt.Println("error: ", err)
		return nil, errors.New("Josn Unmarshal failed!")
	}

	return keyvals.KeyValPairs, nil
}

func (kv *KeyValueJsonFileRepository) writeJsonFile(keyvalList []repo.KeyVal) error {
	keyvalPairs := repo.KeyValPairs{KeyValPairs: keyvalList}
	keyvalPairsJson, _ := json.MarshalIndent(keyvalPairs, "", "  ")
	err := ioutil.WriteFile(kv.jsonFilepath, keyvalPairsJson, 0644)
	if err != nil {
		fmt.Println("error: ", err)
		return errors.New("Write to Json file failed!")
	}

	return nil
}
