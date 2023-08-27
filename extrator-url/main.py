# Fatiamento de strings

# url = "bytebank.com/cambio?moedaDestino=dolarmoedaOrigem=real"
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor do parâmetro
# parametro_busca = 'moedaOrigem'
# indice_parametro = url_parametros.find(parametro_busca)
#
# print(indice_parametro)
#
# indice_valor = indice_parametro + len(parametro_busca) + 1
# valor = url_parametros[indice_valor:]
#
# print(valor)
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)