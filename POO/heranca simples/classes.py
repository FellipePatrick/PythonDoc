class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.__nome = nome
        self.__idade = idade
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade

class Cliente(Pessoa):
    def __init__(self, nome, idade, tamanho) -> None:
        super().__init__(nome, idade)
        self.__tamanho = tamanho

    def cabecalho(self):
        print(f'O nome do cliente é {self.nome}, a idade é {self.idade} e o tamanho é {self.tamanho}')
    @property
    def tamanho(self):
        return self.__tamanho

class Aluno(Pessoa):
    def estudar(self):
        print(f'O aluno {self.nome} está estudando')
