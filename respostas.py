# class Respostas:
#     def __init__(self):
#         self.votos = {"A": 0, "B": 0, "C": 0, "D": 0}
#         self.votantes = set()

#     def registrar(self, deteccoes):
#         for d in deteccoes:
#             aluno_id = d["aluno_id"]

#             if aluno_id not in self.votantes:
#                 self.votos[d["opcao"]] += 1
#                 self.votantes.add(aluno_id)


#     def resetar(self):
#         self.votos = {"A": 0, "B": 0, "C": 0, "D": 0}
#         self.votantes.clear()

#     def obter_votos(self):
#         return self.votos


class Respostas:
    def __init__(self):
        self.resetar()

    def registrar(self, deteccoes):
        """
        deteccoes: lista de tuplas (aluno_id, alternativa)
        Garante apenas 1 voto por aluno
        """
        for aluno, alternativa in deteccoes:
            if aluno not in self.respostas_por_aluno:
                self.respostas_por_aluno[aluno] = alternativa
                if alternativa in self.totais:
                    self.totais[alternativa] += 1

    def resetar(self):
        self.respostas_por_aluno = {}
        self.totais = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0
        }

    def obter_votos(self):
        return self.totais
