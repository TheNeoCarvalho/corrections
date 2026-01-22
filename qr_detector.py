# from pyzbar import pyzbar
# import cv2

# class QRDetector:
#     def detectar(self, frame):
#         resultados = []

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         qrcodes = pyzbar.decode(
#             gray,
#             symbols=[pyzbar.ZBarSymbol.QRCODE]
#         )

#         # if qrcodes:
#         #     print(f"QR detectados: {len(qrcodes)}")

#         for qr in qrcodes:
#             raw = qr.data.decode("utf-8").strip()

#             if "|" not in raw:
#                 continue

#             aluno_id, opcao = raw.split("|", 1)
#             opcao = opcao.upper()

#             if opcao not in ["A", "B", "C", "D"]:
#                 continue

#             resultados.append({
#                 "aluno_id": aluno_id,
#                 "opcao": opcao
#             })

#             x, y, w, h = qr.rect
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             cv2.putText(
#                 frame,
#                 f"{aluno_id}:{opcao}",
#                 (x, y - 10),
#                 cv2.FONT_HERSHEY_SIMPLEX,
#                 0.6,
#                 (0, 255, 0),
#                 2
#             )

#         return resultados


import cv2
from pyzbar.pyzbar import decode

class QRDetector:
    def detectar(self, frame):
        resultados = []

        qrcodes = decode(frame)

        for qr in qrcodes:
            try:
                texto = qr.data.decode("utf-8")
                aluno, alternativa = texto.split("|")

                if alternativa in ["A", "B", "C", "D"]:
                    resultados.append((aluno, alternativa))

            except ValueError:
                # QR inválido, ignora
                pass

        return resultados
