# WSAA-coursework
Web Services and Applications 

**Assignment 2**

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


**Assignment 3** 

Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".

Upload this program to the same repository you used for the first assignment
Save this assignment as "assignment03-cso.py"
This program should not be a long one
    I don't need you to reformat or analyse the data in any way
    It should be about 10ish lines long (I have not counted)
You will need to find the dataset in CSO.ie, try economic and then finance, then finance indicators. yes it is difficult to find, that is part of the task, actually the easiest way to find it is search for it.