from Speller import P300
import pygame
import csv
pygame.init()
P3 = P300(800, 800)
done = False
while not done:
    x = int(input("enter 0, 1, or 2: "))
    if x != 0 and x != 1 and x != 2:
        done = True
    else:
        P3.move(x)
        P3.get_state()
P3.show_log()
