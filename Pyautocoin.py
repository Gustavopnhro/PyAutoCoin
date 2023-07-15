import requests
from bs4 import BeautifulSoup

class Converter:
    #Definindo as moedas disponíveis para conversão
    def __init__(self):
           self.availableCoins = ["EUR", "BRL", "TRY", "JPY", "CAD", "USD"]

    #Pegando os valores
    def actualCoin(self):
        while True:
            print("-="*18)
            print("Opções disponíveis:\n", self.availableCoins)
            print("-="*18)
            actualCoin = str(input("\nINSIRA OS ACRÔNIMOS DA MOEDA:\n")).upper()

            if actualCoin not in self.availableCoins:
                print("\n\nInsira um valor válido!\n\n")
            else:
                return actualCoin

    def value(self):
        while True:
            value = float(input("INSIRA O VALOR QUE DESEJA CONVERTER\n"))

            if value <= 0:
                print("Insira um valor válido!")
            else:
                return value

    def converterCoin(self):
        while True:
            print("-="*18)
            print("Opções disponíveis:\n", self.availableCoins)
            print("-="*18)

            converterCoin = str(input("INSIRA OS ACRÔNIMOS DA MOEDA CONVERSORA:\n")).upper()

            if converterCoin not in self.availableCoins:
                print("\n\nInsira um valor válido!\n\n")
            else:
                return converterCoin

    #Convertendo efetivamente
    def converting(self, actualCoin, value, converterCoin):

        url = "https://www.google.com/finance/quote/{}-{}".format(actualCoin, converterCoin)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        price = soup.find('div', class_="YMlKec fxKbKc")

        print("Valor convertido: ${:.2f} {}".format(value*(float(price.text)), converterCoin) )



converter = Converter()

actualCoin = converter.actualCoin()
value = converter.value()
converterCoin = converter.converterCoin()

converter.converting(actualCoin, value, converterCoin)
    

    
