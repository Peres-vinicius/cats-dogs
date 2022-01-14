# cats-dogs
Desenvolvimento de uma arquitetura de rede neural convolucional para a classificação de gatos e cachorros.


## Dados
- Os dados que foram utilizados pertecem ao kaggle.
- Link: https://www.kaggle.com/chetankv/dogs-cats-images
- Foram utilizadas 8000 imagens para treino, sendo 4000 de gatos e 4000 de cachorros. E, para teste, foram usadas 1000 imagens de cada classe.

## Tecnologias
- Python para criação da arquitetura e para o criar API.
- Flask, TensorFlow, Keras e outras libs
- Jupyter notebook, 

## Arquitetura
Para este problema, onde foi utilizado imagens, existe uma arquitetura de rede neural chamado convolucional, onde até então, tem a melhor performance para problemas com imagens.

A rede neural criada tem:
- - 2 camadas convolucionais (Conv2D), sendo de 32 filtros e de tamanho (3,3). Além de ter sido determinado o tamanho da imagem (64, 64) e tendo 3 canais de cores (RGB)
- - 2 camadas de MaxPooling (MaxPooling2D), com tamanho (2, 2)
- - 2 'camadas' de BatchNotmalization, para acelerar os cálculos, pois normaliza os dados
- - 1 camada Flatten

## Api
A api criada está alocada em localHost. Considerações importantes:
- Como está em localHost, é necessário colocar as imagens que queiram ser classificadas na pasta/api/save_img
- Após as imagens estarem lá, é necessário executar o arquivo app.py, com isto, pode-se utilizar softwares para requisição, como o postman. Deve-se passar o nome da imagem utilizando uma requisição POST.

## Observações
- Caso queira mudar a arquitetura, é possível. O arquivo onde está salvo e passível de mudanças, esta em /api/saved_model
- É necessário ficar atento a duas coisas:
- *1* - ficar atento ao caminho onde é feito a preparação dos dados para treinamento e validação. Pois ele faz acesso as imagens baixadas do kaggle.
- *2* - Olhar onde estará salvando o modelo. Deixei em branco para ser alterado com maior facilidade. Dependendo de onde for salvo, lembre-se de alterar na api.
