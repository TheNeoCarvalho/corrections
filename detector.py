import cv2
import numpy as np

class Detector:
    def __init__(self):
        self.cores = {
            "A": ([0, 0, 0], [180, 255, 30]),
            "B": ([100, 150, 0], [140, 255, 255]),
            "C": ([40, 70, 70], [80, 255, 255]), 
            "D": ([20, 100, 100], [30, 255, 255]), 
        }
        self.threshold_area = 2000

    def Detectar(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        detectadas = []

        for opcao, (lower, upper) in self.cores.items():
            mask = cv2.inRange(
                hsv,
                np.array(lower),
                np.array(upper)
            )

            area = cv2.countNonZero(mask)
            cv2.imshow(f"Mask {opcao}", mask)

            if area > self.threshold_area:
                detectadas.append(opcao)

        return detectadas

    print(pyzbar.decode(frame))