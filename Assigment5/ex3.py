from turtle import *

def draw_square(length, colour):
        line_color = color(colour)
        for i in range(4):
                forward (length)
                left (90)
        return

print (draw_square(100, "gray"))