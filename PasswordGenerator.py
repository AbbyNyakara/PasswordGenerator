"""
Write a program that generates random passwords from the letters, numbers and symbols given below.
The program should prompt the user to input the number of letters, numbers and symbols they want in their password.
The program should then generate the password every time the program runs
"""
import random
letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
          't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['#', '@', '$', '%', '^', '&', '*', '(', '!']

print("Hello there! Welcome to password generator.")
no_of_letters = int(input("How many letters would you like in your password? "))  #the variable here has to be a number as we will use the range function
no_of_numbers = int(input("How many numbers would you like in your password? "))
no_of_symbols = int(input("How many symbols would you like in your password? "))

#OPTION 1 - The password here will follow the letter, number and symbol sequence in that order.
password =""

for letter in range(1, no_of_letters+1):  #The range function is exclusive of the last number. so we+1
    random_letter = random.choice(letters)
    password = password + random_letter

for number in range(1, no_of_numbers+1):
    random_number = random.choice(numbers)
    password += random_number

for symbol in range(1, no_of_symbols+1):
    random_symbol = random.choice(symbols)
    password += random_symbol

print(password)
#At this point, you can write a function and then convert the string to a list, shuffle and convert back to a string
#OPTION 2

password_list = []

for letter in range(1, no_of_letters+1):
    password_list.append(random.choice(letters))

for number in range(1, no_of_numbers+1):
    password_list.append(random.choice(numbers))

for symbol in range(1, no_of_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

new_password = ''.join(password_list)
print(new_password)

