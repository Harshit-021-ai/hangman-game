import pygame

# setup display
pygame.init()
Width, Height= 800, 600
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Hangman Game By Harshit Sharma")

# load images
images = []
for i in range(7):
    image= pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
Hangman_status = 4

# colors
White = (225,225,225)

# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)

    Window.fill(White)
    Window.blit(images[Hangman_status], (150,100))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
