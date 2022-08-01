# Importamos librerias para lecturas
import cv2
import pyqrcode
import png
from pyqrcode import QRCode
from pyzbar.pyzbar import decode
import numpy as np

# Creamos la videocaptura
cap = cv2.VideoCapture(1)

# Empezamos
while True:
    # Leemos los frames
    ret, frame = cap.read()

    # Leemos los codigos QR
    for codes in decode(frame):
        # Extraemos info
        #info = codes.data

        # Decodidficamos
        info = codes.data.decode('utf-8')

        # Tipo de persona LETRA
        tipo = info[0:2]
        tipo = int(tipo)

        # Extraemos coordenadas
        pts = np.array([codes.polygon], np.int32)
        xi, yi = codes.rect.left, codes.rect.top

        # Redimensionamos
        pts = pts.reshape((-1,1,2))

        if tipo == 69:  # J->74 # E->69
            # Dibujamos
            cv2.polylines(frame, [pts], True, (255, 255, 0), 5)
            cv2.putText(frame, 'E0' + str(info[2:]), (xi - 15, yi - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 55, 0), 2)
            print(" El usuario es accionista de la empresa  \n"
                  " Numero de Identificacion: E", str(info[2:]))

        if tipo == 71:  # F->70 # G->71
            # Dibujamos
            cv2.polylines(frame, [pts], True, (255, 0, 255), 5)
            cv2.putText(frame, 'G0' + str(info[2:]), (xi - 15, yi - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
            print(" El usuario pertenece a la seccion ejecutiva \n"
                  " Numero de Identificacion: G", str(info[2:]))

        if tipo == 83:  # C->99 # S->83
            # Dibujamos
            cv2.polylines(frame, [pts], True, (0, 255, 255), 5)
            cv2.putText(frame, 'S0' + str(info[2:]), (xi - 15, yi - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            print(" El usuario pertenece a la seccion salud \n"
                  " Numero de Identificacion: S", str(info[2:]))

        if tipo == 65:  # C->99 # S->83
            # Dibujamos
            cv2.polylines(frame, [pts], True, (0, 255, 255), 5)
            cv2.putText(frame, 'A0' + str(info[2:]), (xi - 15, yi - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            print(" Numero de Identificacion: A", str(info[2:]))
        # Imprimimos
        print(info)

    # Mostramos FPS
    cv2.imshow(" LECTOR DE QR", frame)
    # Leemos teclado
    t = cv2.waitKey(5)
    if t == 27:
        break

cv2.destroyAllWindows()
cap.release()