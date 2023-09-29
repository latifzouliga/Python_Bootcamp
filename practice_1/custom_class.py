class Employee:
    def __init__(self, first_name: str = 'Unknown', last_name: str = 'Unknown', job_title: str = 'Unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.first_name == other.first_name and self.last_name == other.last_name


from day_03.abstraction2 import Square

employee1 = Employee('John')
employee2 = Employee('Latif', 'Zouliga', 'Python Developer')
employee3 = Employee('Latif', 'Zouliga', 'Python Developer')

square = Square(3)
print(employee2 == employee3)

print('=========================')
print(square)
print('========== compare ===============')
print(employee2 == square)
print('=========================')

print(employee1.first_name)
print(employee1.last_name)
print(employee2.first_name)
print(employee2.last_name)

print(employee2)

print(bin(1))
