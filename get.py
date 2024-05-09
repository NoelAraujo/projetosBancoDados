import requests

# URL da rota para buscar caronas
url = "http://127.0.0.1:8000/buscar_caronas/"

# Parâmetros de consulta para a busca
params = {
    "cidade_partida": "São Paulo",
    "banda": "Metallica",
    "data": "2024-07-01"
}

# Enviando solicitação GET com os parâmetros de consulta
response = requests.get(url, params=params)


# url = "http://127.0.0.1:8000/caronas/"
# response = requests.get(url)


# Exibindo resposta do servidor
print(response.json())
