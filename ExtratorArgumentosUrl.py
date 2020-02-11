class ExtratorArgumentosUrl():
    
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida!")# lançando uma exceção, raise significa que ira jogar alguma coisa para o usuário


    @staticmethod
    def urlEhValida(url):
        if url:
            return True
        else:
            return False

    def extraiAgumentos(self):
        buscaMoedaOrigem ="moedaorigem=".lower()
        buscaMoedaDestino ="moedadestino=".lower()
        

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")
    
        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
       
        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigin()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find("&")
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
        
        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino = self.en 
        moedaDestino = self.url[indiceInicialMoedaDestino:]
        
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