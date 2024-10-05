import random

# Define card values
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Deck of cards (4 suits of each card)
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

# Statistics dictionary to track game progress
game_stats = {
    'games_played': 0,
    'player_wins': 0,
    'dealer_wins': 0,
    'ties': 0,
    'player_busts': 0,
    'dealer_busts': 0
}

# Player's starting balance
player_balance = 1000  # Initial balance of $1000


def deal_card(deck):
    """Draw a random card from the deck."""
    return deck.pop(random.randint(0, len(deck) - 1))


def calculate_hand_value(hand):
    """Calculate the total value of a hand."""
    value = sum([card_values[card] for card in hand])
    # Adjust for aces (Ace can be 1 or 11)
    if value > 21 and 'A' in hand:
        value -= 10
    return value


def show_stats():
    """Print the current game statistics and player balance."""
    print("\n--- Game Statistics ---")
    for key, value in game_stats.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print(f"Player's Balance: ${player_balance}")
    print("-----------------------\n")


def play_game():
    global player_balance
    global deck

    # Reset and shuffle deck
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)

    # Ask player for their bet
    while True:
        try:
            bet = int(input(f"Your balance is ${player_balance}. Enter your bet amount: "))
            if bet > player_balance:
                print("You cannot bet more than your current balance.")
            elif bet <= 0:
                print("Your bet must be a positive amount.")
            else:
                break
        except ValueError:
            print("Invalid bet amount. Please enter a number.")

    # Deal initial cards
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    print(f"Player's hand: {player_hand}, value: {calculate_hand_value(player_hand)}")
    print(f"Dealer's hand: [{dealer_hand[0]}, ?]")

    # Check if the player wants to double down
    doubled_down = False
    if len(player_hand) == 2:
        double_down_choice = input("Do you want to [double down]? (yes/no): ").lower()
        if double_down_choice == 'yes':
            if bet * 2 <= player_balance:
                doubled_down = True
                bet *= 2
                print(f"Doubling down! Your new bet is ${bet}.")
            else:
                print("You don't have enough balance to double down.")

    # Player's turn
    while True:
        if doubled_down:
            # In double down, the player gets exactly one more card and stands automatically.
            player_hand.append(deal_card(deck))
            print(f"Player's hand after double down: {player_hand}, value: {calculate_hand_value(player_hand)}")
            break

        action = input("Do you want to [hit] or [stand]? ").lower()
        if action == 'hit':
            player_hand.append(deal_card(deck))
            player_value = calculate_hand_value(player_hand)
            print(f"Player's hand: {player_hand}, value: {player_value}")
            if player_value > 21:
                print("Player busts!")
                game_stats['player_busts'] += 1
                game_stats['dealer_wins'] += 1
                game_stats['games_played'] += 1
                player_balance -= bet
                show_stats()
                return
        elif action == 'stand':
            break

    # Dealer's turn
    dealer_value = calculate_hand_value(dealer_hand)
    print(f"Dealer's hand: {dealer_hand}, value: {dealer_value}")
    while dealer_value < 17:
        dealer_hand.append(deal_card(deck))
        dealer_value = calculate_hand_value(dealer_hand)
        print(f"Dealer's hand: {dealer_hand}, value: {dealer_value}")
        if dealer_value > 21:
            print("Dealer busts!")
            game_stats['dealer_busts'] += 1
            game_stats['player_wins'] += 1
            game_stats['games_played'] += 1
            player_balance += bet
            show_stats()
            return

    # Compare final hands
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > dealer_value:
        print("Player wins!")
        game_stats['player_wins'] += 1
        player_balance += bet
    elif player_value < dealer_value:
        print("Dealer wins!")
        game_stats['dealer_wins'] += 1
        player_balance -= bet
    else:
        print("It's a tie!")
        game_stats['ties'] += 1

    game_stats['games_played'] += 1
    show_stats()


# Main game loop
while True:
    if player_balance <= 0:
        print("You are out of money! Game over.")
        break

    play_game()

    again = input("Do you want to play another hand? (yes/no): ").lower()
    if again != 'yes':
        break

print("Thanks for playing!")
