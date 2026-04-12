import random
import string

def generate_password():
    print("Password Generator")

    length = int(input("Enter password length: "))

    print("\nChoose options:")
    print("1. Letters only")
    print("2. Letters + Numbers")
    print("3. Letters + Numbers + Special Characters")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        characters = string.ascii_letters
    elif choice == '2':
        characters = string.ascii_letters + string.digits
    elif choice == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice! Using default (Letters only).")
        characters = string.ascii_letters

    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

    # Ask user to generate again
    again = input("\nGenerate another password? (y/n): ")
    if again.lower() == 'y':
        generate_password()
    else:
        print("Done!")

# Run program
generate_password()
