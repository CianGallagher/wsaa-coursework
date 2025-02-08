import requests

# Requests a new shuffled deck of cards from API and gets the deck_id from JSON output
shuffle_url = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
shuffled_deck = requests.get(shuffle_url).json()
deck_id = shuffled_deck["deck_id"]

# Draws (count=x) cards from the shuffled deck using the deck_id generated above
draw_card_url = f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5' 
card = requests.get(draw_card_url).json()

# Consider replacing this section with a loop, it's cleaner.
card1_value = card["cards"][0]["value"]
card1_suit = card["cards"][0]["suit"]
card2_value = card["cards"][1]["value"]
card2_suit = card["cards"][1]["suit"]
card3_value = card["cards"][0]["value"]
card3_suit = card["cards"][0]["suit"]
card4_value = card["cards"][0]["value"]
card4_suit = card["cards"][0]["suit"]
card5_value = card["cards"][1]["value"]
card5_suit = card["cards"][1]["suit"]

print(f'Card 1: {card1_value} of {card1_suit}')
print(f'Card 2: {card2_value} of {card2_suit}')
print(f'Card 3: {card3_value} of {card3_suit}')
print(f'Card 4: {card4_value} of {card4_suit}')
print(f'Card 5: {card5_value} of {card5_suit}')

# Tell the player their hand next e.g. "You have a pair of 2s" or "You have a straight".