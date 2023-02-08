class Carrinho:
    def __init__(self) -> None:
        self.__produtos = []
    
    @property
    def produtos(self):
        for i in self.__produtos:
            print(i[0], i[1])
    
    def listar(self):
        for i in self.__produtos:
            print(i[0], i[1])
    
    def inserir(self, produto):
        self.__produtos.append(produto)

    def soma(self):
        total = 0
        for i in self.__produtos:
            total += i[1]
        return total
    
class Produto:
    def __init__(self, nome, valor) -> None:
        self.__nome = nome
        self.__valor = valor
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def valor(self):
        return self.__valor

