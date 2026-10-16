import csv

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show(self):
        print(f"Name: {self.name} | Price: {self.price} | Quantity: {self.quantity}")
        
def read_products(filename):
    products = []
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f, skipinitialspace=True)
        try:
            next(reader) # ข้าม header
        except StopIteration:
            return products # ถ้าไฟล์ว่าง ให้คืนค่าลิสต์เปล่ากลับไป

        for row in reader:
            if len(row) < 3:
                continue
            products.append(Product(row[0], float(row[1]), int(row[2])))
    return products


def show_max_quantity_value(products):
    if not products:
        print("No products found.")
        return
    p = max(products, key=lambda x: x.quantity)
    p.show()
    print(f"Total value: {p.price * p.quantity}")


products = read_products("products.txt")
show_max_quantity_value(products)