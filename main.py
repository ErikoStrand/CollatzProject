import numpy as np
import sys
import pygame
import time
# "{0:.0%}".format(data["lost"]/data["total"])

bg = (200, 200, 200)
box_color = (0, 0, 0)
input_box = pygame.Rect(100, 100, 140, 32)
jumps = 0
max_jump = 0
jump_number = 0
clock = pygame.time.Clock()
number_input = ""
collatz_numbers = []
pygame.init()
pygame.font.init()

font = pygame.font.Font("Pokemon GB.ttf", 32)
screen = pygame.display.set_mode((1600, 600))
screen.fill(bg)
def display(x, y, text, value):
    # clear # left top width height2
    pygame.draw.rect(screen, bg, (x, y, 600, 50))
    draw = font.render(text + value, False, (0, 0, 0))
    screen.blit(draw, (x, y))

def collatz():
    global jumps, number_input, collatz_numbers, max_jump, jump_number
    num = int(number_input)
    # so you can quit while loop is running
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        time.sleep(0.01)
        if num == 1:
            collatz_numbers = []
            max_jump = jumps
            jump_number = number_input
            jumps = 0
            number_input = ""
            break
        elif (num % 2) == 0:
            num = num / 2
            jumps += 1
            collatz_numbers.append(num)

        else:
            num = num * 3 + 1
            jumps += 1
            collatz_numbers.append(num)

        pygame.draw.circle(screen, box_color, (0 + jumps * 10, 500 - num/100), 5)
        display(50, 100, "MAX: ", str(int(max(collatz_numbers))))
        display(50, 150, "Total Jumps: ", str(int(jumps)))
        display(50, 200, "Max Jump: ", str(int(max_jump)))
        display(50, 250, "Jump Number: ", str(int(jump_number)))
        display(50, 300, "Current: ", str(int(collatz_numbers[-1])))
        pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.unicode.isnumeric():
                number_input += event.unicode
                display(50, 50, "Input: ", number_input)

            elif event.key == pygame.K_RETURN:
                if number_input == "":
                    pass
                else:
                    pygame.draw.rect(screen, bg, (0, 350, 1600, 250))
                    collatz()




    # updating visuals

    pygame.display.update()

