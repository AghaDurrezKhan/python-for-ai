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

