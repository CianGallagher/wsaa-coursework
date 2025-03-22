import requests

# Requests a new shuffled deck of cards from API and gets the deck_id from JSON output
shuffle_url = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
shuffled_deck = requests.get(shuffle_url).json()
deck_id = shuffled_deck["deck_id"]

# Draws (count=x) cards from the shuffled deck using the deck_id generated above
draw_card_url = f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5' 
drawn_cards = requests.get(draw_card_url).json()["cards"]

hand = []
for card in drawn_cards:
    counter = drawn_cards.index(card) + 1
    value = card["value"]
    suit = card["suit"]
    hand.append((value, suit))
    print(f'Card {counter}: {value} of {suit}')

FACE_CARDS = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

hand_values = [card[0] for card in hand]
hand_suits = [card[1] for card in hand]
# Flush test
# hand_suits = ["CLUBS","CLUBS","CLUBS","CLUBS","CLUBS"]
is_pair = False
is_trips = False


for value in set(hand_values):  
    count = hand_values.count(value)
    if count == 2:
        is_pair = True
        print(f'Congrats, you have a pair of {value}s!')
    elif count == 3:
        is_trips = True
        print(f'Congrats, you have Three of a kind {value}s!')


if len(set(hand_suits)) == 1:
    is_flush = True
    print(f'Congrats, you have a flush!')

# https://stackoverflow.com/questions/36525890/in-python-how-can-you-sort-a-hand-of-poker-list-and-detect-if-it-is-a-straight
    









