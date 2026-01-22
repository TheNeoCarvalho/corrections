# import cv2
# from camera import Camera
# from qr_detector import QRDetector
# from respostas import Respostas
# from estatisticas import Estatisticas

# def main():
#     camera = Camera()
#     detector = QRDetector()
#     respostas = Respostas()

#     print("Q → Finalizar | R → Resetar")

#     while True:
#         ret, frame = camera.read()
#         if not ret:
#             break

#         deteccoes = detector.detectar(frame)
#         respostas.registrar(deteccoes)

#         cv2.imshow("QR Votacao", frame)

#         key = cv2.waitKey(1) & 0xFF

#         if key == ord('r'):
#             respostas.resetar()
#             print("Contagem reiniciada")

#         if key == ord('q'):
#             break

#     camera.release()

#     votos = respostas.obter_votos()
#     percentuais = Estatisticas.calcular_percentuais(votos)

#     print("\nResultado Final:")
#     for k, v in percentuais.items():
#         print(f"{k}: {v}%")

# if __name__ == "__main__":
#     main()


import cv2
from camera import Camera
from qr_detector import QRDetector
from respostas import Respostas
from estatisticas import Estatisticas
from ui import UI

def main():
    camera = Camera()
    detector = QRDetector()
    respostas = Respostas()
    ui = UI()

    print("Q → Finalizar | R → Resetar")

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        # Detecta QR Codes (retorna lista de tuplas: [(aluno, alternativa), ...])
        deteccoes = detector.detectar(frame)

        # Registra votos por aluno (1 voto por aluno)
        respostas.registrar(deteccoes)

        # Atualiza UI no terminal
        ui.atualizar(
            respostas.respostas_por_aluno,
            respostas.totais
        )

        cv2.imshow("QR Votacao", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('r'):
            respostas.resetar()
            print("Contagem reiniciada")

        if key == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

    # Resultado final
    votos = respostas.obter_votos()
    percentuais = Estatisticas.calcular_percentuais(votos)

    print("\nResultado Final:")
    for alternativa, pct in percentuais.items():
        print(f"{alternativa}: {pct}%")

    print("\nRespostas por aluno:")
    for aluno, resposta in respostas.respostas_por_aluno.items():
        print(f"{aluno}: {resposta}")

if __name__ == "__main__":
    main()
