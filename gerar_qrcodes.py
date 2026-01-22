import qrcode
import os

class GeradorQRCodes:
    def __init__(self, pasta_saida="qrcodes"):
        # Caminho absoluto do diretório do projeto (onde está este arquivo)
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Pasta de saída dentro do projeto
        self.pasta_saida = os.path.join(base_dir, pasta_saida)

        # Cria a pasta se não existir
        os.makedirs(self.pasta_saida, exist_ok=True)

    def gerar_para_alunos(self, alunos_ids, opcoes=("A", "B", "C", "D")):
        for aluno_id in alunos_ids:
            for opcao in opcoes:
                conteudo = f"{aluno_id}|{opcao}"

                img = qrcode.make(conteudo)
                nome_arquivo = f"{aluno_id}_{opcao}.png"

                caminho_arquivo = os.path.join(self.pasta_saida, nome_arquivo)
                img.save(caminho_arquivo)

        print(f"QR Codes gerados com sucesso em: {self.pasta_saida}")
