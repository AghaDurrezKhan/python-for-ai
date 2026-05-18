from datetime import datetime
import pandas as pd

class Product:
    def __init__(self, name, price, stock = 0):
        self.name = name
        self.price = price
        self.stock = stock

    @property
    def price(self):
        return self._price
    
    @property
    def stock(self):
        return self._stock
    
    @price.setter
    def price(self, val):
        if val > 0:
            self._price = val
        else:
            print("Error: Price must be greater than zero")
    
    @stock.setter
    def stock(self, val):
        if val >= 0:
            self._stock = val
        else:
            print("Error: Stock cannot be negative")
            
    def restock(self, amount):
        if amount > 0:
            self.stock += amount
        else:
            print("Error: Restock amount must be greater than 0")

    def __str__(self):
        return f"{self.name} x{self.stock} | ${self.price:,.2f}"
    
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, val):
        if val > 0:
            self._quantity = val
        else:
            raise ValueError("Error: Quantity must be greater than zero")

    @property
    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product} x{self.quantity} | ${self.subtotal:,.2f}"
    
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item.product.stock >= item.quantity:
            self.items.append(item)

    def remove_item(self, name):
        ri = next((item for item in self.items if item.product.name == name), None)
        self.items.remove(ri)

    @property
    def total(self):
        return sum(item.subtotal for item in self.items)
        
    @property
    def item_count(self):
        return len(self.items)
    
    def checkout(self, customer):
        if self.items:
            order = Order(
                customer,
                self.items,
                self.total,
                datetime.now().strftime("%Y-%m-%d")
            )
            for item in self.items:
                item.product.stock -= item.quantity
            self.items = []
            return order

    def __str__(self):
        return f"Cart | Items: {self.item_count} | Total: ${self.total:,.2f}"
    
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = Cart()
        self.order_history = []

    def place_order(self):
        order = self.cart.checkout(self)
        if order:
            self.order_history.append(order)

    def get_order_history(self):
        if self.order_history:
            for order in self.order_history:
                print(order)

    def __str__(self):
        return f"{self.name} | {self.email} | Orders: {len(self.order_history)}"
    
class Order:
    def __init__(self, customer, items, total, date):
        self.customer = customer
        self.items = items
        self.total = total
        self.date = date
    
    def __str__(self):
        return f"Order | {self.customer.name} | ${self.total} | {self.date}"

product1 = Product("iPhone", 200, 8)
product2 = Product("Samsung TV", 500, 2)
product3 = Product("Airpods", 60, 10)
product4 = Product("Macbook", 400, 4)

# cart1.checkout()

print(product1)

customer1 = Customer("John Doe", "johndoe123@email.com")
customer2 = Customer("Jane Smith", "janesmith321@email.com")

customer1.cart.add_item(CartItem(product1, 3))
customer1.cart.add_item(CartItem(product2, 1))

customer2.cart.add_item(CartItem(product3, 4))
customer2.cart.add_item(CartItem(product4, 2))

customer1.cart.add_item(CartItem(product1, 9999))
customer1.cart.add_item(CartItem(product1, -1))

test_product = Product("Test", -10, 1000)
test_product = Product("Test", 1000, -10)

customer1.place_order()
customer2.place_order()

product1.stock

print(customer1)

customer1.get_order_history()
customer2.get_order_history()

products = [product1, product2, product3, product4]

data = []

for product in products:
    data.append({"name": product.name,
                 "price": product.price,
                 "stock": product.stock,
    })

df = pd.DataFrame(data)
df.loc[df["stock"] < 2]

# order1 = Order(customer1)
# print(order1)