#Platformer demo for Yr11
#Juergen Lier
#Version 1_1
#Aug 2022
#Changes: Created main window and added a sprite to move around

import pygame
pygame.init()

#Setting the size of the display window
win = pygame.display.set_mode((500, 500))

#Setting a caption for the game
pygame.display.set_caption("Demo platformer")

#Set co-ordinates of where sprite will appear and its height and width
x = 50
y = 50
width = 20
height = 30

#Set velocity to control speed of sprite
vel = 5

#Game loop starts
done = True
while done:
    pygame.time.delay(60)

    #Quit the game when the window gets closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    #Movement code
    #moves character for as long as the key get held down in what ever direction
    #Set up a list to do this.
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    if keys[pygame.K_ESCAPE]:
        done = False

    #Draw over the above rectangle to cover up its tracks
    win.fill((0,0,0))
    
    #draw a rectangle which will represent the character in the game
    # win = the window we draw on, RGB values, rect with x y width height
    pygame.draw.rect(win,(255,0,255), (x, y, width, height))
    
    #update the screen, otherwise nothing will draw
    pygame.display.update()


pygame.quit()

