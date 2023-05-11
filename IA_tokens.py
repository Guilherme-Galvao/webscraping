

import requests
from bs4 import BeautifulSoup
import time


# URL da página com os dados dos projetos de blockchain
url = "https://www.coingecko.com/pt/categories/artificial-intelligence"

# Lista com os nomes dos 9 projetos relacionados a IA
projetos = ["Fetch.ai", "SingularityNET", "Neuromation", "Cortex", "Endor Protocol", "DeepBrain Chain", "Neurala", "Neurotoken", "Datum"]

# Faz a requisição HTTP para a página
response = requests.get(url)

# Cria um objeto BeautifulSoup com o conteúdo HTML da página
soup = BeautifulSoup(response.content, "html.parser")

# Encontra a tabela com os dados dos projetos de blockchain
table = soup.find("table", {"class=":"sort table mb-0 text-sm text-lg-normal table-scrollable"})
print(table)

'''# Inicializa as listas que irão armazenar os dados dos projetos de blockchain
nomes = []
valores = []
oscilacoes = []
time.sleep(2)
# Encontra todas as linhas da tabela (exceto o cabeçalho)
rows = table.find_all("tr")[1:]

# Itera sobre todas as linhas da tabela e extrai os dados dos projetos relacionados a IA
for row in rows:
    columns = row.find_all("td")
    nome = columns[1].find("a").get_text().strip()
    if nome in projetos:
        valor = columns[7].find("span").get_text().strip()
        oscilacao = columns[8].find("span").get_text().strip()
        nomes.append(nome)
        valores.append(valor)
        oscilacoes.append(oscilacao)

# Imprime os resultados
for i in range(len(nomes)):
    print(f"Nome: {nomes[i]}")
    print(f"Valor: {valores[i]}")
    print(f"Oscilação: {oscilacoes[i]}")
    print()


'''