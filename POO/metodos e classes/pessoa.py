class Pessoa:
    ano = 2022
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        data = self.ano - self.idade
        print(f'O ano que {self.nome} nasceu foi em {data}')
        


    @classmethod
    def  nascimento(cls, nome, ano_nascimento):
        idade = cls.ano - ano_nascimento
        return cls(nome, idade)

p1 = Pessoa.nascimento('Fellipe', 2003)
print(p1)
print(f'{p1.nome} tem {p1.idade} anos')
p1.ano_nascimento()
