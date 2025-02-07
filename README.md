# WSAA-coursework
Web Services and Applications 

Assignment 2

Deck of Cards API    https://deckofcardsapi.com/

Write a program that "deals" (prints out) 5 cards

first you need to shuffle

https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1

get the deck_id, 

with the deck_id you can get the cards

https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2

This example gets two cards

From there you need to print the value and the suit of each card.

save the file as assignment2-carddraw.py (or as a notebook)
Last few marks:

Check if the user has drawn a pair, triple, straight, or all of the same suit and congratulate the user.