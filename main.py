import pygame
from pygame.locals import *
import random
import time

pygame.init()

line_count = 10
width = 800
height = 800
true = 1
size = (width, height)
white = (255,255,255)
black = (0,0,0)
lines = []
screen = pygame.display.set_mode(size)

def makeLines():
    global lines, width, line_count
    for line in range(line_count):
        height = random.randint(200, 800)
        x = (int(line * (width/line_count)) , height)
        y = (int(line * (width/line_count)), 800)
        lines.append([x,y])

def drawLines():
    for e in lines:
        pygame.draw.line(screen, white, e[0], e[1], 1)
        pygame.display.update()

#algs

def bubbleSort():
    global lines
    ar = lines
    n = len(ar)
    for i in range(n):
        for j in range(0, n-i-1):
            if ar[j][0][1] > ar[j+1][0][1] :
                ar[j], ar[j+1] = ar[j+1], ar[j]
            break;
    lines = ar



makeLines()


while true:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true=0
    for e in lines:
        pygame.draw.line(screen, white, e[0], e[1], 1)
        pygame.display.update()
        bubbleSort()
    

    # bubbleSort(lines)

# import pygame

# screen = pygame.display.set_mode((640, 480))
# running = 1

# while running:
#     event = pygame.event.poll()
#     if event.type == pygame.QUIT:
#         running = 0

#     screen.fill((0, 0, 0))
#     pygame.draw.line(screen, (0, 0, 255), (0, 0), (639, 479))
#     pygame.draw.aaline(screen, (0, 0, 255), (639, 0), (0, 479))
#     pygame.display.flip()
class Line():
    def __init__(self, width, n, num_lines):
        self.width = 800
        self.num = n
        self.line_count = num_lines

    def create(self, width, line_count):
            for line in range(line_count):
                height = random.randint(200, 800)
                self.x = (int(line * (width/line_count)) , height)
                self.y = (int(line * (width/line_count)), 800)

    def draw(self, screen):
            pygame.draw.line(self.white, self.x, self.y, 1)
            pygame.display.update()
