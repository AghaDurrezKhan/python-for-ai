# Functions --------------------------------------------------------------------

# Basic functions
def greet():
    print("Hello there!")

greet()

def weather():

    # Input
    temprature = int(input("Enter the temprature: "))

    # Conditionals
    if temprature > 25:
        print("The weather is hot")
    elif temprature < 25:
        print("The weather is cold")
    else:
        print("The weather is normal")

weather()

# Functions with parameters
def print_full_name( first_name, last_name):

    # Concatenation
    full_name = first_name + " " + last_name

    # Output
    print(f"{full_name} is your full name")

print_full_name("Agha Durrez", "Khan")

def exponentiation( first_num, second_num):
    power = first_num ** second_num
    print(f"{power} is the answer")

exponentiation(5, 4)

def calculate_total(price, tax_rate, discount):

    # Calculation
    tax = price * tax_rate
    total_price = price + tax - discount

    # Return used to store output
    return total_price

total = calculate_total(60, 0.06, 10)

def geometry_calculator(breadth, width):

    area = breadth * width
    perimeter = 2 * breadth + 2 * width
    
    # Returning multiple values
    return area, perimeter

area, perimeter = geometry_calculator(4, 2)

# Importing built-in modules ----------------------------------------------------------

# Math
import math
print(math.sqrt(25))

# Random
import random
random_int = random.randint(1, 10)
random_str = random.choices(["Red", "Green", "Blue"])

# Datetime
import datetime
today = datetime.date.today()
print(today)

# Importing specific functions from a module
from math import sqrt, pi
print(sqrt(25))

# Importing with alias
import pandas as pd

# Working with APIs -------------------------------------------------------------------
import requests

latitude = 25.3753
longitude = 68.3651

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

#Response from website
response = requests.get(url)

# Converting reponse into Python object
data = response.json()

print(data)

temprature = data["current"]["temperature_2m"]

# Creating a get_temp function
def get_temp(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

    response = requests.get(url)
    data = response.json()
    temprature = data["current"]["temperature_2m"]

    return temprature


hyderabad_temp = get_temp(25.3753, 68.3651)
leeds_temp = get_temp(53.80, -1.55)
antalya_temp = get_temp(36.8864, 30.7105)

print(f"Hyderabad: {hyderabad_temp}°C")
print(f"Leeds: {leeds_temp}°C")
print(f"Antalya: {antalya_temp}°C")

# Working with files --------------------------------------------

import os

# Fetches curent working directory
os.getcwd()

# Storing the contents of files
with open("data/hyderabad_weather.csv", "r") as file:
    content = file.read()

print(content)

# Python handles regular files and modules differently
import sys

# Locations Python looks for modules in:
print(sys.path)

# Importing a module - Python searches for it
#import mymodule                    - Looks for mymodule.py
#from folder.utils import helper    - Looks for folder/utils.py


# How to dd a folder to Python's search path:
sys.path.append("/path/to/my/folder")

# How to import from a parent folder
parent = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent)

# Error handling ----------------------------------------------------------

# Try / Except example

try:
    with open("eggs.txt", "r") as r:
        content = r.read()
except FileNotFoundError:
    print("Error: File not found")
    
# example 2
try:
    first_num = int(input("Enter an integer: "))
    second_num = int(input("Enter another integer: "))
    if second_num == 0:
        raise ZeroDivisionError
    division = first_num / second_num        # This operation will result in a runtime error
    print(f"Result: {division}")

except ValueError:                                      # Catches the error
    print("Error: Non-integer value(s) entered")

except ZeroDivisionError:                               # Catches the error
    print("Error: Second integer is zero")

finally:                                                # This always runs
    print("Operation Ended")


# Classes in Python -----------------------------------------------------------

class Dog:
    def __init__(self, name, gender, age, breed):
        self.name = name
        self.gender = gender
        self.age = age
        self.breed = breed

dogs = []
dogs = [
    Dog("Duke", "Male", 12, "German Shephard"),
    Dog("Leanne", "Female", 7, "Labrador"),
    Dog("Roman", "Male", 9, "Cane Corso"),
    Dog("Luffy", "Male", 11, "Rotweiler"),
    Dog("Dumdum", "Male", 11, "Great Dane"),
    Dog("Bobo", "Male", 15, "Pitbull")
    ]

df = pd.DataFrame([vars(d) for d in dogs])
df.head()

class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid Email: {email}")

    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")

    def get_errors(self):
        return self.errors


validator = DataValidator()

validator.validate_email("xsgcsui@yahoo.com")
validator.validate_email("xsgcsuiyahoo.com")

validator.validate_age(24)
validator.validate_age(190)

print(validator.get_errors())

# OOP in Python --------------------------------------------------


class Vehicle:
    def __init__(self, make, speed):            # Initialize the class
        self.make = make
        self.__speed = speed
    
    def __str__(self):                              # String function
        return f"{self.make} | {self.speed}mph"
    
    @property                                   # Property method for conervting speed to kmh
    def speed_kmh(self):
        return self.speed * 1.60934
    
    @property                                   # Created a property which is a controlled way to get speed
    def speed(self):
        return self.__speed
    
    @staticmethod                               # Static method within class.Acts as a helper
    def is_fast(mph):
        if mph > 150:
            return True
        else:
            return False
        
    @classmethod                                # Class Method that can be used alternatively to create objects
    def from_kmh(cls, make, speed_kmh):
        speed_mph = speed_kmh / 1.60934
        return cls(make, speed_mph)
    
    @speed.setter                               # Settr method which is a conrolled way to set speed
    def speed(self, value):
        if value < 0:
            print("Speed cannot be negative")
        else:
            self.__speed = value
    
    def move(self):
        print(f"{self.make} is moving at {self.speed}mph")

# Practice

class Car(Vehicle):
    def __init__(self, make, speed, num_doors):
        super().__init__(make, speed)
        self.num_doors = num_doors

    def __str__(self):
        return f"{self.__class__.__name__} | {super().__str__()} | {self.num_doors} doors"
    
    def honk(self):
        print(f"{self.make} is Honking")

    def move(self):
        print(f"{self.make} is driving at {self.speed} with {self.num_doors} doors")

class Motorcycle(Vehicle):
    def __init__(self, make, speed, has_sidecar):
        super().__init__(make, speed)
        self.has_sidecar = has_sidecar

    def __str__(self):
        return f"{self.__class__.__name__} | {super().__str__()} | Has Sidecar: {self.has_sidecar}"
    
    def wheelie(self):
        if self.has_sidecar:
            print(f"Can't perform wheelie because {self.make} has a sidecar")
        else:
            print(f"{self.make} Performed a wheelie")

vehicle = Vehicle("Toyota", 124)
vehicle.move()
vehicle.__str__()

car = Car("Honda", 170, 4)
car.honk()
car.move()
car.__str__()
motorcycle = Motorcycle("Harley-Davidson", 120, False)
motorcycle.wheelie()

vehicles = []

vehicles = [
    Vehicle("Toyota", 124),
    Vehicle("Mercedes", 219),

    Car("Honda", 170, 4),
    Car("Jaguar", 217, 2),

    Motorcycle("Harley-Davidson", 120, False),
    Motorcycle("Ural", 80, True)
]

df = pd.DataFrame([vars(v) for v in vehicles])      # Saved objects to dataframe
print(df.loc[df["num_doors"].notna()])              # Fetches cars

vehicle = Vehicle.from_kmh("Yoyo", 145)
print(vehicle.speed)
print(vehicle.speed_kmh)
vehicle.is_fast(vehicle.speed)
vehicle.speed = 250
vehicle.is_fast(vehicle.speed)

class Book:
    def __init__(self, title, author, isbn, is_available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    @property
    def status(self):
        if self.is_available:
            return "Available"
        else:
            return "Checked Out"
        
    @staticmethod
    def validate_isbn(isbn):
        isbn = isbn.replace("-", "")
        if len(isbn) == 13 and isbn.isdigit():
            return "Valid Isbn"
        else:
            return "Invalid Isbn"
        
    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["isbn"], data["is_available"])


    def __str__(self):
        return f"{self.title} by {self.author} | {self.status}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.max_books = 3
        self.membership = "Regular"

    def borrow_book(self, book):
        if book.status == "Available" and len(self.borrowed_books) != self.max_books:
            self.borrowed_books.append(book)
            book.is_available = False
        elif len(self.borrowed_books) == self.max_books:
            print(f"You have already borrowed {len(self.borrowed_books)} / {self.max_books} books")
        else:
            print("Book not available")

    def return_book(self, book):
        if book.status == "Checked Out":
            self.borrowed_books.remove(book)
            book.is_available = True
        else:
            print("Book not checked out")

    def __str__(self):
        return f"{self.name} | ID: {self.member_id} | {self.membership} | Borrowed Books: {len(self.borrowed_books)}"
    
class PremiumMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.max_books = 10
        self.membership = "Premium"
        


book1 = Book("Pinocchio", "Carlo Collodi", "978-0141331645")
book2 = Book("Diplomacy", "Henry Kissinger", "978-0007350834")
book3 = Book("The Adventures of Sherlock Holmes", "Sir Arthur Conan Doyle", "978-0007350834")
book4 = Book("Napoleon: A Life", "Andrew Roberts", "978-0143127857")
book5 = Book("The Alchemist", "Paulo Coelho", "978-0060879075" )
book6 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "978-1408866191", True )
book7 = Book("The Witness", "Nora Roberts", "978-0515152340", True )
book8 = Book("The Throne of Fire", "Rick Riordan", "978-0786838653", True )
book9 = Book("Animal Farm", "George Orwell", "978-0451526342", True )
book10 = Book("The Cottage", "Danielle Steel", "978-0552148539", True )
book11 = Book("A Brief History of Time", "Stephen Hawking", "978-0553380163", True )


book11.__str__()
book1.status


member1 = Member("George Atkins", "72167")
premium_member1 = PremiumMember("Robert Brown", "83722")

member1.borrow_book(book1)
member1.borrow_book(book2)
member1.borrow_book(book3)
member1.borrow_book(book4)

member1.__str__()

premium_member1.borrow_book(book1)

member1.return_book(book1)
member1.return_book(book2)
member1.return_book(book3)

premium_member1.borrow_book(book1)
premium_member1.borrow_book(book2)
premium_member1.borrow_book(book3)
premium_member1.borrow_book(book4)
premium_member1.borrow_book(book5)
premium_member1.borrow_book(book6)
premium_member1.borrow_book(book7)
premium_member1.borrow_book(book8)
premium_member1.borrow_book(book9)
premium_member1.borrow_book(book10)
premium_member1.borrow_book(book11)

premium_member1.__str__()

books = [
    book1,
    book2,
    book3,
    book4,
    book5,
    book6,
    book7,
    book8,
    book9,
    book10,
    book11
]
        
df = pd.DataFrame([vars(b) for b in books])

print(df.loc[df["is_available"]])

print(Book.validate_isbn("978-0141331645"))
print(Book.validate_isbn("123"))
print(Book.validate_isbn("ABCDEFGHIJKLM")) 

data = {
    "title": "Dune",
    "author": "Frank Herbert",
    "isbn": "978-0441013593",
    "is_available": True
}

book12 = Book.from_dict(data)
print(book12.__str__)


# import pandas as pd
# from datetime import datetime

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.transactions = []

    @property
    def set_balance(self, balance):
        self.balance = balance

    @classmethod
    def from_dict(cls, data):
        account = cls(data["owner"])
        account.balance = data["balance"]
        return account

    @staticmethod
    def validate_deposit(deposit):
        if isinstance(deposit, int):
            if deposit > 0:
                return True
            else:
                return False
        else:
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"{datetime.now()} - Deposited ${amount}")
        else:
            print("Error: Amount Cannot be Negative")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"{datetime.now()} - Withdrew ${amount}")
        else:
            print("Error: Insufficent Balance")

    def get_transactions(self):
        return self.transactions
    
    def __str__(self):
        return f"Owner: {self.owner} | Balance: ${self.balance:,.2f}"
    

class SavingsAccount(BankAccount):
    def __init__(self, owner):
        super().__init__(owner)
        self.interest_rate = 0.05

    def apply_interest(self):
        interest = (self.balance * self.interest_rate)/100
        self.balance += interest
        self.transactions.append(f"{datetime.now()} - Interest of ${interest} applied")

    def __str__(self):
        return f"{super().__str__()} | Rate: {self.interest_rate*100}%"
    
bank_account = BankAccount("George")
savings_account = SavingsAccount("Robert")

bank_account.deposit(5700)
bank_account.withdraw(200)

savings_account.deposit(7000)
savings_account.withdraw(500)

bank_account.withdraw(10000)
bank_account.deposit(-1000)

savings_account.apply_interest()

print(bank_account.get_transactions())
print(savings_account.get_transactions())

data = {
    "owner": savings_account.owner,
    "balance": savings_account.balance,
    "transactions": savings_account.get_transactions(),
    "rate": savings_account.interest_rate*100
}

data2 = {
    "owner": bank_account.owner,
    "balance": bank_account.balance,
    "transactions": bank_account.get_transactions(),
}
df = pd.DataFrame(data, data2)

bank_account.validate_deposit("uishc")



