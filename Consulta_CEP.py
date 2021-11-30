import requests
print('-=' * 20)
print('          CONSULTA CEP')
print('-=' * 20)
cep = input('Digite o CEP: ')
if len(cep) != 8:
    print('CEP inválido. Digite novamente.')
    cep = input('Digite o CEP: ')
requests = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
data = requests.json()
if 'erro' not in data:
    print('<<< CEP encontrado >>>')
    print(f'CEP: {data["cep"]}')
    print(f'Logradouro: {data["logradouro"]}')
    print(f'Complemento: {data["complemento"]}')
    print(f'Bairro: {data["bairro"]}')
    print(f'Cidade: {data["localidade"]}')
    print(f'Estado: {data["uf"]}')
else:
    print(f'{cep} - CEP inválido.')
    cep = input('Digite o CEP: ')
while True:
    resp = str(input('Quer consultar um novo CEP: [S/N] '))
    if resp in 'Nn':
        break
print('     <<< VOLTE SEMPRE >>>')
