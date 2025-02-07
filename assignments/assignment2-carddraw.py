import requests

shuffle_url = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
shuffled_deck = requests.get(shuffle_url).json()
deck_id = shuffled_deck["deck_id"]

print(shuffled_deck)
print(deck_id)
