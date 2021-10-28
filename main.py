import re

padrao = "\w{5,50}@[a-z]{3,10}.\w{2,3}.\w{2,3}"
texto = "aaaabbbccc rafael213@gmail.com.br sd65a1d65s1 65d1as 6165 1s6d5sa"
resposta = re.search(padrao, texto)
print(resposta.group())