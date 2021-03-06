#card shuffler

import random

listOfCards = ['ace of hearts', 'two of hearts', 'three of hearts', 'four of hearts', 'five of hearts', 'six of hearts', 'seven of hearts',
               'eight of hearts', 'nine of hearts', 'ten of hearts', 'jack of hearts', 'queen of hearts', 'king of hearts', 'ace of clubs',
               'two of clubs', 'three of clubs', 'four of clubs', 'five of clubs', 'six of clubs', 'seven of clubs', 'eight of clubs', 'nine of clubs',
               'ten of clubs', 'jack of clubs', 'queen of clubs', 'king of clubs', 'ace of spades', 'two of spades', 'three of spades', 'four of spades',
               'five of spades', 'six of spades', 'seven of spades', 'eight of spades', 'nine of spades', 'ten of spades', 'jack of spades',
               'queen of spades', 'king of spades', 'ace of diamonds', 'two of diamonds', 'three of diamonds', 'four of diamonds', 'five of diamonds',
               'six of diamonds', 'seven of diamonds', 'eight of diamonds', 'nine of diamonds', 'ten of diamonds', 'jack of diamonds', 'queen of diamonds',
               'king of diamonds']

found = False

def shuffle():
    random.shuffle(listOfCards)
    return listOfCards

def check(deck):
    if len(set(deck))==1:
        found = True
        return "match!"
    else:
        return "not a match"

i = 0
while found == False:
    i+=1
    check(shuffle())
    if i%100000 == 0:
        print("shuffle: "+str(i)+" - not yet found")
