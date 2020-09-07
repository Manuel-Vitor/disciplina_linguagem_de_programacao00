from class_pessoa import Pessoa
from class_pessoa import Aluno
from class_pessoa import Professor
from class_pessoa import Responsavel
from class_pessoa import Coordenador
from class_pessoa import Diretor

pessoa = Pessoa("Narukami", 25 , 81925456351 )
pessoa.informar_nome()
pessoa.informar_idade()
pessoa.informar_numero()


aluno = Aluno("Minato", 20, 81921457563, "Biologia", 56351)
aluno.informar_nome()
aluno.informar_idade()
aluno.n_celular
aluno.curso
aluno.numero_matricula

#Profesor quanto a este código acima parei aqui deu o seguinte. 'int' object is not callable. Tentei resolver de tudo quando e jeito porém não consegui, quer dizer até consegui tirando os () porém o código não lia essa parte.

professor = Professor("Shisui", 45, 81925413698, "Segurança de Redes")
professor.informar_nome()
professor.informar_idade()
professor.informar_numero()
professor.disciplina


responsavel = Responsavel("Sarutobi", 37, 81965428742, "Minato")
responsavel.informar_nome()
responsavel.informar_idade()
responsavel.informar_numero()
responsavel.responsavel_do_aluno


coordenador = Coordenador("Tobirama", 39, 81952468712, "Gestão em T.I")
coordenador.informar_nome()
coordenador.informar_idade()
coordenador.informar_numero()
coordenador.coordenar_curso



diretor = Diretor("Hashirama", 45, 81956324175, "Konohagakure")
diretor.informar_nome()
diretor.informar_idade()
diretor.informar_numero()
diretor.diretoria_da_instituicao()