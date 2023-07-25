def main():
    greeting()
    calculate_tip()

def greeting():
    greet_message = print("Welcome to the tip calculator.")
    return greet_message

def calculate_tip():
    while True:
        try:
            bill_total = float(input("What was the total bill? $"))
            break
        except ValueError:
            print("Please enter a valid bill amount.")
    while True:
        try:
            tip_percentage = (float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100)
            break
        except ValueError:
            print("Please enter a valid tip amount.")
    while True:
        try:
            split_count = int(input("How many people to split the bill? "))
            break
        except ValueError:
            print("Please enter a valid number of people to split the bill.")

    tip_total = bill_total * tip_percentage
    total_per_person = (bill_total + tip_total) / split_count

    answer_phrase = print(f"Each person should pay: ${round(total_per_person, 2)}")
    return answer_phrase

main()