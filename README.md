# Detecção de Cores com Aprendizado de Máquina

Este projeto utiliza aprendizado de máquina para identificar e classificar cores com base nos valores RGB extraídos de imagens ou cliques em tempo real. O modelo foi treinado para associar cores RGB a nomes de cores específicos, e é capaz de prever o nome de uma cor com base em suas características RGB.

## Tecnologias Utilizadas

- **Python 3.x**
- **OpenCV**: Para captura de imagens e manipulação de cores.
- **Scikit-learn**: Para treinar o modelo de aprendizado de máquina (K-Nearest Neighbors).
- **JSON**: Para armazenar e gerenciar as cores e seus valores RGB.

## Funcionalidades

- **Captura de Cores**: O usuário pode clicar em uma imagem ou capturar uma cor em tempo real de uma webcam.
- **Treinamento do Modelo**: O modelo é treinado com um conjunto de cores e seus respectivos nomes para prever cores desconhecidas.
- **Previsão de Cor**: O modelo prevê o nome da cor baseada no valor RGB capturado.
- **Armazenamento de Cores**: O projeto salva as cores e seus valores RGB em um arquivo JSON para consulta futura. Caso a cor já exista, ela será atualizada com novos valores RGB.

## Como Executar

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina. Além disso, instale as bibliotecas necessárias utilizando o `pip`:
pip install opencv-python scikit-learn

### Passos para Executar
- **Clone este repositório:**
- **git clone https://github.com/manuelalmartins/DetectaCores.git**
- **cd DetectaCores**

### Execute o script main.py:
- python main.py

### O programa irá capturar cores de uma imagem ou da webcam e treinar o modelo para prever a cor com base nos valores RGB. Você pode clicar na imagem para capturar uma cor e fornecer o nome dessa cor.

## Exemplo de Uso
**O modelo irá exibir o nome da cor prevista.**
**Você pode confirmar se a cor está correta.**
*Se a cor não for prevista corretamente, o programa solicitará que você forneça o nome correto da cor.*
### As cores serão salvas em um arquivo cores.json no formato:
json
{
  "vermelho": [
    [255, 0, 0],
    [200, 0, 0]
  ],
  "azul": [
    [0, 0, 255]
  ],
  "cinza": [
    [161, 161, 159]
  ]
}
**Exemplo de Saída**
## Quando uma cor for capturada, você verá a seguinte saída no terminal:

Cor capturada no clique: R=163, G=159, B=155
A cor prevista é: vermelho
A cor está correta? (s/n): n
Qual é o nome da cor? cinza
Salvamento de Cores
Se a cor não foi salva previamente, ela será adicionada ao arquivo cores.json. Caso a cor já tenha sido registrada, o novo valor RGB será adicionado à lista existente para essa cor.