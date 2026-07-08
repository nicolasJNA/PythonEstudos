#Classes são moldes para a criação d euma instancia

class Person:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname

p1 = Person('Nicolas','Justo')
print(f'{p1.name} {p1.lastname}')