import requests
from acesso_cep import BuscaEndereco

cep = 59296470
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

# r = requests.get("https://viacep.com.br/ws/59296470/json/")
# print(type(r.text))

logradouro, bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(logradouro, bairro, cidade, uf)

