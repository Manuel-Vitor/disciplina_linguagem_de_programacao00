class aviao():
    def __init__(self, modelo, cor, funcao):
        self.modelo = modelo 
        self.funcao = funcao
        self.cor = cor

    def Ligar(self):
        print('O Aviao esta ligando')

    def Desligar(self):
        print('O Aviao esta desligando')