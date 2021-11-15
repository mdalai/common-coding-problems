package server

import (
	"context"

	repo "github.com/mdalai/repository-go/repository"
)

type keyValServer struct {
	kvRepository repo.Repository
}

func NewServer(kvRepo repo.Repository) *keyValServer {
	return &keyValServer{kvRepository: kvRepo}
}

func (kv keyValServer) GetVal(ctx context.Context, key string) (string, error) {
	return kv.kvRepository.GetVal(ctx, key)
}

func (kv keyValServer) SetVal(ctx context.Context, key string, val string) error {

	return kv.kvRepository.SetKeyVal(ctx, key, val)
}
