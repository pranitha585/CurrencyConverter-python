import tkinter as tk
from tkinter import messagebox

# Dictionary to store exchange rates relative to USD
exchange_rates = {
    "USD": 1.0,   # 1 USD is 1 USD
    "EUR": 0.93,  # 1 USD = 0.93 EUR
    "GBP": 0.81,  # 1 USD = 0.81 GBP
    "JPY": 149.62,  # 1 USD = 149.62 JPY
    "INR": 83.12,  # 1 USD = 83.12 INR
    "AUD": 1.47,  # 1 USD = 1.47 AUR
    "CAD": 1.36,  # 1 USD = 1.36 CAD
    "NZD": 1.68,  # 1 USD = 1.68 NZD
    "BRL": 0.17,  # 1 USD = 0.17 BRL
    "BHD": 2.65,  # 1 USD = 2.65 BHD
    "CHF": 0.88,  # 1 USD = 0.88 CHF
    "KYD": 1.20,  # 1 USD = 1.20 KYD
    "JOD": 0.71,  # 1 USD = 0.71 JOD
}

# Saving the conversion history in a text file
history_file = "conversion_history.txt"

# Function to display available currencies
def display_currencies():
    # Returns a list of currency codes available in the dictionary
    return list(exchange_rates.keys())

# Function to convert amount from one currency to another
def convert_currency(amount, base_currency, target_currency):
    # To check if the input currencies are valid
    if base_currency in exchange_rates and target_currency in exchange_rates:
        # Perform conversion using the formula: (amount in base currency) * (rate of target currency) / (rate of base currency)
        converted_amount = amount * exchange_rates[target_currency] / exchange_rates[base_currency]
        return converted_amount
    else:
        # Return an error message if one of the currencies is unsupported
        return "Unsupported currency"

# Function to log the conversion to a file
def log_conversion(amount, base_currency, target_currency, converted_amount):
    # Open the history file in append mode
    with open(history_file, "a") as file:
        # Write the conversion details to the file
        file.write(f"{amount} {base_currency} = {converted_amount} {target_currency}\n")

# Function to display the conversion history from the text file
def display_history():
    try:
        # Try to open the file and read the content
        with open(history_file, "r") as file:
            return file.read()
    except FileNotFoundError:
        # If the file does not exist, return a default message
        return "No conversion history yet."

# Function to handle the convert button click
def on_convert_click():
    try:
        # Get the amount entered by the user and convert it to a float
        amount = float(entry_amount.get())
        # Get the base and target currencies selected by the user
        base_currency = combo_base_currency.get()
        target_currency = combo_target_currency.get()

        # Convert the currency using the conversion function
        converted_amount = convert_currency(amount, base_currency, target_currency)

        # Check if the conversion is successful (converted_amount is a float)
        if isinstance(converted_amount, float):
            # Update result label and log conversion
            result_label.config(text=f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
            # Log the conversion to the history file
            log_conversion(amount, base_currency, target_currency, converted_amount)
        else:
            # Show error message if currency is unsupported
            messagebox.showerror("Error", converted_amount)  
    except ValueError:
        # If the amount entered is not a valid number, show an error message
        messagebox.showerror("Error", "Please enter a valid amount.")

# Function to handle the history button click
def on_history_click():
    # Get the conversion history from the file
    history_text = display_history()
    # Show the history in a messagebox
    messagebox.showinfo("Conversion History", history_text)

# Setting up the GUI window using tkinter
root = tk.Tk()
root.title("Currency Converter") # Set the window title
root.geometry("500x500") # Set the window size

# Label for the title
title_label = tk.Label(root, text="Currency Converter", font=("Arial", 16))
title_label.pack(pady=10)

# Amount Entry
amount_label = tk.Label(root, text="Amount:")
amount_label.pack()
entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

# Base Currency dropdown
base_currency_label = tk.Label(root, text="Base Currency:")
base_currency_label.pack()

# Get the list of available currencies and set the default value to the first currency in the list
base_currency_list = display_currencies()
combo_base_currency = tk.StringVar(root)
combo_base_currency.set(base_currency_list[0])  # Default value
base_currency_menu = tk.OptionMenu(root, combo_base_currency, *base_currency_list)
base_currency_menu.pack(pady=5)

# Target Currency dropdown
target_currency_label = tk.Label(root, text="Target Currency:")
target_currency_label.pack()

combo_target_currency = tk.StringVar(root)
combo_target_currency.set(base_currency_list[1])  # Default value (second currency)
target_currency_menu = tk.OptionMenu(root, combo_target_currency, *base_currency_list)
target_currency_menu.pack(pady=5)

# Convert button that triggers the currency conversion process
convert_button = tk.Button(root, text="Convert", command=on_convert_click)
convert_button.pack(pady=20)

# Label to display the conversion result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# History button to show the conversion history
history_button = tk.Button(root, text="Show Conversion History", command=on_history_click)
history_button.pack(pady=10)

# Start the tkinter event loop
root.mainloop()