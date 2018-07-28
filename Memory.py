# implementation of card game - Memory
import simplegui
import random

# define keys and ciphers
WIDTH = 800
HEIGHT = 100
CARD_WIDTH = 50
cipher = {}

def new_game():
    global turns, state, exposed
    global card_number, number, cipher
    # create cipher
    card_number = range(16)
    number = range(8) * 2
    random.shuffle(number)
    for n in card_number:
        cipher[n] = number.pop()
    turns = 0
    label.set_text("Turns = 0")
    state = 0
    exposed = [False] * 16
        
# define event handlers        
def mouseclick(pos):
    # add game state logic here
    global turns, state, exposed
    global key1, key2
    pos = list(pos)
    # selecting two cards and determining if they match
    if state == 0:
        state = 1
        # exposed 1st card
        key1 = pos[0] / CARD_WIDTH
        exposed[key1] = True
    elif state == 1:
        state = 2
        # exposed 2nd card
        key2 = pos[0] / CARD_WIDTH 
        if not exposed[key2]:
            exposed[key2] = True
    elif state == 2:
        state = 1
        key3 = pos[0] / CARD_WIDTH
        if not exposed[key3]:
            turns += 1 
            label.set_text("Turns = " + str(turns))
            # if are not paired
            if cipher[key1] != cipher[key2]:
                # exposed 1 card and unexposed 2 cards
                exposed[key1] = False
                exposed[key2] = False
            key1 = key3
            exposed[key1] = True
                  
def draw(canvas):
    # either draw a blank green rectangle or the card's value
    global card_number
    for n in card_number:
        if exposed[n]:
            canvas.draw_polygon(([n * CARD_WIDTH, 0], [n * CARD_WIDTH, HEIGHT], 
                         [(n + 1) * CARD_WIDTH, HEIGHT], [(n + 1) * CARD_WIDTH, 0]), 
                        2, "Black")  
            canvas.draw_text(str(cipher[n]), [n * CARD_WIDTH + 13, HEIGHT / 1.5], 48, "Black")
        else:
            canvas.draw_polygon(([n * CARD_WIDTH, 0], [n * CARD_WIDTH, HEIGHT], 
                         [(n + 1) * CARD_WIDTH, HEIGHT], [(n + 1) * CARD_WIDTH, 0]), 
                        2, "White", "Green")  

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
frame.set_canvas_background("White")

# get things rolling
new_game()
frame.start()