import requests

# Requests a new shuffled deck of cards from API and gets the deck_id from JSON output
shuffle_url = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
shuffled_deck = requests.get(shuffle_url).json()
deck_id = shuffled_deck["deck_id"]

# Draws two cards (count=2) from the deck using the deck_id generated above
draw_card_url = f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2' 
card = requests.get(draw_card_url).json()

card1_value = card["cards"][0]["value"]
card1_suit = card["cards"][0]["suit"]
card2_value = card["cards"][1]["value"]
card2_suit = card["cards"][1]["suit"]

hand = f'Your hand: {card1_value} of {card1_suit} and the {card2_value} of {card2_suit}'

print(hand)
