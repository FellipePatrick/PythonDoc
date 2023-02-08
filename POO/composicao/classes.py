class Cliente:
    def __init__(self, nome, idade) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__endereco = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    def inseri_endereco(self, cidade, estado):
        self.__endereco.append(Endereco(cidade, estado))
    

    def listar_endereco(self):
        for  i in self.__endereco:
            print(i.cidade, '-', i.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')


    
class Endereco:
    def __init__(self, cidade, estado) -> None:
        self.cidade = cidade
        self.estado = estado
    
    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')

