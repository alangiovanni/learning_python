import requests

# Faz uma chamada a API e armazena a resposta
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status Code: ", r.status_code)

# Armazena a resposta da API
response_dict = r.json()

# Processa o resultado
print(response_dict.keys())
