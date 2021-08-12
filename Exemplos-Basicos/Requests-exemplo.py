import requests

def retorna_cep(cep):
    response = requests.get('https://viacep.com.br/ws/'+cep+'/json/')
    print(response.status_code)
    print(response.text)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])

def pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    dados_pokemon = response.json()
    print(dados_pokemon['name'])
    print(dados_pokemon['sprites']['front_shiny'])

def retorna_response_html(url):
    response = requests.get(url)
    return response.text

# response = retorna_response_html('https://www.google.com.br/')
# print(response)

pokemon = pokemon('pikachu')
