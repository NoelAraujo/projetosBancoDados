import requests

# ID da carona que você deseja excluir
carona_id = "82aa895e-c6f1-48e3-b428-61fed075d65f"

# URL da rota para deletar uma carona (substitua {carona_id} pelo ID da carona que deseja excluir)
url = "http://127.0.0.1:8000/caronas/{carona_id}"

# Enviando solicitação DELETE
response = requests.delete(url.format(carona_id=carona_id))

# Exibindo resposta do servidor
print(response.json())
