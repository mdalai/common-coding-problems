// Only read file at the beginning, save to file everytime saves key value.

package keyvalstore

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type KeyValStoreTxt struct {
	filepath string
	kvpairs  map[string]string
}

func NewKeyValStoreTxt(fpath string) *KeyValStoreTxt {
	kv_pairs := readKeyValPairsFromFile2(fpath)
	return &KeyValStoreTxt{filepath: fpath, kvpairs: kv_pairs}
}

func (kvstore *KeyValStoreTxt) SaveKeyVal(k string, v string) {
	kvstore.kvpairs[k] = v
	kvstore.saveKeyValPairsToFile()
}

func (kvstore *KeyValStoreTxt) GetVal(k string) string {
	return kvstore.kvpairs[k]
}

func (kvstore *KeyValStoreTxt) DelKeyVal(k string) {
	delete(kvstore.kvpairs, k)
	kvstore.saveKeyValPairsToFile()
}

func readKeyValPairsFromFile2(fpath string) map[string]string {
	kvpairs := make(map[string]string)
	f, err := os.OpenFile(fpath, os.O_CREATE, 0644)
	if err != nil {
		fmt.Printf("File open error: %s", err)
		os.Exit(2)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		kv_arr := strings.Split(line, "=")
		kvpairs[kv_arr[0]] = kv_arr[1]
	}
	return kvpairs
}

func (kvstore *KeyValStoreTxt) readKeyValPairsFromFile() {
	f, err := os.OpenFile(kvstore.filepath, os.O_CREATE, 0644)
	if err != nil {
		fmt.Printf("File open error: %s", err)
		os.Exit(2)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		kv_arr := strings.Split(line, "=")
		kvstore.kvpairs[kv_arr[0]] = kv_arr[1]
	}
}

func (kvstore *KeyValStoreTxt) saveKeyValPairsToFile() {
	// %p format can print the memory address
	fmt.Printf("%v, %p \n", kvstore.kvpairs, &kvstore.kvpairs)

	// To overwrite file content, must add os.O_TRUNC
	f, err := os.OpenFile(kvstore.filepath, os.O_CREATE|os.O_RDWR|os.O_TRUNC, 0644)
	if err != nil {
		fmt.Printf("Open File for writing error: %s", err)
	}
	defer f.Close()

	// Write-1: no buffer
	// for k, v := range kvstore.kvpairs {
	// 	f.WriteString(k + "=" + v + "\n")
	// }
	// f.Sync()

	// Write-2: with buffer
	writer := bufio.NewWriter(f)
	for k, v := range kvstore.kvpairs {
		fmt.Printf("Writing: %s = %s \n", v, v)
		_, err = writer.WriteString(k + "=" + v + "\n")
		if err != nil {
			fmt.Printf("Flush error: %s", err)
		}
	}
	writer.Flush()
}
