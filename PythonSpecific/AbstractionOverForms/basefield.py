from abc import ABCMeta, abstractmethod


class BaseField(metaclass=ABCMeta):
    def is_valid(self):
        return True

    @abstractmethod
    def __str__(self):
        pass
