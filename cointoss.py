import random

def coin_toss():
    user_guess = input("Please choose HEADS or TAILS: ").upper()
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
        return True
    else:
        print("You lose")
        return False

def main():
    user_wins = 0
    while True:
        if coin_toss():
            user_wins += 1
        play_again = input("Do you want to play again? Type 'Y' for yes or 'N' for no: ").upper()
        while play_again not in ["Y", "N"]:
            play_again = input("Please type 'Y' for yes or 'N' for no: ").upper()
        if play_again == "N":
            print(f"Thanks for playing. You won {user_wins} times. Goodbye!")
            break

if __name__ == "__main__":
    main()
