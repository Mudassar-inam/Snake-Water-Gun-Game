"""
Snake Water Gun Game
A simple command-line game similar to Rock-Paper-Scissors

Game Rules:
- Snake drinks Water (Snake wins)
- Water rusts Gun (Water wins)
- Gun shoots Snake (Gun wins)

snake = 1
water = -1
gun = 0
"""

import random

def play_game():
    """Main game function"""
    # Computer makes random choice
    computer = random.choice([1, 0, -1])
    
    # Get user input
    youstring = input("Enter your choice, s = snake, w = water, g = gun: ").lower()
    
    # Dictionary mappings
    youdic = {"s": 1, "w": -1, "g": 0}
    reversdic = {1: "Snake", -1: "Water", 0: "Gun"}
    
    # Validate input
    if youstring not in youdic:
        print("Invalid input! Please enter 's', 'w', or 'g'")
        return
    
    you = youdic[youstring]
    
    # Display choices
    print(f"\nYou chose: {reversdic[you]}")
    print(f"Computer chose: {reversdic[computer]}")
    print("-" * 30)
    
    # Determine winner
    if computer == you:
        print("It's a Draw! 🤝")
    else:
        if (computer == 1 and you == -1):
            print("You lose! 😢 Snake drinks Water")
        elif (computer == 1 and you == 0):
            print("You Win! 🎉 Gun shoots Snake")
        elif (computer == -1 and you == 0):
            print("You lose! 😢 Water rusts Gun")
        elif (computer == -1 and you == 1):
            print("You Win! 🎉 Snake drinks Water")
        elif (computer == 0 and you == 1):
            print("You lose! 😢 Gun shoots Snake")
        elif (computer == 0 and you == -1):
            print("You Win! 🎉 Water rusts Gun")
        else:
            print("Something went wrong!")

def main():
    """Main function to run the game"""
    print("=" * 40)
    print("🎮 Welcome to Snake Water Gun Game! 🎮")
    print("=" * 40)
    print("Rules:")
    print("🐍 Snake drinks Water")
    print("💧 Water rusts Gun")
    print("🔫 Gun shoots Snake")
    print("=" * 40)
    
    while True:
        play_game()
        
        # Ask if player wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye! 👋")
            break
        print("\n" + "=" * 40)

if __name__ == "__main__":
    main()
