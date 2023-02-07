class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco
        self.precoR = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco*(percentual/100))
        self.percentual = percentual

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, palavra):
        self._nome = palavra.title()

    #GETTER
    @property
    def preco(self):
        return self._preco

    #SETTER
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    def cabecalho(self):
        print(f'O nome do produto é {self.nome}, o preço dele é {self.precoR}R$ e o desconto foi de {self.percentual}%, ficando {self.preco}R$.')


p1 = Produto('Chave', 10)
p1.desconto(50)
p1.cabecalho()

p2 = Produto('notebook', 'R$15')
p2.desconto(10)
p2.cabecalho()