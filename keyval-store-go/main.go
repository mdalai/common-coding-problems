package main

import (
	"fmt"

	"example/mymod/keyvalstore/keyvalstore"
)

func main() {
	fmt.Println("main start ...")

	var kvstore keyvalstore.KeyValStore
	//kvstore = keyvalstore.NewKeyValStoreMemory()
	kvstore = keyvalstore.NewKeyValStoreTxt("test.db")

	kvstore.SaveKeyVal("key1", "value1")
	kvstore.SaveKeyVal("key2", "value2")
	kvstore.SaveKeyVal("key3", "value3")

	k := "key2"
	fmt.Printf("%s: %s \n", k, kvstore.GetVal(k))
	kvstore.DelKeyVal(k)
	fmt.Printf("%s: %s \n", k, kvstore.GetVal(k))

}
