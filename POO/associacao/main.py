from classes import Escritor, Caneta, Maquina

escritor = Escritor('João')
caneta = Caneta('Bic')
maquina = Maquina()
escritor.ferramenta = caneta
escritor.ferramenta.escrever('papel')