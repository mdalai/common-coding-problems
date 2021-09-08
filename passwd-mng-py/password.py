import os
import utils


class Password:
    def __init__(self, passwd_conf:str):
        
        self.prev_passwords_count = int(utils.get_value('PREVIOUS_PASSWORDS_COUNT', passwd_conf))
        self.at_least_x_char_diff = int(utils.get_value('AT_LEAST_X_CHAR_DIFF', passwd_conf))
        self.passwd_store = utils.get_value('PASSWORD_STORE_PATH', passwd_conf)
        self.passwords = self.get_passwords()

    def get_password(self):
        if self.passwords:
            return utils.decrypt(self.passwords[-1])
        else:
            return None

    def set_password(self, password: str):
        password = password.encode()
        for prev_passwd in self.passwords:
            decrypted_passwd = utils.decrypt(prev_passwd)
            if self._at_least_x_char_diff(decrypted_passwd, password, self.at_least_x_char_diff):
                encrypted_passwd = utils.encrypt(password.decode())
                self.passwords.append(encrypted_passwd)
            else:
                print(f"At least {self.at_least_x_char_diff} charactors difference from previous password")

        if not self.passwords:
            self.passwords.append(utils.encrypt(password))

        while len(self.passwords) > self.prev_passwords_count:
            self.passwords.pop(0)

        utils.save_passwords(self.passwords, self.passwd_store)


    def _at_least_x_char_diff(self, str1: str, str2: str, x:int=8) -> bool:
        str1_chars = [chr for chr in str1]
        str2_chars = [chr for chr in str2]

        count = 0

        for chr in str2_chars:
            if chr not in str1_chars:
                count = count + 1

        return count >= x

   

    def get_passwords(self):
        if os.path.exists(self.passwd_store):
            return utils.read_passwords(self.passwd_store)
        return []



if __name__ == '__main__':
    passwd_conf = 'passwd-mng-py/passwd.conf'
    passwd = Password(passwd_conf)
    print(f"{passwd.at_least_x_char_diff} ... {type(passwd.at_least_x_char_diff)}")
    print(f"The password storage: {passwd.passwd_store}")
    print(f"The current password: {passwd.get_password()}")
    passwd.set_password('652134')
    print(f"The current password: {passwd.get_password()}")
    passwd.set_password('6521341123abcccdd')
    print(f"The current password: {passwd.get_password()}")
    passwd.set_password('xxxabcccdd')
    print(f"The current password: {passwd.get_password()}")
