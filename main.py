from roulette import play_game

def main():
    print("You won the game!" if play_game() else "You lost the game!")

if __name__ == "__main__":
    main()