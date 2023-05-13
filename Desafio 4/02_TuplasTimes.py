#   Com as tuplas dos 20 primeiros colocados da Liga Juvenil de Futebol Amador,
#   ordenados de acordo com sua colocação, escreva na tela:
#       a) Os 5 primeiros times.
#       b) Os últimos 4 colocados.
#       c) Times em ordem alfabética.
#       d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético', 'Internacional',
         'Atlético-PR', 'Botafogo', 'Goias', 'Corinthians', 'Grêmio',
         'Bahia', 'São Paulo', 'Ceará SC', 'Fortaleza', 'Vasco da Gama',
         'Cruzeiro', 'Fluminense', 'Chapecoence', 'CSA', 'Avaí')

# a)
print(times[0:5])

# b)
print(times[16:20])

# c)
print(sorted(times)) 

# d)
posicao = times.index('Chapecoence') + 1
print('O time da Chapecoence esta na posicao: {}'.format(posicao))