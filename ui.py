# class UI:
#     def atualizar(self, respostas_por_aluno, totais):
#         print("\nRespostas por aluno:")
#         for aluno, resp in respostas_por_aluno.items():
#             print(f"{aluno}: {resp}")

#         print("\nTotais:")
#         for alt, qtd in totais.items():
#             print(f"{alt}: {qtd}")


import os
import time

class UI:
    def atualizar(self, respostas_por_aluno, totais):
        os.system("cls" if os.name == "nt" else "clear")

        print("=== RESULTADOS EM TEMPO REAL ===\n")

        print("Respostas por aluno:")
        for aluno, resp in respostas_por_aluno.items():
            print(f"{aluno}: {resp}")

        print("\nTotais:")
        for alt, qtd in totais.items():
            print(f"{alt}: {qtd}")

        time.sleep(0.2)
