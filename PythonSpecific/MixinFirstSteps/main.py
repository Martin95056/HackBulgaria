from utils.serializers.serializers import Jsonable, Xmlable


class Panda(Jsonable, Xmlable):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

az = Panda('Martin', 20)
vtoro_az = Panda.from_json(az.to_json())
treto_az = Panda.from_xml(az.to_xml())
print(treto_az.to_xml())
