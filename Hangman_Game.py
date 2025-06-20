import pygame
import os

pygame.init()
Width = 800
Height = 600
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Hangman Game By Harshit Sharma")

FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
