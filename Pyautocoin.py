from bs4 import BeautifulSoup
import requests

availableCoin = ["EUR", "BRL", "CAD", "USD", "TRY", "JPY"]

while True:
    print("==-==-==-==-==-==-==-==-==-==-==-==-==\nINSIRA OS ACRÔNIMOS DA MOEDA VIGENTE:")
    for coin in availableCoin: 
        print(coin)
    actualCoin = str(input("==-==-==-==-==-==-==-==-==-==-==-==-==\n")).upper()

    if actualCoin not in availableCoin:
        print("Insira uma moeda válida!\n")
    else:
        break

while True:
    value = float(input("INSIRA O VALOR QUE DESEJA CONVERTER:\n"))

    if value <= 0:
        print("Insir um valor acima de zero")
    else:
        break

 
while True:
    print("==-==-==-==-==-==-==-==-==-==-==-==-==\nINSIRA OS ACRÔNIMOS DA MOEDA CONVERSORA:")
    for coin in availableCoin: 
        print(coin)
    secondaryCoin = str(input("==-==-==-==-==-==-==-==-==-==-==-==-==\n")).upper()

    if secondaryCoin not in availableCoin:
        print("Insira uma moeda válida!\n")
    else:
        break



url = "https://www.google.com/finance/quote/{}-{}".format(actualCoin, secondaryCoin)
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
links = soup.find_all("div")
price = soup.find('div', class_="YMlKec fxKbKc")


print("Valor convertido: ${:.2f} {}".format(value*(float(price.text)), secondaryCoin.upper()))