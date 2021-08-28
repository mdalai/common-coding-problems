

class Password:
    def __init__(self):
        self.password = None
        self.previous_passwords = self.get_previous_passwords()

    def get_password(self):
        return self.password

    def set_password(self, password: str):
        for prev_passwd in self.previous_passwords:
            if self._at_least_x_char_diff(prev_passwd, password):
                self.password = password
            else:
                print(f"At least 8 charactors difference from previous password")


    def _at_least_x_char_diff(self, str1: str, str2: str, x:int=8) -> bool:
        str1_chars = [chr for chr in str1]
        str2_chars = [chr for chr in str2]

        count = 0

        for chr in str2_chars:
            if chr not in str1_chars:
                count = count + 1

        print(count)

        return count >= x


    

    def get_previous_passwords(self):
        # Read passwords from a file
        return ['abcdefghi12345678']



if __name__ == '__main__':
    passwd = Password()
    passwd.set_password('passworduuuii')