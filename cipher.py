# Pseudocode
# Get input from user
plaintext = input("Enter plaintext (all uppercase letters, no spaces): ")
keyword = input("Enter keyword (all uppercase letters): ")
# Function to convert keyword to numerical values
def key_to_num(keyword):
    return [ord(char) - 65 for char in keyword]
# Function to encrypt plaintext using Vigenère cipher
def encrypt(plaintext, keyword): 
# Convert keyword to numerical values
    key_num = key_to_num(keyword) 
# Convert plaintext to numerical values
plaintext_num = [ord(char) - 65 for char in plaintext]
# Encrypt plaintext
# Generate Vigenère cipher and print result