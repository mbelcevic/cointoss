import random

def coin_toss():
    user_guess = input("Please choose HEADS or TAILS").upper()
    while user_guess not in ["HEADS", "TAILS"]:
            user_guess = input("Please type in 'HEADS' or 'TAILS': ").upper()
            
    result = random.randint(0, 1)
    print("Tossing...")
    print("...")
    if result == 1:
        print("Result is: HEADS")
        result = "HEADS"
    else:
        print("Result is: TAILS")
        result = "TAILS"
        
    if user_guess == result:
        print("You win!")
    else:
        print("You loose")

def main():
    while True:
        coin_toss()
        play_again = input("Do you want to play again? Type 'Y' for yes or 'N' for no: ").upper()
        while play_again not in ["Y", "N"]:
            play_again = input("Please type 'Y' for yes or 'N' for no: ").upper()
        if play_again == "N":
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
