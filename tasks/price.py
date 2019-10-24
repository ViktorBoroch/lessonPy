def format_price(price):
    price = int(price)
    price = f'Цена: {price} руб.'
    return price

price_two = format_price(52.64)
print(price_two)