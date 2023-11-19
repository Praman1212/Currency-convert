from forex_python.converter import CurrencyRates


def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()

    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount
    except:
        return "Invalid currency code(s). Please check and try again."


if __name__ == "__main__":
    print("Currency Converter")

    amount = float(input("Enter the amount: "))
    from_currency = input(
        "Enter the source currency code (e.g., USD): ").upper()
    to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

    result = convert_currency(amount, from_currency, to_currency)

    if isinstance(result, float):
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
    else:
        print(result)
