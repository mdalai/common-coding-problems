package repository

type KeyValPairs struct {
	KeyValPairs []KeyVal `json:"keyvals"`
}

type KeyVal struct {
	Key   string `json:"key"`
	Value string `json:"value"`
}
