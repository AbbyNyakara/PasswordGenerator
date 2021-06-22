#THIS IS AN IMPROVED CODE OF THE ORIGINAL PYTHON CODE

import random
import string

letters = string.ascii_letters
character = string.punctuation
numbers = string.digits

print("Hello there! Welcome to password generator.")
no_of_letters = int(input("How many letters would you like in your password? "))
no_of_numbers = int(input("How many numbers would you like in your password? "))
no_of_symbols = int(input("How many symbols would you like in your password? "))

password = ""
for letter in range (no_of_letters):
    random_letter = random.choice(letters)
    password += random_letter

#debugging code~
# print(type(random_letter))

for num in range(no_of_numbers):
    random_number = random.choice(numbers)
    password += random_number

for char in range(no_of_symbols):
    random_symbol = random.choice(character)
    password += random_symbol

password = random.sample(password, len(password))
#print(type(password))
final_password = ''.join(password)
print(final_password)
#We need to shuffle the password in order that they dont appear in any specific order.
#The .shuffle() fuction doesnt work on strings. We will convert the password to a list, shuffle and then back to a str

