class Plant:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name
        return


obj = Plant("object")
print(obj.get_name())


class Wood(Plant):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


oak = Wood("oak", "brown")
print(oak.get_name())
print(oak.color)


class Furniture:
    def __init__(self, furniture_name, name, color):
        self.furniture_name = furniture_name
        self.wood = Wood(name, color)


furniture = Furniture("bench", "pine", "light brown")
print(furniture.furniture_name)
print(furniture.wood.get_name())
print(furniture.wood.color)


class ClassB:
    class_variable = 2

    def __init__(self, object_variable):
        self.object_variable = object_variable

    @classmethod
    def class_method(cls):
        cls.class_variable = 3
        return

    def object_method(self):
        self.object_variable = "longer_string"
        return


obj1 = ClassB("string")
obj2 = ClassB("also a string")

print(obj1.object_variable)
print(obj2.object_variable)
obj1.object_method()
print(obj1.object_variable)
print(obj2.object_variable)

print(obj1.class_variable)
print(obj2.class_variable)
ClassB.class_method()
print(obj1.class_variable)
print(obj2.class_variable)
