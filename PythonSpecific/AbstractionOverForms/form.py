from inputs import SubmitInput
from collections import OrderedDict


class Form:
    def __init__(self, data=None, method='GET', action='', id=None):
        self.__fields = OrderedDict()
        for k, v in vars(self.__class__).items():
            if not callable(v) and '__' not in k:
                self.__fields[k] = v

        self.data = data or {}
        self.method = method
        self.action = action
        self.id = id

    def __str__(self):
        tags = ['<form>']
        tags += [str(field) for _, field in self.__fields.items()]
        tags += [str(field) for _, field in self.data.items()]

        tags.append(str(SubmitInput('Submit')))
        tags.append('</form>')
        return '\n'.join(tags)

    def is_valid(self):
        for _, field in self.__fields.items():
            field.is_valid()
