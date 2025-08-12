import random
import string

# Prompt the user for desired password length
length = int(input("Enter the desired password length: "))

# Define possible characters (letters, digits, punctuation)
characters = string.ascii_letters + string.digits + string.punctuation

# Generate a random password
password = ''.join(random.choice(characters) for _ in range(length))

# Display the generated password
print("Generated Password:", password)
