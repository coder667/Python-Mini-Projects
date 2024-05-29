import random

def roll_dice(num_dice, num_sides):
    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
    return rolls

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        num_dice = int(input("Enter the number of dice to roll: "))
        num_sides = int(input("Enter the number of sides for each die: "))
        
        if num_dice <= 0 or num_sides <= 0:
            print("Please enter valid values for number of dice and sides.")
            continue
        
        rolls = roll_dice(num_dice, num_sides)
        print("Rolling the dice...")
        print("Results:", rolls)
        
        play_again = input("Would you like to roll again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
