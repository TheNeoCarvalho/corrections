class Estatisticas:
    @staticmethod
    def calcular_percentuais(votos):
        total = sum(votos.values())

        if total == 0:
            return {k: 0 for k in votos}

        return {
            k: round((v / total) * 100, 2)
            for k, v in votos.items()
        }
