package keyvalstore

type KeyValStoreMemory struct {
	keyval_pairs map[string]string
}

func NewKeyValStoreMemory() *KeyValStoreMemory {
	kv_pairs := make(map[string]string)
	return &KeyValStoreMemory{keyval_pairs: kv_pairs}
}

func (kvstore *KeyValStoreMemory) SaveKeyVal(k string, v string) {
	kvstore.keyval_pairs[k] = v
}

func (kvstore *KeyValStoreMemory) GetVal(k string) string {
	return kvstore.keyval_pairs[k]
}

func (kvstore *KeyValStoreMemory) DelKeyVal(k string) {
	delete(kvstore.keyval_pairs, k)
}
