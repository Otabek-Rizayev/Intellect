import pickle as p
from getpass import getpass
from rich import print


class Registration():
    def __main__(self, login, password, password2, data_base, signup):
        self.login = login
        self.password = password
        self.password2 = password2
        self.data_base = data_base
        self.sign_up = sign_up

    def new_login(self):
        self.login = input("Login: ").isalpha()
        return self.login

    def new_password(self):
        self.password = getpass("Password: ")
        return self.password

    def confirm_password(self):
        self.password2 = getpass("Confirm password: ")
        return self.password2

    def data_base(self):
        with open("data_base", "wb") as file:
            p.dump(self.password, file)
        #self.data_base[self.login] = self.password

    def login(self):
        print("Kirish")
        with open("data_base", "rb") as file:
            p.readline(file)
        self.login = input("Login: ")
        return self.login
