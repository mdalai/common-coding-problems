package keyvalstore

type KeyValStore interface {
	SaveKeyVal(key string, value string)
	GetVal(key string) string
	DelKeyVal(key string)
}
