
### The Roulette Gamble Simulation

Imagine a simulation involving a person betting on a roulette wheel with a specific strategy. They start with a bankroll of $1,000 and place incremental bets with the aim of building a separate pile of winnings. Each time they win, they add to their separate pile, and each time they lose, they double their bet until they win. The goal is to keep the initial bankroll intact while accumulating additional winnings.

---

### The Strategy: The Martingale Betting System

The player follows a well-known betting strategy called the "Martingale System." Here's how it works:

1. **Starting with $1,000**: The player begins with a bankroll of $1,000.
2. **Betting $1**: They place an initial bet of $1.
3. **Doubling After Each Loss**: If the player loses, they double their next bet, aiming to recover previous losses and gain an additional $1.
4. **Reset on Win**: When a win occurs, they add any surplus winnings to a separate pile and restore the bankroll to the original $1,000.
5. **Repeat**: This process continues with a goal of maximizing the separate winnings pile while keeping the initial bankroll intact.

The simulation ends after a set number of rounds or once a specified winnings target is achieved.

---

### The Risks and Rewards

The Martingale System relies on the notion that consecutive losses will eventually lead to a win, recovering all prior losses. However, it comes with certain risks and benefits:

- **Potential Gains**: When successful, this strategy can steadily increase the winnings pile with minimal impact on the original bankroll.
- **High Risk of Rapid Loss**: The major risk is a prolonged losing streak, which could quickly exhaust the bankroll due to the exponential increase in bet size.

This strategy is particularly effective for the player in scenarios where no table limits are present. However, in real-world roulette tables, limits would typically cap the bet size and restrict the effectiveness of this strategy.

---

### Running the Simulation

To try out the Roulette Gamble Simulation:

1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd roulette-gamble-simulation
   ```
3. Run the simulation with:
   ```bash
   python roulette_simulation.py
   ```

The simulation will display each round's outcome, the current bankroll, and the amount accumulated in the separate winnings pile.

---

### Additional Information

While the Martingale System can appear promising, it is important to consider both the risks and limitations. Although no real-world casino would allow unlimited betting, this simulation provides a fascinating look into the mechanics and potential pitfalls of the strategy.

**Credit**: The Martingale System has been analyzed by many mathematicians and gambling theorists. This simulation serves as an educational tool to illustrate how the system works in a controlled environment.
