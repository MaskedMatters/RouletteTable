import random
import time
import helper

class RouletteGame:
    def __init__(self, wallet):
        self.wallet = wallet
        
    # Spin Function: Handles spinning the roulette wheel.
    def spin(self):
        return helper.wheel[random.randint(0, 37)]

    # Validation Function: Checks if bet type is valid.
    def is_valid_bet_type(bet_type):
        valid_colors = ["r", "b"]
        valid_numbers = [str(num) for num in range(37)] + ["00"]
        return bet_type in valid_colors or bet_type in valid_numbers

    # Get Wager Function: Validates the user's wager amount.
    def get_wager(self):
        while True:
            try:
                wager = int(input("Enter your wager amount (1-10000): "))
                if 1 <= wager <= 10000:
                    return wager
                else:
                    print("Wager must be between 1 and 10000.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for the wager.")

    # Get Bet Function: Handles user input for bet type and uses helper functions for validation.
    def get_bet(self):
        while True:
            bet_type = input("Place your bet on a color or number (r/b/#): ").lower()
            if self.is_valid_bet_type(bet_type):
                wager = self.get_wager()
                return {"bet_type": bet_type, "wager": wager}
            else:
                print("Invalid bet type. Please enter 'r', 'b', or a number (0-36, 00).")
                time.sleep(1)
                helper.clear()

    # Determine Outcome Function: Evaluates if the player has won or lost the bet.
    def determine_outcome(self, bet, result):
        bet_type = bet["bet_type"]
        wager = bet["wager"]

        # Win conditions based on color
        if bet_type == "r":
            return wager if result["color"] == "red" else -wager
        elif bet_type == "b":
            return wager if result["color"] == "black" else -wager

        # Win condition based on exact number
        return wager if bet_type == result["number"] else -wager

    # Main Turn Function: Executes one betting turn.
    def turn(self):
        spin_result = self.spin()
        bet = self.get_bet()
        return self.determine_outcome(bet, spin_result)

def play_game():
    # Initiate the Roulette Game
    game = RouletteGame(1000)

    # Play game until you lose all your money or gain double your money.
    while game.wallet < (game.wallet * 2) or game.wallet != 0:
        game.wallet = game.turn()
    
    return True if game.wallet == (game.wallet * 2) else False