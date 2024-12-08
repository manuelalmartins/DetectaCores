# cores.py

import numpy as np

# Definir os intervalos de cores em HSV com mais tons de cada cor
cores = {
    "vermelho": [
        (0, 120, 70), (10, 255, 255),  # Vermelho mais claro
        (170, 120, 70), (180, 255, 255),  # Vermelho mais escuro
        (10, 255, 150), (15, 255, 255),  # Vermelho mais suave
        (160, 100, 100), (180, 255, 255),  # Tom de vermelho mais apagado
        (0, 255, 255), (10, 255, 255),  # Vermelho intenso
        (0, 255, 100), (5, 255, 255),  # Vermelho forte
        (0, 255, 50), (10, 255, 255),  # Vermelho claro
    ],
    "azul": [
        (100, 150, 0), (140, 255, 255),  # Azul normal
        (110, 255, 150), (120, 255, 255),  # Azul mais claro
        (130, 255, 255), (135, 255, 255),  # Azul mais forte
        (90, 255, 255), (110, 255, 255),  # Azul escuro
        (100, 255, 255), (110, 255, 255),  # Azul profundo
        (110, 100, 100), (130, 255, 255),  # Azul mais apagado
        (120, 150, 100), (140, 255, 255),  # Azul esverdeado escuro
        (100, 100, 50), (140, 255, 255),  # Azul mais profundo
    ],
    "verde": [
        (35, 100, 100), (85, 255, 255),  # Verde normal
        (50, 100, 100), (70, 255, 255),  # Verde claro
        (60, 255, 255), (75, 255, 255),  # Verde mais suave
        (80, 100, 100), (100, 255, 255),  # Verde intenso
        (65, 255, 255), (80, 255, 255),  # Verde mais vivo
        (50, 150, 100), (85, 255, 255),  # Verde escuro
        (40, 100, 100), (60, 255, 255),  # Verde escuro mais saturado
        (80, 100, 100), (110, 255, 255),  # Verde musgo escuro
        (70, 100, 50), (100, 255, 255),  # Verde bem escuro
    ],
    "amarelo": [
        (20, 100, 100), (30, 255, 255),  # Amarelo normal
        (25, 150, 150), (30, 255, 255),  # Amarelo mais suave
        (30, 100, 100), (35, 255, 255),  # Amarelo mais intenso
        (35, 100, 100), (40, 255, 255),  # Amarelo mais vivo
        (25, 255, 255), (30, 255, 255),  # Amarelo bem claro
        (25, 200, 255), (35, 255, 255),  # Amarelo forte
    ],
    "roxo": [
        (130, 50, 50), (150, 255, 255),  # Roxo normal
        (140, 50, 50), (160, 255, 255),  # Roxo mais claro
        (135, 255, 255), (150, 255, 255),  # Roxo mais forte
        (145, 50, 50), (155, 255, 255),  # Roxo mais suave
        (140, 100, 100), (160, 255, 255),  # Roxo mais profundo
        (125, 50, 50), (150, 255, 255),  # Roxo mais escuro
        (140, 100, 100), (160, 255, 255),  # Roxo escuro mais saturado
        (130, 150, 50), (150, 255, 255),  # Roxo mais amarelado
    ],
    "laranja": [
        (10, 100, 100), (25, 255, 255),  # Laranja normal
        (15, 150, 150), (25, 255, 255),  # Laranja mais suave
        (20, 255, 255), (25, 255, 255),  # Laranja mais intenso
        (10, 255, 255), (20, 255, 255),  # Laranja mais forte
        (15, 255, 255), (25, 255, 255),  # Laranja mais vivo
        (5, 255, 255), (15, 255, 255),  # Laranja mais claro
    ],
    "rosa": [
        (150, 50, 50), (170, 255, 255),  # Rosa normal
        (160, 50, 50), (180, 255, 255),  # Rosa mais suave
        (150, 100, 100), (170, 255, 255),  # Rosa mais claro
        (160, 100, 100), (180, 255, 255),  # Rosa mais forte
        (150, 150, 255), (170, 255, 255),  # Rosa mais forte e claro
        (160, 150, 100), (180, 255, 255),  # Rosa mais quente
    ],
    "ciano": [
        (85, 100, 100), (100, 255, 255),  # Ciano normal
        (90, 150, 150), (100, 255, 255),  # Ciano mais claro
        (90, 255, 255), (100, 255, 255),  # Ciano mais forte
        (80, 100, 100), (100, 255, 255),  # Ciano escuro
        (95, 255, 255), (105, 255, 255),  # Ciano mais intenso
        (85, 255, 255), (95, 255, 255),  # Ciano forte
    ],
    "cinza": [
        (0, 0, 50), (180, 50, 200),  # Cinza normal
        (0, 0, 100), (180, 50, 200),  # Cinza claro
        (0, 0, 150), (180, 50, 200),  # Cinza mais forte
        (0, 0, 200), (180, 50, 200),  # Cinza bem claro
        (0, 0, 250), (180, 50, 200),  # Cinza muito claro
    ],
    "preto": [
        (0, 0, 0), (180, 255, 50),  # Preto
        (0, 0, 20), (180, 255, 50),  # Preto mais claro
        (0, 0, 10), (180, 255, 50),  # Preto escuro
    ],
    "branco": [
        (0, 0, 200), (180, 30, 255),  
        (0, 0, 250), (180, 30, 255),  
    ],
}
