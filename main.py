from ExtratorArgumentosUrl import ExtratorArgumentosUrl

# '''
# argumento = "https://www.butebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"

# subString = argumento[5:11]

# print(subString)
# '''

# # argumento = "moedaorigem=real"

# # listaArgumento = argumento.split("=") #A função split transforma o conteudo da variavel em uma lista excluido oque foi passado como parametro
# # print(listaArgumento)

# url = "pagina?argumentos"
# indice = url.find("?") # A função find() pega o indice o argumento que está sendo passado por parametro
# print(url[indice + 1:])

url = "https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"

argumentosUrl = ExtratorArgumentosUrl(url)

moedaOrigem, moedaDestino = argumentosUrl.extraiAgumentos()
print(moedaDestino, moedaOrigem)

# print(ExtratorArgumentosUrl.urlEhValida(url))

# index = url.find("moedadestino") + len("moedadestino") +1
# substring = url[index:]

# print(substring)

# string = "bytebankbyte"

# print(stringNova)

banco1 = "bytebank".upper()
banco2 = "BYTEBANK".lower()

# print(banco2)