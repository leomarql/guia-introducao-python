"""
Para este exercicio, voce tem uma lista de dicionarios. Cada dicionario
tem as seguintes chaves:
 - lat: inteiro representando o valor de latitude
 - lon: inteiro representando o valor de longitude
 - name: nome do local
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Adicione um novo local a lista
# YOUR CODE HERE
waypoints.append({"lat" : int(input()), "lon" : int(input()), "name" : input()})
    
# Modifique o dicionario com nome "a place" para uma longitude
# de valor -130 e mude seu nome para "not a real place"
# YOUR CODE HERE
waypoints[0] = {"lat" : 43, "lon" : -130, "name" : "not a real place"}

# Crie um loop que escreva na tela todos os valores dos dicionarios da lista
# YOUR CODE HERE
for i in range(0, len(waypoints)):
    print(waypoints[i])