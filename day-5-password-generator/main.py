import random
from password_chars import LETTERS, NUMBERS, SYMBOLS

def main():
    print("Welcome to the PyPassword Generator!")
    num_of_letters, num_of_numbers, num_of_symbols = user_choose()
    password = generate_password(num_of_letters, num_of_numbers, num_of_symbols)
    print(f"Here is your password: {password}")

def user_choose():
    while True:
        try:
            num_of_letters = int(input("How many letters would you like in your password?\n")) 
            num_of_symbols = int(input("How many symbols would you like?\n"))
            num_of_numbers = int(input("How many numbers would you like?\n"))
        
            if num_of_letters >= 0 and num_of_symbols >= 0 and num_of_numbers >= 0:
                return num_of_letters, num_of_numbers, num_of_symbols
            else:
                print("Invalid input. Please enter numeric values greater than or equal to 0.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a numeric value greater than or equal to 0.")

def generate_password(num_of_letters, num_of_numbers, num_of_symbols):
    password_character_list = []

    for letter in range(num_of_letters):
        password_character_list.append(LETTERS[(random.randint(0,51))])

    for number in range(num_of_numbers):
        password_character_list.append(NUMBERS[(random.randint(0,9))])

    for symbol in range(num_of_symbols):
        password_character_list.append(SYMBOLS[(random.randint(0,8))])

    random.shuffle(password_character_list)

    password = ''
    for char in password_character_list:
        password += char
    return password

if __name__ == "__main__":
    main()
    