class Respostas:
    def __init__(self):
        self.reset_id_atual = None
        self.respostas_por_aluno = {}
        self.totais = {"A": 0, "B": 0, "C": 0, "D": 0}

    def sincronizar_reset(self, reset_id):
        if self.reset_id_atual != reset_id:
            self.reset_id_atual = reset_id
            self.respostas_por_aluno = {}
            self.totais = {"A": 0, "B": 0, "C": 0, "D": 0}

    def registrar(self, aluno, alternativa):
        if aluno in self.respostas_por_aluno:
            return False

        if alternativa in self.totais:
            self.respostas_por_aluno[aluno] = alternativa
            self.totais[alternativa] += 1
            return True

        return False

    def to_dict(self, reset_id):
        return {
            "por_aluno": self.respostas_por_aluno,
            "totais": self.totais,
            "reset_id": reset_id
        }
