import requests

# ID da carona que você deseja atualizar
carona_id = "82aa895e-c6f1-48e3-b428-61fed075d65f"

# URL da rota para atualizar uma carona (substitua {carona_id} pelo ID da carona que deseja atualizar)
url = "http://127.0.0.1:8000/caronas/{carona_id}"

# Novos dados da carona
carona_data = {
    "nome": "Maria",
    "cidade_partida": "São Paulo",
    "cidade_chegada": "Rio de Janeiro",
    "banda": "Metallica",
    "data": "2024-07-01"
}

# Enviando solicitação PUT com o ID da carona e os novos dados
response = requests.put(url.format(carona_id=carona_id), json=carona_data)

# Exibindo resposta do servidor
print(response.json())
