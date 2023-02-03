from random import randint
class Code:
    def __init__(self, nome, userid) -> None:
        self.nome = nome
        self.userid = userid
    @staticmethod
    def gera_id():
        rand = randint(100000, 199999)
        return rand

p1 = Code('Fellipe', Code.gera_id())
print(f'O codigo de {p1.nome} é {p1.userid}')
