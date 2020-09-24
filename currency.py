""" Importing request """
import requests
""" Importing Tkinter """
from tkinter import Entry, Label, OptionMenu, StringVar
import tkinter as tk

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
        amount = round(amount * self.rates[to_c], 2)

class TkinterUI():
    def __init__(self, master, rates):
        self._master = master

        # Entry amount
        self.entry_amount = Entry(master)

        # Listboxes
        key_list = list(rates.keys()) # List of currencies

        from_variable = StringVar(master)
        from_variable.set(key_list[0])
        self.list_from = OptionMenu(master, from_variable, *key_list)

        to_variable = StringVar(master)
        to_variable.set(key_list[0])
        self.list_to = OptionMenu(master, to_variable, *key_list)

        # Label
        self.label = Label(master, text="convert to")

        # Grid display
        self.entry_amount.grid(row=0, column=0, padx=5, pady=5)
        self.list_from.grid(row=0, column=1, pady=5, padx=5)
        self.label.grid(row=0, column=2, padx=5, pady=5)
        self.list_to.grid(row=0, column=3, pady=5, padx=5)

        master.mainloop()                

def main():
    # API Access key
    url = "http://data.fixer.io/api/latest?access_key=864a1bd5385ffa5b3c62b559b5d73aa5&format=1"

    # Currency object
    c = Currency(url)
    
    # Storing the rates
    rates = c.rates

    # Tkinter UI
    root = tk.Tk()
    ui = TkinterUI(root, rates)

if __name__ == "__main__":
    main()
