stock = [
    {'name': 'iPhone XS Plus', 'stock': 24, 'price': 65432.2, 'recommended': ['Samsung Galaxy S10', 'iPhone XS']},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5}
]

print(type(stock))
print(stock[0]['recommended'][1])