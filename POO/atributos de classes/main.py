class Exemplo:
    variavel = 324
    def __init__(self) -> None:
        self.variavel = 123

p1 = Exemplo()
print(p1.variavel)
print(Exemplo.variavel)