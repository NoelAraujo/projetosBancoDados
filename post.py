import requests

# URL da rota para criar uma nova carona
url = "http://127.0.0.1:8000/caronas/"

# Dados da carona a ser criada
carona_data = {
    "nome": "João",
    "cidade_partida": "São Paulo",
    "cidade_chegada": "Rio de Janeiro",
    "banda": "Metallica",
    "data": "2024-07-01"
}

# Enviando solicitação POST com os dados da carona
response = requests.post(url, json=carona_data)

# Exibindo resposta do servidor
print(response.json())
