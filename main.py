
import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def compare(a, b):

    if a > 21 and b > 21 :
        return f"Your score is greater than 21. You lose! "

    if a == b :
        return "Draw 🙃"
        
    elif b == 0 :
        return "Lose, opponent has Blackjack 😱"
        
    elif a == 0 :
        return "Win with a Blackjack 😎"
        
    elif a > 21:
        return "Your score is greater than 21. You lose 😭"
        
    elif b > 21:
        return "Opponent score is greater than 21. You win 😁"
    
    elif a > b:
        return "You win 😃"
        
    else:
        return "You lose 😤"
           

def deal_card(a):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_drawn = random.choice(cards)
    return a.append(card_drawn)


def calculate_score(a): 

    if (11 in a) and (10 in a) and (len(a) == 2) :
        return 0

    if (11 in a) and (sum(a) > 21) :
        a.append(1)
        a.remove(11)
    
    return sum(a)

     
def black_jack() :

    print(logo)

    dealer_deck = []
    our_deck = []
    
    for i in range(2):
        deal_card(dealer_deck)
        deal_card(our_deck)

    game = True
    
    while game :

        print("The dealer gave everyone cards")
        print(f"Your cards are {our_deck}")
        print(f"One of the dealers card is : {dealer_deck[0]}")
        
        our_score = calculate_score(our_deck)
        print(f"Your score is {our_score}")
        
        dealer_score = calculate_score(dealer_deck)
        
    
        if (our_score == 0) or (dealer_score == 0) or (our_score > 21) :
            game = False
    
        else:
            another_card = input("Do you want another card? 'y' or 'n' ? ")
    
            if another_card == "y" :
                deal_card(our_deck)
    
            if another_card == "n" :
                game = False
    
    while (dealer_score != 0) and (dealer_score < 17) :
        deal_card(dealer_deck)
        dealer_score = calculate_score(dealer_deck)
    
    print(f"Your final hand: {our_deck}, final score: {our_score}")
    print(f"Dealer's final hand: {dealer_deck}, final score: {dealer_score}")
    print(compare(our_score, dealer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear() 
  black_jack()
    