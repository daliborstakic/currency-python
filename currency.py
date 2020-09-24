""" Importing request """
import requests
""" Importing Tkinter """
from tkinter import Entry, Label, OptionMenu, StringVar, Button, Tk

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
        
        # Returns the amount
        return amount

def button_click(c, app):
    """ On button click """
    try:
        intial_amount = int(app.entry_amount.get()) # Getting the amount
    except ValueError:
        app.final_label.configure(text="Enter the amount!", fg='red')
        app.final_label.grid(row=2, pady=5)
        return

    # Getting the currencies
    from_c = app.from_variable.get()
    to_c = app.to_variable.get()

    # Converting the rate
    amount = c.convert(from_c, to_c, intial_amount)

    # Displaying the amount
    app.final_label.configure(text=f"{intial_amount} {from_c} = {amount} {to_c}", fg='black')
    app.final_label.grid(row=2, padx=5, pady=5)

class TkinterUI():
    def __init__(self, master, c):
        self._master = master

        # Entry amount
        self.entry_amount = Entry(master)

        # Listboxes
        key_list = list(c.rates.keys()) # List of currencies

        self.from_variable = StringVar(master)
        self.from_variable.set(key_list[0])
        self.list_from = OptionMenu(master, self.from_variable, *key_list)

        self.to_variable = StringVar(master)
        self.to_variable.set(key_list[0])
        self.list_to = OptionMenu(master, self.to_variable, *key_list)

        # Label
        self.label = Label(master, text="convert to")
        self.final_label = Label(master)

        # Button
        self.button = Button(master, text="Convert", command=lambda: button_click(c, self))

        # Grid display
        self.entry_amount.grid(row=0, column=0, padx=5, pady=5)
        self.list_from.grid(row=0, column=1, pady=5, padx=5)
        self.label.grid(row=0, column=2, padx=5, pady=5)
        self.list_to.grid(row=0, column=3, pady=5, padx=5)
        self.button.grid(row=1, columnspan=4, padx=5, pady=5)

        master.mainloop()

def main():
    """ Main function """
    # API Access key
    url = "http://data.fixer.io/api/latest?access_key=864a1bd5385ffa5b3c62b559b5d73aa5&format=1"

    # Currency object
    c = Currency(url)

    # Tkinter UI
    root = Tk()
    root.title("Monetary Convertor")
    ui = TkinterUI(root, c)

if __name__ == "__main__":
    main()
