class Respostas:
    def __init__(self):
        self.respostas_por_aluno = {}
        self.totais = {"A": 0, "B": 0, "C": 0, "D": 0}

    def registrar(self, aluno, alternativa):
        # BLOQUEIA troca de resposta
        if aluno in self.respostas_por_aluno:
            return False

        if alternativa in self.totais:
            self.respostas_por_aluno[aluno] = alternativa
            self.totais[alternativa] += 1
            return True

        return False

    def to_dict(self):
        return {
            "por_aluno": self.respostas_por_aluno,
            "totais": self.totais
        }
