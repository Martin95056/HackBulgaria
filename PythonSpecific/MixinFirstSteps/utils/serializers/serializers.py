import xml.etree.ElementTree as ET
import json


class clsName:
    @property
    def class_name(self):
        return self.__class__.__name__


class Jsonable(clsName):
    def to_json(self):
        dic = {
            "name": self.class_name,
            "properties": self.__dict__
        }
        return json.dumps(dic, indent=4)

    @classmethod
    def from_json(cls, json_string):
        dic = json.loads(json_string)
        return cls(**dic['properties'])


class Xmlable(clsName):
    def to_xml(self):
        name = ET.Element('{}'.format(self.class_name))
        for k in self.__dict__:
            prop = ET.SubElement(name, '{}'.format(k))
            prop.text = str(self.__dict__[k])
        return ET.tostring(name)

    @classmethod
    def from_xml(cls, xml_string):
        root = ET.fromstring(xml_string)
        props = {child.tag: child.text for child in root}

        return cls(**props)
