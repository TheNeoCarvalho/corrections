class Respostas:
    def __init__(self):
        self.votos = {"A": 0, "B": 0, "C": 0, "D": 0}
        self.votantes = set()

    def registrar(self, deteccoes):
        for d in deteccoes:
            aluno_id = d["aluno_id"]

            if aluno_id not in self.votantes:
                self.votos[d["opcao"]] += 1
                self.votantes.add(aluno_id)


    def resetar(self):
        self.votos = {"A": 0, "B": 0, "C": 0, "D": 0}
        self.votantes.clear()

    def obter_votos(self):
        return self.votos
