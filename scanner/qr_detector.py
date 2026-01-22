from pyzbar.pyzbar import decode

class QRDetector:
    def detectar(self, frame):
        resultados = []

        for qr in decode(frame):
            try:
                texto = qr.data.decode("utf-8")
                aluno, alternativa = texto.split("|")
                resultados.append((aluno, alternativa))
            except ValueError:
                pass

        return resultados
