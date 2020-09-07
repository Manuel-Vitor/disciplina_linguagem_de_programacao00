class TimeFutebol():
    def __init__(self, nome, cor, estadio):
        self.nome = nome
        self.cor = cor
        self.estadio = estadio
    
    def jogar_atacando(self):
        print("O time {} esta jogando ATACANDO.".format(self.nome))

    def jogar_defendendo(self):
        print("O time {} esta jogando DEFENSIVAMENTE.".format(self.nome))