from pyzbar import pyzbar
import cv2

class QRDetector:
    def detectar(self, frame):
        qrcodes = pyzbar.decode(frame)
        resultados = []

        for qr in qrcodes:
            data = qr.data.decode("utf-8").strip()
            aluno_id, opcao = data.split("|")

            opcao = opcao.upper()

            if data in ["A", "B", "C", "D"]:
                resultados.append({
                    "aluno_id": aluno_id,
                    "opcao": opcao,
                    "rect": qr.rect
                })

                x, y, w, h = qr.rect
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(
                    frame, data, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2
                )

        return resultados
