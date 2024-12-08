import cv2
import numpy as np
import json
import os
from sklearn.neighbors import KNeighborsClassifier


def carregar_cores():
    if os.path.exists('cores_treinadas.json'):
        with open('cores_treinadas.json', 'r') as f:
            return json.load(f)
    return {}


def salvar_cores(cores):
    # Converte os valores RGB para tipo int (para garantir que o JSON possa serializar)
    cores_convertidas = {nome: [list(map(int, cor)) for cor in valores] for nome, valores in cores.items()}
    with open('cores_treinadas.json', 'w') as f:
        json.dump(cores_convertidas, f, indent=4)


def treinar_modelo(cores):
    if not cores:
        return None
    X = []
    y = []
    for nome_cor, valores_rgb in cores.items():
        for valor_rgb in valores_rgb:
            X.append(valor_rgb)
            y.append(nome_cor)
    
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X, y)
    return knn

# Função para prever o nome da cor com base no valor RGB
def prever_cor(cor, knn):
    cor = np.array([cor]).reshape(1, -1)  # Reshape para que seja compatível com o modelo
    return knn.predict(cor)[0]

# Função para capturar a cor ao clicar na imagem
def capturar_cor(event, x, y, flags, param):
    global imagem, knn, cores
    if event == cv2.EVENT_LBUTTONDOWN:
        cor_bgr = imagem[y, x]
        cor_rgb = (cor_bgr[2], cor_bgr[1], cor_bgr[0])  # Converte BGR para RGB
        print(f"Cor capturada no clique: R={cor_rgb[0]}, G={cor_rgb[1]}, B={cor_rgb[2]}")
        
        nome_cor = prever_cor(cor_rgb, knn)
        print(f"A cor prevista é: {nome_cor}")

        resposta = input(f"A cor está correta? (s/n): ").strip().lower()
        if resposta == "n":
            nome_cor = input("Qual é o nome da cor? ").strip()
            if nome_cor not in cores:
                cores[nome_cor] = []
            cores[nome_cor].append(cor_rgb)
            salvar_cores(cores)  # Salva no arquivo JSON
            print(f"Cor {nome_cor} salva com o valor RGB: {cor_rgb}")
            knn = treinar_modelo(cores)  # Re-treina o modelo com as novas cores

# Função para iniciar a captura de vídeo
def iniciar_captura():
    global imagem, knn, cores
    cores = carregar_cores()
    knn = treinar_modelo(cores)  # Treina o modelo com as cores carregadas
    
    # Inicia a captura da câmera
    captura = cv2.VideoCapture(0)

    while True:
        ret, imagem = captura.read()
        if not ret:
            print("Erro ao acessar a câmera.")
            break

        # Exibe a imagem ao vivo
        cv2.imshow("Captura de Cores", imagem)

        # Configura a captura do clique do mouse
        cv2.setMouseCallback("Captura de Cores", capturar_cor)

        # Sai do loop ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    captura.release()
    cv2.destroyAllWindows()

# Inicia o programa
if __name__ == "__main__":
    iniciar_captura()
