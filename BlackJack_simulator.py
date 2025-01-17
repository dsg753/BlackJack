import random

# Define constants
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}
SUITS = ['♠', '♥', '♦', '♣']
DECK = [f"{value}{suit}" for value in CARD_VALUES for suit in SUITS]

# Global variables for stats and balance
STATS = {
    "games_played": 0,
    "player_wins": 0,
    "dealer_wins": 0,
    "ties": 0,
    "player_busts": 0,
    "dealer_busts": 0
}
PLAYER_BALANCE = 1000


# Utility Functions
def shuffle_deck():
    """Shuffle and return a fresh deck of cards."""
    deck = DECK[:]
    random.shuffle(deck)
    return deck


def deal_card(deck):
    """Draw a random card from the deck."""
    return deck.pop(random.randrange(len(deck))) if deck else None


def calculate_hand_value(hand):
    """Calculate the total value of a hand and adjust for Aces."""
    value = sum(CARD_VALUES[card[:-1]] for card in hand)
    # Adjust for Aces (Ace can be 11 or 1)
    ace_count = hand.count('A')
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value


def display_hand(name, hand, hide_second_card=False):
    """Display the player's or dealer's hand."""
    if hide_second_card:
        print(f"{name}'s Hand: [{hand[0]}, ?]")
    else:
        hand_value = calculate_hand_value(hand)
        print(f"{name}'s Hand: {hand} (Value: {hand_value})")


def place_bet():
    """Prompt the player to place a bet and validate it."""
    global PLAYER_BALANCE
    while True:
        try:
            bet = int(input(f"Your balance is ${PLAYER_BALANCE}. Enter your bet amount: "))
            if bet <= 0:
                raise ValueError("Bet must be a positive number.")
            if bet > PLAYER_BALANCE:
                print("You can't bet more than your current balance.")
            else:
                return bet
        except ValueError as e:
            print(e)


# Game Functions
def player_turn(deck, hand):
    """Handle the player's turn."""
    while True:
        display_hand("Player", hand)
        action = input("Do you want to [hit] or [stand]? ").lower()
        if action == "hit":
            hand.append(deal_card(deck))
            if calculate_hand_value(hand) > 21:
                return "bust"
        elif action == "stand":
            return "stand"
        else:
            print("Invalid action. Please select [hit] or [stand].")


def dealer_turn(deck, hand):
    """Handle the dealer's turn (must hit on 16 and stay on 17 or above)."""
    while calculate_hand_value(hand) < 17:
        hand.append(deal_card(deck))
    return "bust" if calculate_hand_value(hand) > 21 else "stand"


def determine_winner(player_hand, dealer_hand):
    """Determine the winner of the round."""
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > dealer_value:
        return "player"
    elif player_value < dealer_value:
        return "dealer"
    else:
        return "tie"


def update_stats(result, bet):
    """Update global statistics and player balance."""
    global STATS, PLAYER_BALANCE
    STATS["games_played"] += 1

    if result == "player":
        STATS["player_wins"] += 1
        PLAYER_BALANCE += bet
    elif result == "dealer":
        STATS["dealer_wins"] += 1
        PLAYER_BALANCE -= bet
    elif result == "tie":
        STATS["ties"] += 1


def print_stats():
    """Display game statistics and balance."""
    print("\n--- Game Statistics ---")
    for key, value in STATS.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print(f"Player's Balance: ${PLAYER_BALANCE}")
    print("-----------------------\n")


# Main Game Loop
def play_blackjack():
    global PLAYER_BALANCE

    while PLAYER_BALANCE > 0:
        # Initialize and shuffle deck
        deck = shuffle_deck()

        # Place a bet
        bet = place_bet()

        # Deal initial hands
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]

        # Show initial hands
        display_hand("Player", player_hand)
        display_hand("Dealer", dealer_hand, hide_second_card=True)

        # Player's turn
        if player_turn(deck, player_hand) == "bust":
            print("Player busts! Dealer wins.")
            update_stats(result="dealer", bet=bet)
            print_stats()
            continue

        # Dealer's turn
        display_hand("Dealer", dealer_hand)
        if dealer_turn(deck, dealer_hand) == "bust":
            print("Dealer busts! Player wins.")
            update_stats(result="player", bet=bet)
            print_stats()
            continue

        # Determine winner
        result = determine_winner(player_hand, dealer_hand)
        if result == "player":
            print("Player wins!")
        elif result == "dealer":
            print("Dealer wins!")
        else:
            print("It's a tie!")

        # Update stats and show result
        update_stats(result=result, bet=bet)
        print_stats()

        # Ask if player wants to play again
        play_again = input("Do you want to play another hand? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing! Final balance:", PLAYER_BALANCE)


if __name__ == "__main__":
    play_blackjack()
