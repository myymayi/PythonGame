# define global variables
import simplegui

width = 300
height = 200
success_number = 0
attempts_number = 0
time = 0
clicks = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t / 600
    B = (t - A * 600) / 100
    C = (t - A * 600 - B * 100) / 10
    D = t - A * 600 - B * 100 - C * 10  
    timer = str(A) + ":" + str(B)+ str(C) + "." + str(D)                
    return timer
            
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global clicks
    timer.start()
    clicks = False
    
def stop():
    global time
    global success_number
    global attempts_number
    global clicks
    if not clicks:
        timer.stop()                
        attempts_number += 1
        if time % 50.0 == 0:
            success_number += 1
        clicks = True

def reset():
    global time
    global success_number
    global attempts_number
    time = 0
    success_number = 0
    attempts_number = 0
    timer.stop()
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    global time
    global success_number
    global attempts_number
    score = str(success_number) + "/" + str(attempts_number)
    canvas.draw_text(str(format(time)), [width / 3.2, height / 1.8], 40, "white")
    canvas.draw_text(score , [width / 1.18, height / 9], 20, "red")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
start_button = frame.add_button("Start", start, 150)
start_button = frame.add_button("Stop", stop, 150)
start_button = frame.add_button("Reset", reset, 150)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
