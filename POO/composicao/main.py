from classes import Cliente, Endereco

c1 = Cliente('João', 22)
c1.inseri_endereco('São Pedro', 'RN')
c1.inseri_endereco('São Pedro', 'RJ')
c1.inseri_endereco('Natal', 'RN')
print(c1.nome)
c1.listar_endereco()
print()