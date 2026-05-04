# Test variables

first_variable = 25
second_variable = 5

# Basic operations

division = first_variable / second_variable
print(division)

multiplication = first_variable * second_variable
print(multiplication)

addition = first_variable + second_variable
print(addition)

subtraction = first_variable - second_variable
print(subtraction)

square = division ** 2
print(square)


# Concatenating strings

first_name = "Agha Durrez"
last_name = "Khan"
full_name = first_name + " " + last_name

# Using f-string

my_long_string = f"""My name is {full_name}.
I am attempting to learn python for AI.
In my opinion, Python itself is not tricky however, using it for AI is uncharted territory for me"""

print(my_long_string)

# Testing functions on strings

long_dash = "-" * 16

print(len(full_name))
print(len(long_dash))

print(full_name)
print(long_dash)


# Experimenting with conditional statements
is_true = True

age = 24

can_vote = age >= 18

if can_vote == is_true:
    print("They can vote.")

else:
    print("They cannot vote.")

has_firearms_liscense = True

if age >= 25 and has_firearms_liscense:
    print("They may own a firearm.")

else:
    print("They are not allowed to own firearms.")


password = "ghhsu"
if password == input("Enter your password"):
    print("Correct")
else:
    print("wrong")



score = 95

if score <= 20:
    print("F")
elif 20 < score <= 40:
    print("D")
elif 40 < score <= 60:
    print("C")
elif 60 < score <= 80:
    print("B")
elif 80 < score < 90:
    print("A")
elif score >= 90:
    print("A+")
else:
    print("Invalid score")

# Testing for-loop

for i in range(0, 11, 2):
    for k in range(11):
        print(f"{i}, {k}")

i = 1
while i < 6:
  print(i)
  i += 1

# Data structures - lists
my_list = [full_name, age, score, has_firearms_liscense]

print(my_list)

# Slicing

print(my_list[0 : 2])

my_list.append("Hello")
my_list.remove("Hello")

my_list.insert(0,"Hello")

# Data structures - dictionaries

profile = {
    "name": full_name,
    "age": age,
    "score": score
}

profile["score"] = 100
print(profile["score"])

profile["exists"] = True
del profile["exists"]

students = {"Robert": {"age": 23, "score": 37},
            "Jake": {"age": 27, "score": 65},
            "Manny": {"age": 21, "score": 54},
            "Edgar": {"age": 24, "score": 80}
            }

print(students["Edgar"]["age"])


while is_true:
 
 vending_machine = {1: {"name": "Sting", "price": 1},
                    2: {"name": "Pepsi", "price": 2},
                    3: {"name": "Coke", "price": 3},
                    4: {"name": "Cold Cofee", "price": 5}
                    }
 
 money = float(input("Insert money"))
 keys = list(vending_machine.keys())
 for i in range(len(keys)):
     item = vending_machine[keys[i]]
     print(f"{keys[i]} -> {item["name"]} ${item["price"]}")

 choice = int(input("Enter your pick"))
 item = vending_machine[choice]

 if money < item["price"]:
     print("Insufficent money")
     break
 else:
     money = money - item["price"]
     print("Enjoy your " + item["name"])
     

 re_try = input("Would you like to buy anything else? y/N")

 if re_try == "N":
     break
 else:
     print()

# Data structures - tuples

#explicit

tuple_example = ("red", "green", "blue")

#implicit

tuple_example = "red", "green", "blue"

print(tuple_example[0])
print(tuple_example[0 : 2])

# Tuples are immutable which means that any attempt to change them will result in an error

tuple_example[0] = "white"

# Data structures - sets

set_example = {1, 3, 3, 6, 7}

# Duplicates are removed

print(set_example)

# Converting a list into a set (used to remove duplicates)

list_to_set = [1, 3, 5, 2, 5, 1]

list_to_set = set(list_to_set)

print(list_to_set)
