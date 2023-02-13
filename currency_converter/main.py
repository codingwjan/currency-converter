conversion_rates = {
    'USD' : 1.0,
    'EUR' : 0.91,
    'GBP' : 0.76,
    'INR' : 72.97
}

amount = float(input("Enter the amount: "))
from_currency = input("Enter the source currency: ").upper()
to_currency = input("Enter the target currency: ").upper()

initial_amount = amount * conversion_rates[to_currency]
converted_amount = initial_amount / conversion_rates[from_currency]

converted_amount = round(converted_amount, 2)

print(f"{amount} {from_currency} is queal to {converted_amount} {to_currency}")