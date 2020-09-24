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