package main

import (
	"context"
	"fmt"

	repomem "github.com/mdalai/repository-go/repository/inmem"
	"github.com/mdalai/repository-go/server"
)

func main() {
	ctx := context.Background()

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
}
