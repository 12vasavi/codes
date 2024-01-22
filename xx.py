import random

# Define lists of characters for password generation
letters = ['a', 'b', 'c', ..., 'Z']
numbers = ['0', '1', '2', ..., '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message and user input for password criteria
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level for password generation - password as a string
password = ""

# Generate random letters for the password
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

# Generate random symbols for the password
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

# Generate random numbers for the password
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

# Print the generated password
print(password)

# Hard Level for password generation - password as a shuffled list
password_list = []

# Generate random letters for the password and add them to the list
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Generate random symbols for the password and extend the list
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# Generate random numbers for the password and extend the list
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# Shuffle the password list to mix the characters randomly
random.shuffle(password_list)

# Print the shuffled password list
print(password_list)

# Create the final password by joining the shuffled list elements into a string
password = ""
for char in password_list:
    password += char

# Print the final generated password
print(f"Your password is: {password}")
