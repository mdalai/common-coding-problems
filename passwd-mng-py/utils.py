

from cryptography.fernet import Fernet
from typing import ByteString, Dict, List

import secret

KEYSTORE = '.my.sec'
PASSWDSTORE = '.my.passwd'


def read_conf(conf_path: str) -> Dict:
    with open(conf_path, 'r') as f:
        lines = f.readlines()

    lines = [ line.strip()  for line in lines]
    p = [line.split("=") for line in lines]
    #p = [it.strip()  for it in p]
    return {kv[0]:kv[1] for kv in p}

def get_value(key: str, conf_path: str) -> str:
    keyvals = read_conf(conf_path)
    return keyvals[key]


def encrypt(plain_text: str) -> str:
    key = secret.get_secret_key(KEYSTORE)
    
    cipher_suite = Fernet(key)
    encoded_text = cipher_suite.encrypt(str.encode(plain_text))
    return encoded_text

def decrypt(encrypted_txt: str) -> str:
    key = secret.get_secret_key(KEYSTORE)
    cipher_suite = Fernet(key)
    decoded_text = cipher_suite.decrypt(encrypted_txt)
    return decoded_text


def read_passwords(passwd_store: str) -> List[ByteString]:
    with open(passwd_store, 'rb') as f:
        passwds = f.readlines()
    return [passwd.strip()  for passwd in passwds]

def save_passwords(passwds: List[ByteString], passwd_store: str):
    with open(passwd_store, 'wb') as f:
        for passwd in passwds:
            f.write(passwd + str.encode("\n"))




if __name__ == '__main__':
    conf_path = 'passwd-mng-py/passwd.conf'
    print(read_conf(conf_path))
    print(get_value('PREVIOUS_PASSWORDS_COUNT', conf_path))

    all_passwords = []

    just_a_passwd = '123456'
    encrypted_passwd = encrypt(just_a_passwd)
    print(f"Text: {just_a_passwd} is encrypted to {encrypted_passwd}")
    all_passwords.append(encrypted_passwd)
    save_passwords(all_passwords, PASSWDSTORE)
    passwds = read_passwords(PASSWDSTORE)
    for passwd in passwds:
        decrypted_passwd = decrypt(passwd)
        print(f"{passwd} is decrypted to {decrypted_passwd}")

    just_a_passwd2 = '654321'
    encrypted_passwd = encrypt(just_a_passwd2)
    print(f"Text: {just_a_passwd2} is encrypted to {encrypted_passwd}")
    all_passwords.append(encrypted_passwd)
    save_passwords(all_passwords, PASSWDSTORE)
    passwds = read_passwords(PASSWDSTORE)
    for passwd in passwds:
        decrypted_passwd = decrypt(passwd)
        print(f"{passwd} is decrypted to {decrypted_passwd}")



    