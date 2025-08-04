#Platformer demo for Yr11
#Juergen Lier
#Version 1_2
#Aug 2022

import pygame
pygame.init()

#Setting the size of the display window
screen = ((500, 500))
win = pygame.display.set_mode((screen))

ScreenWidth = 500

#Setting a caption for the game
pygame.display.set_caption("Demo platformer")

#Set co-ordinates of where sprite will appear and its height and width
x = 50
y = 420
width = 20
height = 30

#Set velocity to control speed of sprite
vel = 5

#Jump code
isJump = False
jumpCount = 10

#Game loop starts
done = True
while done:
    pygame.time.delay(100)

    #Quit the game when the window gets closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    #Movement code
    #moves character for as long as the key get held down in what ever direction
    #Set up a list to do this.
    #To create boundary so character doesnt move off screen, add 'and' onto key press
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < ScreenWidth - width - vel:
        x += vel

    #If the spacebar is pressed, then up and down keys won't work anymore.
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < ScreenWidth - width -vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    #Game quits when I press the escape key
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

