import inspect


class Animal:
    _all = []

    def __init__(self, age=0, gender=None, legs_count=None, has_wings=None, name_class=__qualname__.lower()):
        self._age = age
        self.gender = gender
        self.legs_count = legs_count
        self.has_wings = has_wings
        self.name_class = name_class

    def get_older(self):
        self._age += 1

    def get_age(self):
        return self._age

    def __str__(self):
        name = self.name_class
        return name.lower()

    def __new__(cls, *args, **kwargs):
        item = super().__new__(cls)
        cls._all.append(item)
        return item

    @staticmethod
    def add_year():
        for i in Animal._all:
            i.get_older()


class Pet(Animal):
    def __init__(self, *args, name=None, name_class=__qualname__, **kwargs):
        if name is None:
            raise ValueError('Pet should have a name')
        super().__init__(*args, **kwargs)
        self.name = name
        self.name_class = name_class


class Bird(Animal):
    def __init__(self, *args, name_class=__qualname__, **kwargs):
        super().__init__(*args, **kwargs)
        self.legs_count = 2
        self.has_wings = 2
        self.name_class = name_class


class Cat(Pet):

    def __init__(self, *args, name_class=__qualname__, **kwargs):
        super().__init__(*args, **kwargs)
        self.legs_count = 4
        self.name_class = name_class


class Dog(Pet):
    def __init__(self, *args, name_class=__qualname__, **kwargs):
        super().__init__(*args, **kwargs)
        self.legs_count = 4
        self.name_class = name_class


class Parrot(Pet, Bird):
    def __init__(self, *args, name_class=__qualname__, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_class = name_class


class Duck(Bird):
    def __init__(self, *args, name_class=__qualname__, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_class = name_class


def FindAllSubclasses(classType):
    import sys, inspect
    subclasses = []
    callers_module = sys._getframe(1).f_globals['__name__']
    classes = inspect.getmembers(sys.modules[callers_module], inspect.isclass)
    for name, obj in classes:
        if (obj is not classType) and (classType in inspect.getmro(obj)):
            subclasses.append((obj, name))
    return subclasses


class AnimalMeta(metaclass=Animal):
    Animal._classes = FindAllSubclasses(Animal)


print(Animal._classes)
