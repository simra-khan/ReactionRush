from pygame import *

def draw_rect():
    draw.rect(screen, "blue", Rect(100, height / 2, 50, 50))
    draw.rect(screen, "blue", Rect(width - 100, height / 2, 50, 50))