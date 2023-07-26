import random
from ascii_art import ROCK, PAPER, SCISSORS

def main():
    user_choice = choose_user()
    computer_choice = choose_computer()
    print(user_choice)
    print(f"Computer Chose:\n{computer_choice}")
    
    result_message = check_user_result(user_choice, computer_choice)
    print(result_message)

game_choices = [ROCK, PAPER, SCISSORS]

def choose_user():
    while True:
        try:
            user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
            user_choice = game_choices[user_choice]
            return user_choice
        except (ValueError, IndexError):
            print("Invalid input. Please enter 0, 1, or 2.")    

def choose_computer():
    computer_choice = game_choices[random.randint(0,2)]
    return computer_choice

def check_user_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == ROCK and computer_choice == SCISSORS) or \
         (user_choice == PAPER and computer_choice == ROCK) or \
         (user_choice == SCISSORS and computer_choice == PAPER):
        return "You win!"
    else:
        return "You lose!"

if __name__ == "__main__":
    main()