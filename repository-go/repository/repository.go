package repository

import "context"

type Repository interface {
	GetVal(ctx context.Context, key string) (string, error)
	SetKeyVal(ctx context.Context, key string, val string) error
}
