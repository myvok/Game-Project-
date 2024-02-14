#Final Project - CS112
#KieuMyVo

import random

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.stay = 0
        
    def __str__(self):
        s = self.name + "has the value of" + self.hand + "points" 
        return s

    def update_hand_value(self, card):
        self.hand.append(card)
        
    def displayHand(self):
        print(self.name + "'s cards: ", end='')
        for i in self.hand:
            print(i[0] + "; ", end='')
        print("")

class Card:
    def __init__(self, rank = [2,3,4,5,6,7,8,9,10,'Ace','King','Queen','Jack'],\
                        suit = ['♠','♥','♣','♦']):
        self.ranks = rank
        self.suits = suit
        self.deck = []

    def __str__(self):
        s = self.deck
        return s

    def create_deck(self):
        special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}

        deck = []
        for rank in self.ranks:
            for suit in self.suits:
                key = str(rank) + ' ' + suit

                if type(rank) == int:
                    value = rank
                else:
                    value = special_values[rank]
            
                deck.append([key, value])

        self.deck = deck
        return deck



def instruction(p1,p2):
    print(f"Welcome {p1} and {p2} to BlackJack game!!")
    print("The magic number for Blackjack is 21!")
    print("The values for all the cards dealt to a player are added and if the sum exceeds 21, the player busts and loses instantly.")
    print("Player 2 will be a dealer")
    print("If a player gets an exact 21, the player wins against the dealer.")
    print("Special values: ")
    print("King: 10; Queen: 10; Jack: 10")
    print("Ace is count for 1 if all of your cards' values ")


def deal(deck):
    random.shuffle(deck)
    key, value = deck.pop()
    return(key,value)


def HitOrStay(player, list, deck):

    while True:
        ans = input(f"{player} do you want to HIT or STAY?").lower()
        if ans == "hit":
            list.append(deal(deck))
            print(f"{player}, here's list of your cards: ", list)
        else:
            break

def sumCard(list):
    sum_card = 0
    for i in range(len(list)):
        sum_card += list[i][1]
    return sum_card
    

def dealerHitorStay(player, list, deck):
    while sumCard(list = list) <= 16:
        list.append(deal(deck))
        print(f"{player}, here's list of your cards: ", list)

def main():

    p1 = input("What's player1 name? ")
    p2 = input("What's player2 name? ")

    instruction(p1,p2)

    player1 = Player(name=p1)
    player2 = Player(name=p2)

    #deal 2cards to 2 players
    cards = Card()
    cards.create_deck()

    for i in range(2):
        player1.update_hand_value(card=deal(cards.deck))
        player2.update_hand_value(card=deal(cards.deck))

    player1.displayHand()
    player2.displayHand()

    
    HitOrStay(player = player1.name, list = player1.hand, deck=cards.deck)
    dealerHitorStay(player = player2.name, list = player2.hand, deck=cards.deck)

    #the sum here is your handValue
    sum1 = sumCard(list = player1.hand)
    sum2 = sumCard(list = player2.hand)

    print(player1.name,"'s final sum of cards is:", sum1)
    print(player2.name,"'s final sum of cards is:", sum2)
    #check if bust
    if sum1 > 21:
        print("Bust! " + player1.name + ", you lose the game!")
    elif sum2 >21:
        print("Bust! " + player2.name + ", you lose the game!")

    #check who win
    if sum1 > sum2 and sum1 < 22:
        print(f"{p1} win!!")
    elif sum1 < sum2 and sum2 < 22:
        print(f"{p2} win!!")
    elif sum1 == sum2 and sum1 < 22:
        print("It is a tie!!")
    elif sum1 > 22 and sum2 > 22:
        print("No one win this game!")

    
   
main()