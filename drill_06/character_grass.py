from pico2d import *
import math

open_canvas()

# fill here
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
move = 0
turn = 0
angle = 270
while (True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)

    if(turn == 0):
        if(move == 0):
            x = x + 2
        elif(move == 1):
            y = y + 2
        elif(move == 2):
            x = x - 2
        else:
            y = y - 2

        if(x == 780 and y == 90):
            move = 1
        elif(x == 780 and y == 550):
            move = 2
        elif(x == 10 and y == 550):
            move = 3
        elif(x == 10 and y == 90):
            move = 0
            
        if(x == 400 and y == 90):
            turn = 1

    else:
        if(move == 0):
            x = x - math.cos(angle / 360 * 2 * math.pi)
            y = y + math.sin(angle / 360 * 2 * math.pi)
            angle = angle - 2
        elif(move == 1):
            x = x + math.cos(angle / 360 * 2 * math.pi)
            y = y + math.sin(angle / 360 * 2 * math.pi)
            angle = angle - 2
        elif(move == 2):
            x = x + math.cos(angle / 360 * 2 * math.pi)
            y = y - math.sin(angle / 360 * 2 * math.pi)
            angle = angle - 2
        else:
            x = x - math.cos(angle / 360 * 2 * math.pi)
            y = y - math.sin(angle / 360 * 2 * math.pi) 
            angle = angle - 2

        if(angle == 180):
            move = 1
        elif(angle == 90):
            move = 2
        elif(angle == 0):
            move = 3
            angle = 360
        elif(angle == 270):
            move = 0
            
        if(angle == 270):
            turn = 0

        
        

    

    delay(0.01)


close_canvas()
