import random
from colorama import Fore, Style, init

init(autoreset=True)

def play_game():
    choices = ["rock", "paper", "scissors"]
    print(Style.BRIGHT + "🎮 Let's play Rock 🪨, Paper 📄, or Scissors ✂️!\n")

    player_wins = 0
    computer_wins = 0
    count = 0
    icons = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

    while player_wins < 2 and computer_wins < 2:
        player_choice = input("🧍 Choose rock 🪨, paper 📄, or scissors ✂️: ").strip().lower()

        if player_choice not in choices:
            if player_choice in ["quit", "exit"]:
                print(Fore.MAGENTA + "🚪 Goodbye!")
                break
            count += 1
            if count > 5:
                print(Fore.MAGENTA + "😴 Too many mistakes. Please rest and come back when you're ready!")
                break
            print(Fore.YELLOW + "⚠️  Wrong input, please try again")
            continue

        computer_choice = random.choice(choices)
        print(f"💻 Computer chose: {computer_choice} {icons[computer_choice]}")

        if (player_choice == "rock" and computer_choice == "scissors") or \
           (player_choice == "scissors" and computer_choice == "paper") or \
           (player_choice == "paper" and computer_choice == "rock"):
            player_wins += 1
            print(Fore.GREEN + "🎉 You won this round!")
        elif player_choice == computer_choice:
            print(Fore.CYAN + "🤝 It's a tie.")
        else:
            computer_wins += 1
            print(Fore.RED + "😢 Computer won this round.")

        print(f"📊 Current Score - Player: {player_wins}, Computer: {computer_wins}.")

    if player_wins > 0 or computer_wins > 0:
        if player_wins > computer_wins:
            print(Fore.GREEN + "🏆 Congrats, you won the game!")
        else:
            print(Fore.RED + "💀 Computer won the game!")
        print("End of the game!")

if __name__ == "__main__":
    play_game()