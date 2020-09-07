#Criando a classe principal
class Pessoa():

    def __init__(self, nome, idade, numero_celular):
        self.nome = nome
        self.idade = idade
        self.n_celular = numero_celular

    def vivo(self):
        print("{} está vivo. ".format(self.nome))

    def informar_idade(self):
        print("{} tem {} anos!".format(self.nome, self.idade))
    
    def informar_nome(self):
        print("O nome desta pessoa e {}".format(self.nome))
    
    def informar_numero(self):
        print("O numero para usar de contato e {}".format(self.n_celular))

#Criando outras classes com herança.
class Aluno(Pessoa):

    def __init__(self, nome, idade, celular, estudando_curso, numero_matricula):
        super().__init__(nome, idade, celular)
        self.curso = estudando_curso
        self.n_matricula = numero_matricula
    
    def estudar(self):
        print("O aluno {} está fazendo o curso {}!".format(self.nome, self.curso))

    def numero_matricula(self):
        print("O número da mátricula do aluno {} é {} ".format(self.nome, self.numero_matricula))

class Responsavel(Pessoa):

    def __init__(self, nome, idade, n_celular, responsavel_do_aluno):
        super().__init__(nome, idade, n_celular)
        self.responsavel_do_aluno = responsavel_do_aluno
    
    def responsabilidade(self):
        print("{} é responsavel pelo aluno {}".format(self.nome, self.responsavel_do_aluno))
    
    def informar_responsavel(self):
        print("{} é responsavel por {}".format(self.nome, self.responsavel_do_aluno))

class Professor(Pessoa):

    def __init__(self, nome, idade, n_celular, disciplina):
        super().__init__(nome, idade, n_celular)
        self.disciplina = disciplina

    def periodo_aula(self):
        print("O professor {} esta dando aula no segundo período.".format(self.nome,))

    def disciplina_aplicada(self):
        print("A disciplina que do professor é {}".format(self.disciplina))

class Coordenador(Pessoa):
    
    def __init__(self, nome, idade, n_celular, c_coordenado):
        super().__init__(nome, idade, n_celular)
        self.c_coordenado = c_coordenado
    
    def coordenar_curso(self):
        print("O coordenador {}, coordena o curso de {}".format(self.nome, self.c_coordenado))

class Diretor(Pessoa):

    def __init__(self, nome, idade, n_celular, instituicao):
        super().__init__(nome, idade, n_celular)
        self.instituicao = instituicao
    
    def diretoria_da_instituicao(self):
        print("O diretor {}, faz a direção da instituição {}".format(self.nome, self.instituicao))