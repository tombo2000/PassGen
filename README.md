# PassGen - Password Generator
Description
This script generates a specified number of passwords with a specified length, using a combination of uppercase letters, lowercase letters, numbers, and special characters. The user can choose to include or exclude each of these character types, as well as exclude similar characters (e.g. 'i' and 'I', '1' and 'l', etc.).

Usage
Run the script in a Python environment.
Enter the number of passwords to generate.
Enter the desired password length.
Answer the prompts to include or exclude each character type (uppercase, lowercase, numbers, special characters).
Answer the prompt to exclude similar characters.
The script will generate the specified number of passwords and print them to the console.

Script Options
num_passwords: The number of passwords to generate.
password_length: The desired length of each password.
include_uppercase: Whether to include uppercase letters (default: True).
include_lowercase: Whether to include lowercase letters (default: True).
include_numbers: Whether to include numbers (default: True).
include_special_chars: Whether to include special characters (default: True).
exclude_similar_chars: Whether to exclude similar characters (default: True).

Example Output
Enter the number of passwords to generate: 5
Enter the desired password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y
Exclude similar characters? (y/n): y
Generated Passwords:
F4s$eJ#8dL3aP
G2r$eH#9kM1b
P3o$eN#1lI2c
L9a$eK#4mJ8d
E1c$eF#6gH3b

License
This script is licensed under the MIT License. See the LICENSE file for details.
