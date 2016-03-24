from models import Client
from hashers import hash_pass
from validation import get_validator, PasswordNotStrongError,\
                        email_validation, EmailNotValidError


class ClientAlreadyRegistered(Exception):
    pass


class NoSuchCLient(Exception):
    pass


class WithdrawError(Exception):
    pass


class MainController:
    def register(self, email, name, password):
        user = self.session.query(Client).\
                filter(Client.email == email).first()

        if user is not None:
            raise ClientAlreadyRegistered('Client already registered.')

        if not get_validator(email.split("@")[0]).is_valid(password):
            raise PasswordNotStrongError

        if not email_validation(email):
            raise EmailNotValidError

        hashed_pass, salt = hash_pass(password)

        client = Client(email=email, name=name, password=hashed_pass, salt=salt)
        self.__commit_object(client)

    def change_message(self, new_message, logged_user):
        user = self.session.query(Client).\
                filter(Client.email == logged_user.email).first()

        if user is None:
            raise NoSuchCLient('There is no such client.')

        user.message = new_message
        self.__commit()

    def change_password(self, new_password, logged_user):
        user = self.session.query(Client).\
                filter(Client.email == logged_user.email).first()

        if user is None:
            raise NoSuchCLient('There is no such client.')

        hashed_pass, salt = hash_pass(new_password)

        user.password = hashed_pass
        user.salt = salt
        self.__commit()

    def login(self, email, password):
        hashed_pass, salt = hash_pass(password)
        user = self.session.query(Client).\
                filter(Client.email == email,
                       Client.password == hashed_pass,
                       Client.salt == salt).first()
        if user:
            return Client(email=email, name=user.name,
                            password=hashed_pass, salt=salt)
        else:
            raise NoSuchCLient('There is no such client.')

    def __commit(self):
        self.session.commit()

    def __commit_object(self, obj):
        self.session.add(obj)
        self.__commit()

    def __commit_objects(self, objects):
        self.session.add_all(objects)
        self.__commit()

    def __init__(self, session):
        self.session = session


class TransactionController:
    def __init__(self, session):
        self.session = session

    def __commit(self):
        return self.session.commit()

    def deposit(self, client, money_amount):
        if money_amount >= 0:
            raise ValueError("You want to deposit invalid sum.")

        user = self.session.query(Client).\
                filter(Client.email == client.email).first()

        if user is None:
            raise NoSuchCLient('There is no such client.')

        user.balance += money_amount
        self.__commit()

    def withdraw(self, client, money_amount):
        if money_amount <= 0:
            raise ValueError("You want to withdraw invalid sum.")

        user = self.session.query(Client).\
                filter(Client.email == client.email).first()

        if user is None:
            raise NoSuchCLient('There is no such client.')

        if user.balance - money_amount < 0:
            raise WithdrawError("You don't have enough money.")
        else:
            user.balance -= money_amount

        self.__commit()

    def display_balance(self, client):
        user = self.session.query(Client).\
                filter(Client.email == client.email).first()
        if user is None:
            raise NoSuchCLient('There is no such client.')

        return "{}$".format(user.balance)
