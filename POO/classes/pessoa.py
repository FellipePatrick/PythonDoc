class Pessoa:
    ano = 2202
    def __init__(self, nome, idade, comendo=False, falando=False) -> None:
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def Comer(self):
        if self.falando == True:
            print('A pessoa não pode comer, porque está falando, pare de falar')
            return
        else:
            if self.comendo == True:
                print('A pessoa já está comendo')
                return
            else:
                self.comendo = True
                print('A pessoa está comendo')
                return
    def PararDeComer(self):
        if self.comendo == False:
            print('a pessoa não está comendo, então não pode parar de comer')
            return
        else:
            self.comendo = False
            print('A pessoa não está comendo')
            return

    def Falar(self):
        if self.comendo == True:
            print('A pessoa não pode falar, porque está comendo, pare de comer')
            return
        else:
            self.falando = True
            print('A pessoa está falando')
            return

    def ParaDeFalar(self):
        self.falando = False
        print('A pessoa não está falando')
        return