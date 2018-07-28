import random
import simplegui

WIDTH = 400
HEIGHT = 400
answer_number = random.randrange(0, 100)

def number_to_fortune(number):
    dic = {0: "Yes, for sure!", 1: "Probably yes.", 2: "Seems like yes...", 
          3: "Definitely not!", 4: "Probably not.", 5: "I really doubt it...",
          6: "Not sure, check back later!", 7: "I really can't tell."}
    if number in range(0, 8):
        return dic[number]
    else:
        return "Something was wrong with my input."

def mystical_octosphere(question):
    print "Your question was... " + question
    print "You shake the mystical octosphere."
    
    answer_fortune = number_to_fortune(answer_number)
    
    print "The cloudy liquid swirls, and a reply comes into view..."
    print "The mystical octosphere says... " + answer_fortune    
    print

def draw_handler(canvas):
    canvas.draw_text("Guess the Number!", [100, 200], 24, "Red")
    
def button_hundred():
    global answer_number
    answer_number = random.randrange(0, 100)

def button_thousand():
    global answer_number
    answer_number = random.randrange(0, 1000)
    
frame = simplegui.create_frame("Mystical Octosphere", WIDTH, HEIGHT)
inp = frame.add_input("What is your question?", mystical_octosphere, 200)
frame.set_draw_handler(draw_handler)
button_one = frame.add_button("[0, 100)", button_hundred, 200)
button_two = frame.add_button("[0, 1000)", button_thousand, 200)

frame.start()