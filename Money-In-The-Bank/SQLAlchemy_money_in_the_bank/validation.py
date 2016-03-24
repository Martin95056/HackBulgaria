import string


class AtleastOneSymbol:
    def __init__(self, symbols):
        self.__symbols = symbols

    def __call__(self, string):
        return any([ch in self.__symbols for ch in string])


class LengthValidation:
    def __init__(self, length):
        self.__length = length

    def __call__(self, string):
        return len(string) >= self.__length


class PasswordValidator:
    def __init__(self):
        self.__validators = []

    def is_valid(self, password):
        return all([v(password) for v in self.__validators])

    def add_validation(self, validator):
        self.__validators.append(validator)
        return self


SPECIAL_SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
CAPITAL_LETTERS = list(string.ascii_uppercase)


def get_validator(username):
    validator = PasswordValidator()
    validator\
        .add_validation(LengthValidation(8))\
        .add_validation(AtleastOneSymbol(SPECIAL_SYMBOLS))\
        .add_validation(AtleastOneSymbol(CAPITAL_LETTERS))\
        .add_validation(lambda string: any([ch.isdigit() for ch in string]))\
        .add_validation(lambda pwd: username.lower() not in pwd)

    return validator


def email_validation(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False


class EmailNotValidError(Exception):
    pass


class PasswordNotStrongError(Exception):
    pass


class UserBlockedException(Exception):
    pass
