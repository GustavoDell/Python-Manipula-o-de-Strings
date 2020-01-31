'''
argumento = "https://www.butebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"

subString = argumento[5:11]

print(subString)
'''

# argumento = "moedaorigem=real"

# listaArgumento = argumento.split("=")
# print(listaArgumento)

url = "pagina?argumentos"
indice = url.find("?")
print(url[indice + 1:])