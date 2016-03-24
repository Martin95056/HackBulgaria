from basefield import BaseField


class Field(BaseField):
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        args = ['type="{}"'.format(self.__class__.type)]

        if self.value:
            args.append('value="{}"'.format(self.value))

        return '<input {} />'.format(' '.join(args))
