package main

import (
	"context"
	"fmt"

	repomem "github.com/mdalai/repository-go/repository/inmem"
	repojsonfile "github.com/mdalai/repository-go/repository/jsonfile"
	"github.com/mdalai/repository-go/server"
)

func main() {
	ctx := context.Background()

	fmt.Println("======= In-Memory Repository =================")

	// Initiate an in-memory repository
	repo := repomem.NewKeyValMemoryRepository()

	// use the repo to create new server
	kvServer := server.NewServer(repo)
	err := kvServer.SetVal(ctx, "name", "Dee")
	if err != nil {
		fmt.Println(err.Error())
	}
	err = kvServer.SetVal(ctx, "age", "36")
	if err != nil {
		fmt.Println(err.Error())
	}
	val, _ := kvServer.GetVal(ctx, "name")
	fmt.Println(val)
	val, _ = kvServer.GetVal(ctx, "age")
	fmt.Println(val)

	fmt.Println("======= JsonFile Repository =================")

	// Initiate a JsonFile repository
	jsonfilepath := "data/db.json"
	repojson := repojsonfile.New(jsonfilepath)

	// use the repo to create new server
	kvServerJson := server.NewServer(repojson)
	err = kvServerJson.SetVal(ctx, "name", "Dee")
	if err != nil {
		fmt.Println(err.Error())
	}
	err = kvServerJson.SetVal(ctx, "age", "36")
	if err != nil {
		fmt.Println(err.Error())
	}
	val, _ = kvServerJson.GetVal(ctx, "name")
	fmt.Println(val)
	val, _ = kvServerJson.GetVal(ctx, "age")
	fmt.Println(val)
}
