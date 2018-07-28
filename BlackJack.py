# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
# score is the point player got
score = 0

# dictionary for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# basic rules for Hand class and Deck class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# add card to hand(both dealer and player) and caculate value
class Hand:
    def __init__(self):
        self.handlist = []
                
    def __str__(self):
        card_string = ""
        for i in self.handlist:
            card_string += str(i) + " "
        return "Hand contains " + card_string
    
    def add_card(self, card):
        self.handlist.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        exist_A = False
        for i in self.handlist:
            value += VALUES[i.get_rank()]  
            if i.get_rank() == "A":
                exist_A = True
                
        if exist_A and value <= 11:
            value += 10
            
        return value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for j, i in enumerate(self.handlist):
            i.draw(canvas, [pos[0] + 80 * j, pos[1]])
        
# deal and shuffle card
class Deck:
    def __init__(self):
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i, j))
                
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
            
    def __str__(self):
        deck = ""
        for i in self.deck:
            deck += str(i) + " "
        return "Deck contains " + deck   
    
#define event handlers for buttons
def deal():
    global in_play, score, outcome
    global player_hand, dealer_hand, deck
    in_play = True
    outcome = ""
    
    deck = Deck()
    deck.shuffle()
        
    player_card_1 = deck.deal_card()
    player_card_2 = deck.deal_card()
    dealer_card_1 = deck.deal_card()
    dealer_card_2 = deck.deal_card()
    
    print(player_card_1)
    print(player_card_2)
    print(dealer_card_1)
    print(dealer_card_2)
    print("")
    
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(player_card_1)
    player_hand.add_card(player_card_2)
    dealer_hand.add_card(dealer_card_1)
    dealer_hand.add_card(dealer_card_2)
        
    if player_hand.get_value() == 21 and dealer_hand.get_value() != 21:
        outcome = "Blackjack! Player wins!"
        in_play = False
        score += 1
        print player_hand.get_value(), dealer_hand.get_value()
        print ""
    elif dealer_hand.get_value() == 21:
        outcome = "Blackjack! Dealer wins!"
        in_play = False
        score -= 1
        print player_hand.get_value(), dealer_hand.get_value()
        print ""
    
def hit():
    # if the hand is in play, hit the player
    global outcome, in_play, score
    global player_hand, deck
    
    if in_play:
        player_hand.add_card(deck.deal_card())

        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            in_play = False
            outcome = "Busted! Dealer wins!"
            score -= 1
            print player_hand.get_value(), dealer_hand.get_value()
            print ""
    
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global outcome, in_play, score
    global dealer_hand, deck
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
            
        if dealer_hand.get_value() >= 17:
            in_play = False
            if dealer_hand.get_value() > 21:
                outcome =  "Busted! Player wins!"
                score += 1
                print player_hand.get_value(), dealer_hand.get_value()
                print ""
            else:
                if dealer_hand.get_value() >= player_hand.get_value():
                    if dealer_hand.get_value() == 21:
                        outcome = "Blackjack! Dealer wins!"
                    else:
                        outcome = "Dealer wins!"
                    score -= 1
                    print player_hand.get_value(), dealer_hand.get_value()
                    print ""
                else:
                    if player_hand.get_value() == 21:
                        outcome = "Blackjack! Player wins!"
                    else:                 
                        outcome = "Player wins!"
                    score += 1
                    print player_hand.get_value(), dealer_hand.get_value()
                    print ""
                    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text(outcome, [220, 100], 16, "Pink")
    canvas.draw_text("Blackjack", [220, 50], 36, "White")
    player_hand.draw(canvas, [100, 150])
    canvas.draw_text("PLAYER", [200, 300], 16, "White")
    dealer_hand.draw(canvas, [100, 350])
    canvas.draw_text("DEALER", [200, 500], 16, "White")
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_CENTER[0], 350 + CARD_CENTER[1]], CARD_BACK_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()
deal()