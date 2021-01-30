import random
import string
import re

def generate_password(letters_count, digits_count, special_character_count):
    sample_password = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    sample_password += ''.join((random.choice(string.digits) for i in range(digits_count)))
    sample_password += ''.join((random.choice(string.punctuation) for i in range(special_character_count)))
    #then shuffle the sample password
    password_in_list = list(sample_password)
    random.shuffle(password_in_list)
    final_password = ''.join(password_in_list)
    return final_password

def validate(password):
    valid = True
    while valid:
        special_characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if len(password) < 8:
            print("Make sure your password is at least 8 characters")
            password = input("Enter your password: ")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
            password = input("Enter your password: ")
        elif re.search('[a-zA-Z]',password) is None: 
            print("Make sure your password has a letter in it")
            password = input("Enter your password: ")
        elif re.search('[@_!#$%^&*()<>?/\|}{~:]',password) is None:
            print("Make sure your password has a special character in it")
            password = input("Enter your password: ")
        else:
            print("Your password is okay")
            valid = False

print("Password option: \na) Generate password\nb) Create your own password")
choice = input("Press a or b: ")

if choice == 'a':
    i = 0
    minimum = True
    print("Lenght of password must be at least 8 characters")
    num_of_letter = int(input("Number of letter: "))
    num_of_digit = int(input("Number of digit: "))
    num_of_special_character = int(input("Number of special character: "))
    length = num_of_digit + num_of_letter + num_of_special_character
    while minimum:
        if length < 8:
            print("Re-enter")
            num_of_letter = int(input("Number of letter: "))
            num_of_digit = int(input("Number of digit: "))
            num_of_special_character = int(input("Number of special character: "))
            length = num_of_digit + num_of_letter + num_of_special_character
        else:
            print("Password: "+generate_password(num_of_digit, num_of_letter, num_of_special_character))
            print("Password: "+generate_password(num_of_digit, num_of_letter, num_of_special_character))
            print("Password: "+generate_password(num_of_digit, num_of_letter, num_of_special_character))
            minimum = False

else:
    password = input("Enter your password: ")
    validate(password)
    print("Your Password: "+password)
