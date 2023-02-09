class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
    
    def __str__(self) -> str:
        class_str = f'{self.__class__.__name__}' + f'-({self.nome} {self.sobrenome})'
        return class_str

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, o):
        return self.sobrenome == o.sobrenome and self.nome == o.nome
        
if __name__ == '__main__':
    p1 = Pessoa('Fellipe', 'Brito')
    p2 = Pessoa('Fellipe', 'Brito')
    print(p1 == p2)
