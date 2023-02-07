"""
public, protected, private ==> em outras linguagens de programação

python ==> _ (protected / public com _) ou __(private)
"""

class Dados:
    def __init__(self) -> None:
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}

        else:
            self.__dados['clientes'].update({id:nome})

    def listar(self):
        for id, nome in self.__dados['clientes'].items():
            print('-'*30)
            print(id, nome)
    
    def apagaCliente(self, id):
        del self.__dados['clientes'][id]

bd = Dados()

bd.inserir(1, 'Fellipe')
bd.inserir(2, 'Patrick')

bd.listar()
print(bd.dados)