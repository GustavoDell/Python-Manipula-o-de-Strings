'''
argumento = "https://www.butebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"

subString = argumento[5:11]

print(subString)
'''

# argumento = "moedaorigem=real"

# listaArgumento = argumento.split("=") #A função split transforma o conteudo da variavel em uma lista excluido oque foi passado como parametro
# print(listaArgumento)

url = "pagina?argumentos"
indice = url.find("?") # A função find() pega o indice o argumento que está sendo passado por parametro
print(url[indice + 1:])