def format_price(price):
    price = int(price)
    price = f'Цена: {price} руб.'
    return price

price_one = format_price(52.64)
print(price_one)
