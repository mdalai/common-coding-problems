package inmem

import (
	"context"
	"errors"
)

type KeyValMemoryRepository struct {
	kvPairs map[string]string
}

func NewKeyValMemoryRepository() *KeyValMemoryRepository {
	kvRepo := &KeyValMemoryRepository{}
	kvRepo.kvPairs = make(map[string]string)
	return kvRepo
}

func (kv KeyValMemoryRepository) GetVal(_ context.Context, key string) (string, error) {
	return kv.getVal(key)
}

func (kv *KeyValMemoryRepository) SetKeyVal(_ context.Context, key string, val string) error {

	kv.setKeyVal(key, val)
	return nil
}

func (kv KeyValMemoryRepository) getVal(key string) (string, error) {
	val, ok := kv.kvPairs[key]
	if !ok {
		return "", errors.New("Key not exist")
	}

	return val, nil
}

func (kv *KeyValMemoryRepository) setKeyVal(key string, val string) {
	kv.kvPairs[key] = val
}
