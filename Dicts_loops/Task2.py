# Create a function which takes as input two dicts with structure mentioned above, then computes and returns
# the total price of stock.
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
price_ofStock = {key: prices[key] * stock[key] for key in stock}
print(price_ofStock)
