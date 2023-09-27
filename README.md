# MVP - Aplicação para Obtenção de News

Essa aplicação é utilizada para localizar artigos e manchetes de notícias de atuais

## Pré-requisitos

Para executar este projeto, você precisa ter o Python 3.8 ou superior instalado, além Docker caso seja necessário.

## Como usar

1. Para instalar as dependências, execute o seguinte comando:

```
pip install -r requirements.txt
```

2. Inicie a aplicação:

```
python app.py
```

Acesse a aplicação em seu navegador no endereço http://localhost:6000

3. Rotas:

API Endpoint
GET /get_news

Recupera artigos de "news" com base em uma palavra fornecida.

Request:

http://localhost:6000/get_news?keyword=technology

Response:

{
    "news_titles": [
        "News Title 1",
        "News Title 2",
        "News Title 3"
    ]
}

É possível também utilizar o Docker já que a aplicação foi dockerizada. Para isso será necessário construir e depois executar:

 docker build -t  task-public-api .
 docker run -p 6000:6000 task-public-api `

