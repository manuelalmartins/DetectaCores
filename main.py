import cv2
import numpy as np
from cores import cores

# Função para identificar a cor com base no HSV
def identificar_cor(hsv):
    for cor, intervalos in cores.items():
        for lower, upper in zip(intervalos[::2], intervalos[1::2]):  # Interpola os pares de limites
            if np.all(lower <= hsv) and np.all(hsv <= upper):
                return cor
    return "Desconhecida"

# Função de callback para capturar o clique do mouse
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Obtém o valor da cor no ponto clicado (BGR)
        bgr = frame[y, x]
        # Converte para o espaço de cor HSV
        hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0]
        
        # Identifica a cor
        cor_detectada = identificar_cor(hsv)

        # Mostra o nome da cor e exibe a cor ao lado
        print(f"Cor detectada no ponto ({x}, {y}): {cor_detectada}")

        # Desenha o nome da cor na tela
        cv2.putText(frame, f"Cor: {cor_detectada}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Desenha um retângulo com a cor ao lado da tela
        color_rect = np.zeros((100, 200, 3), dtype=np.uint8)
        color_rect[:] = bgr
        cv2.imshow("Cor Detectada", color_rect)

# Captura de vídeo da câmera
cap = cv2.VideoCapture(0)  # 0 geralmente é a câmera padrão

# Configura a janela para capturar o clique
cv2.namedWindow("Câmera")
cv2.setMouseCallback("Câmera", mouse_callback)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Falha ao capturar imagem da câmera.")
        break

    # Exibir a imagem com a cor detectada
    cv2.imshow("Câmera", frame)

    # Quando pressionar 'q', encerra a captura
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
