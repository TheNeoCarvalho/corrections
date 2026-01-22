from gerar_qrcodes import GeradorQRCodes

if __name__ == "__main__":
    alunos = [f"ALUNO_{i}" for i in range(1, 31)]

    gerador = GeradorQRCodes()
    gerador.gerar_para_alunos(alunos)
q