class ExtratorArgumentosUrl():
    
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida!")# lançando uma exceção, raise significa que ira jogar alguma coisa para o usuário

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moedaOrigem,moedaDestino = self.extraiAgumentos()
        representacaoString2 = "Valor:" + self.extraiValor() + " " + moedaOrigem + " " + moedaDestino
        representacaoString =  "Valor: {}\n Moeda Origem: {}\n Moeda Destino: {}\n".format(self.extraiValor(), moedaOrigem, moedaDestino)
        return representacaoString
    
    def __eq__(self, outraInstancia):
        return self.url == outraInstancia.url
        
    @staticmethod
    def urlEhValida(url):
        urlByteBank = "https://bytebank.com"
        if url and url.startswith(urlByteBank):#startswith, verifica se a string começa com um caracter especifico
            return True
        else:
            return False

    def extraiAgumentos(self):
        buscaMoedaOrigem ="moedaorigem=".lower()
        buscaMoedaDestino ="moedadestino=".lower()
        

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&") #find é utlizado para procurar se um determina trecho esta de dentro de algo
    
        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
       
        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigin()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find("&")
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
        
        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino = self.url.find("&valor")
        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]
        
        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    def trocaMoedaOrigin(self):
        self.url = self.url.replace("moedadestino", "real",1) #replace procura a palavra informada e substitui por outra palavra que informada, mais a quantiade de substituições que se deseja fazer
        print(self.url)

    def extraiValor(self):
        buscaValor = "valor="
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]

        return valor