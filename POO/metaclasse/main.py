class NameMetaClass(type):
    def __new__(mcs, name, base, namespace):
        print('new metaclass')
        cls = super().__new__(mcs, name, base, namespace)
        return cls

class Person(metaclass=NameMetaClass):
    def __init__(self, nome, sobrenome) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def sobrenome(self):
        return self.__sobrenome

def init_person(self, nome, sobrenome) -> None:
    self.nome = nome
    self.sobrenome = sobrenome
    
Pessoa = type('Pessoa', (),{
    '__init__':init_person
    })

if __name__ == '__main__':
    p = Person('Fellipe', 'Patrick')
    print(type(Person))
    
    pessoa = Pessoa('José', 'Aruin')
    print(pessoa.nome)