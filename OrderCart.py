joe = Customer('John', 0)
ann = Customer('Ann Smith', 1100)

cart = [
    LineItem('Choloate', 4, 1.5),
    LineItem('Beer', 4, 5.5),
    LineItem('Watermelon', 4, 5.5)
]

banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
