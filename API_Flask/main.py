import requests

link = 'https://d4976654-fd15-4fe5-9ad0-ec92e0c09245-00-38fy0cuiurlft.picard.replit.dev/pegarvendas'

requisição = requests.get(link)

print(requisição)
lista = requisição.json()
print(lista['TV'])