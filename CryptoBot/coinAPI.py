import requests
import json

class coinSearch():

    def __init__(self):
        self.url = "https://api.coinmarketcap.com/v1/ticker"
        self.coin = ""
        self.name = ""
        self.symbol = ""
        self.rank = ""
        self.price_usd = ""


    #method for starting a cmc api call
    def main(self,query):

        self.coin = query
        self.url += '/' + self.coin + '/'
        request = requests.get(self.url)
        data = request.json()

        self.name = data[0]['name']
        self.symbol = data[0]['symbol']
        self.rank = data[0]['rank']
        self.price_usd = data[0]['price_usd']



      