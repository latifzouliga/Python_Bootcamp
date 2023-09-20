class Person:

    def __init__(self, name: str = 'Latif', age: int = 2):
        self.__name = None
        self.__age = None
        self.person_name = name
        self.person_age = age

    @property  # acts as a variable outside the class. this method becomes a variable
    def person_name(self):
        return self.__name

    @person_name.setter
    def person_name(self, name):
        self.__name = name

    @property
    def person_age(self):
        return self.__age

    @person_age.setter
    def person_age(self, age):
        self.__age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


# command + j


person1 = Person()
person1.person_name = 'Daniel'
print(person1.person_name)
print(person1)
