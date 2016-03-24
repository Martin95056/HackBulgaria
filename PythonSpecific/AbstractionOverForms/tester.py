from inputs import *
from form import Form


class LoginForm(Form):
    name = TextInput()
    body = PasswordInput()


l = LoginForm({'name': 'formaaa'})
print(str(l))
