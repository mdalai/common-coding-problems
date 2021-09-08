import os
from cryptography.fernet import Fernet
from typing import ByteString


def gen_secret_key(key_store: str) -> None:
    key = Fernet.generate_key()
    with open(key_store, 'wb') as f:
        f.write(key)


def get_secret_key(key_store: str) -> ByteString:
    if not os.path.exists(key_store):
        gen_secret_key(key_store)

    with open(key_store, 'rb') as f:
        secret = f.read()
    return secret


if __name__ == '__main__':
    keystore = 'my.sec'
    secret = get_secret_key(keystore)
    print(secret)
