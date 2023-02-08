from classes import Carrinho, Produto

carrinho = Carrinho()

p1 = ('Celular', 500)

p2 = ('Fone', 200)

p3 = ('Carregador', 150)


carrinho.inserir(p1)

carrinho.inserir(p2)

carrinho.inserir(p3)

carrinho.listar()

print('O valor final da compra é:',carrinho.soma(),'R$.')