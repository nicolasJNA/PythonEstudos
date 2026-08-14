from dataclasses import dataclass

@dataclass
class Person:
    name: str
    lastname: str

    @property
    def full_name(self):
        return f'{self.name} {self.lastname}'
if __name__ == "__main__":
    pessoa1 = Person('nicolas','justo')
    print(pessoa1.full_name)
