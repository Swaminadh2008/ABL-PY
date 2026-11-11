products = (("Laptop", 50000, 10),
    ("Mobile", 20000, 0),
    ("Tablet", 15000, 5)
)

for name, price, stock in products:
    if stock == 0:
        print(name, "- Out of Stock")
    else:
        print(name, "- In Stock")