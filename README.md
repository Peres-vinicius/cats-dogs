# cats-dogs
Desenvolvimento de uma arquitetura de rede neural convolucional para a classificação de gatos e cachorros.


## Dados
- Os dados que foram utilizados pertecem ao kaggle.
- Link: https://www.kaggle.com/chetankv/dogs-cats-images
- Foram utilizadas 4000 imagens de gato, 4000 imagens de cachorros para teste. E, para treino, foram usadas 1000 imagens de cada classe.

## Tecnologias
- Python para criação da arquitetura e para o backend
- React (sendo desenvolvido para o frontend)
- Flask, TensorFlow, Keras e outras libs
- Jupyter notebook, 

## Arquitetura
Para este problema, onde foi utilizado imagens, existe uma arquitetura de rede neural chamado convolucional, onde até então, tem a melhor performance para problemas com imagens.

A rede neural criada tem:
- - 2 camadas convolucionais (Conv2D), sendo de 32 filtros e de tamanho (3,3). Além de ter sido determinado o tamanho da imagem (64, 64) e tendo 3 canais de cores (RGB)
- - 2 camadas de MaxPooling (MaxPooling2D), com tamanho (2, 2)
- - 2 'camadas' de BatchNotmalization, para acelerar os cálculos, pois normaliza os dados
- - 1 camada Flatten

