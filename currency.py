""" Importing request """
import requests
""" Importing Tkinter """
import tkinter

class Currency:
    def __init__(self, url):
        """ Init method """

        # Getting the API data to a JSON format
        data = requests.get(url).json()

        # The actual rates
        self.rates = data["rates"]
    
    def convert(self, from_c, to_c, amount):
        """ Converts the ammount based on the rates """
        init_amount = amount

        # If the currency is not euro, then we convert it
        if from_c != "EUR":
            amount /= self.rates[from_c]
        
        # Applying the actual rate
        amount.round(amount * self.rates[to_c])
