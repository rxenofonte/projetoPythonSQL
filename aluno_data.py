import pymysql.cursors
from aluno_model import Aluno


class AlunoData:
    # def __init__(self, host, user, pwd, database):
    def __init__(self):
        self.conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='escola',
            port=3306,
            # parametro para retornar os dados como dicionario e nao como tupla
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conexao.cursor()

    def insertAluno(self, aluno: Aluno):
        try:
            sql = "insert into alunos " \
                  "(matricula, nome, idade, curso, nota) values " \
                  "(%s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (aluno.matricula,
                                      aluno.nome,
                                      aluno.idade,
                                      aluno.curso,
                                      aluno.nota))
            self.conexao.commit()
        except Exception as error:
            print(f"Erro ao cadastrar: {error}")

    def updateAluno(self, aluno: Aluno, matricula: str):
        try:
            sql = "update alunos set nome = %s, idade = %s, " \
                  "curso = %s, nota = %s where matricula = %s"
            self.cursor.execute(sql, (aluno.nome,
                                      aluno.idade,
                                      aluno.curso,
                                      aluno.nota,
                                      matricula))
            self.conexao.commit()
        except Exception as error:
            print(f"Erro ao atualizar o aluno: {error}")

    def deleteAluno(self, matricula: str):
        try:
            sql = "delete from alunos where matricula = %s"
            self.cursor.execute(sql, matricula)
            self.conexao.commit()
        except Exception as error:
            print(f"Erro ao apagar o aluno: {error}")

    def selectAlunos(self):
        try:
            sql = "select * from alunos"
            self.cursor.execute(sql)
            alunos = self.cursor.fetchall()
            return alunos
        except Exception as error:
            print(f"Erro ao buscar os alunos: {error}")

# if __name__ == "__main__":
#     db = AlunoData()