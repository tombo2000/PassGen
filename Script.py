#This is a script that generates strong passwords by combining uppercase letters, lowercase letters, numbers, and special characters
import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_numbers=True, include_special_chars=True, exclude_similar_chars=True):
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special_chars = "!@#$%^&*()"

    # Combine selected character sets
    char_set = ""
    if include_uppercase:
        char_set += uppercase
    if include_lowercase:
        char_set += lowercase
    if include_numbers:
        char_set += numbers
    if include_special_chars:
        char_set += special_chars

    # Exclude similar characters if requested
    if exclude_similar_chars:
        char_set = char_set.translate(str.maketrans("", "", "iIl1oO0"))

    # Shuffle the characters
    char_list = list(char_set)
    random.shuffle(char_list)

    # Ensure that at least one character from each selected character type is included
    password = ""
    if include_uppercase:
        password += random.choice(uppercase)
    if include_lowercase:
        password += random.choice(lowercase)
    if include_numbers:
        password += random.choice(numbers)
    if include_special_chars:
        password += random.choice(special_chars)

    # Generate the remaining characters
    remaining_length = length - len(password)
    password += "".join(random.sample(char_list, remaining_length))

    # Shuffle the password to further randomize it
    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)

    return password

# User interaction
num_passwords = int(input("Enter the number of passwords to generate: "))
password_length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
exclude_similar_chars = input("Exclude similar characters? (y/n): ").lower() == 'y'

passwords = []
for _ in range(num_passwords):
    password = generate_password(password_length, include_uppercase, include_lowercase, include_numbers, include_special_chars, exclude_similar_chars)
    passwords.append(password)

print("Generated Passwords:")
for password in passwords:
    print(password)