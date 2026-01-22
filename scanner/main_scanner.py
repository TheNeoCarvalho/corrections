import cv2
from scanner.camera import Camera
from scanner.qr_detector import QRDetector
from core.respostas import Respostas
from core.storage import salvar, carregar

camera = Camera()
detector = QRDetector()
respostas = Respostas()

print("Scanner ativo | Q para sair")

while True:
    estado = carregar()
    respostas.sincronizar_reset(estado.get("reset_id", 0))

    ret, frame = camera.read()
    if not ret:
        break

    deteccoes = detector.detectar(frame)

    for aluno, alternativa in deteccoes:
        if respostas.registrar(aluno, alternativa):
            salvar(respostas.to_dict(respostas.reset_id_atual))
            print(f"{aluno} votou em {alternativa}")

    cv2.imshow("Scanner QR", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
