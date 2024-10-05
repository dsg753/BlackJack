Blackjack Simulator

This program allows you to play a simplified version of Blackjack against a dealer in the console. Starting with an initial balance, you can place bets, play hands, and track your progress with live game statistics.

Features

  Simulated Blackjack Game: Play Blackjack with standard card values and rules.
    Betting System: Place bets for each hand and manage your balance.
    Double Down: Option to double your bet and receive only one additional card.
    Game Statistics: Track the number of wins, losses, ties, and busts for both player and dealer.
    Dynamic Balance Updates: Starting with a balance of $1000, the game adjusts based on wins, losses, and bets.

  Rules of the Game

  Each player is dealt two cards initially.
    The dealer is also dealt two cards, one face-up and one face-down.
    Players can either "Hit" (take an additional card) or "Stand" (keep their current hand).
    Players may choose to "Double Down" immediately after the initial two cards.
    In this case, the player doubles their bet, receives one additional card, and stands automatically.
    If a hand exceeds 21, the player or dealer "busts" (loses automatically).
    After the player finishes, the dealer reveals their hand and hits until reaching a total of 17 or higher.
    The winner is determined based on the closest hand to 21 without busting.

  How to Play

  Betting: Start each round by entering your bet amount. You cannot bet more than your current balance.
    Player Actions:
        Hit: Draw an additional card to try to get closer to 21.
        Stand: End your turn, keeping your current hand value.
        Double Down: Double your bet, take one more card, and automatically end your turn.
    Winning:
        Win by having a hand value closer to 21 than the dealer without exceeding 21.
        If both you and the dealer have the same hand value, it’s a tie.

Requirements

This program requires Python 3.x and the random library, which is pre-installed with Python.
