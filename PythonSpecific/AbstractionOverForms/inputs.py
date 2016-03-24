from field import Field


class TextInput(Field):
    type = "text"


class PasswordInput(Field):
    type = "password"

    def is_valid(self):
        if len(self.value) >= 8:
            return True
        else:
            raise ValidationError('Wrong value')


class EmailInput(Field):
    type = "email"

    def is_valid(self):
        if '@' in self.value and '.' in self.value:
            return True
        else:
            raise ValidationError('Wrong value')


class SubmitInput(Field):
    type = "submit"


class ValidationError(Exception):
    pass
