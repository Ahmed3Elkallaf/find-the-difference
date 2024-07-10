import pygame
import time


#screen displaying
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("spot the difference")

# variables
level = 1
all_spotted = 0

# differences  (hidden sqaures if mouse pressed them create a circle)
spot1 = pygame.Rect((700,320,30,30))
pygame.draw.rect(screen,(255,255,255),spot1)

spot2 = pygame.Rect((500,360,30,30))
pygame.draw.rect(screen,(255,255,255),spot2)

spot3 = pygame.Rect((416,385,30,30))
pygame.draw.rect(screen,(255,255,255),spot3)

reverse_spot1 = pygame.Rect((295,320,30,30))
pygame.draw.rect(screen,(255,255,255),reverse_spot1)

reverse_spot2 = pygame.Rect((100,350,30,30))
pygame.draw.rect(screen,(255,255,255),reverse_spot2)

reverse_spot3 = pygame.Rect((10,370,30,30))
pygame.draw.rect(screen,(255,255,255),reverse_spot3)


# display images
img = pygame.transform.scale(pygame.image.load("find difference.jpg"),(800,600))
screen.blit(img,(0,0))



run = True
# level 1
while run and level == 1:

    mouse_pos = pygame.mouse.get_pos() # get mouse position every loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if all_spotted == 3:
        win = pygame.transform.scale(pygame.image.load("you win.jpg"),(800,600))
        screen.blit(win,(0,0))
        time.sleep(0.1)
        level += 1

 # if pressed on mouse and one of position of hidden sqaures collide with mouse position create a circle
    if event.type == pygame.MOUSEBUTTONDOWN and spot1.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (295,320),40,5)
        spot1.x = 900
        reverse_spot1.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and spot2.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (100,350),40,5)
        spot2.x = 900
        reverse_spot2.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and spot3.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (10,370),40,5)
        spot3.x = 900
        reverse_spot3.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot1.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (700,320),40,5)
        reverse_spot1.x = 900
        spot1.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot2.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (500,360),40,5)
        reverse_spot2.x = 900
        spot2.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot3.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (416,385),40,5)
        reverse_spot3.x = 900
        spot3.x = 900
        all_spotted += 1


    pygame.display.update()

time.sleep(1)

# level 2
spot1 = pygame.Rect((700,160,30,30))
pygame.draw.rect(screen,(0,0,0),spot1)

spot2 = pygame.Rect((455,170,40,40))
pygame.draw.rect(screen,(0,0,0),spot2)

spot3 = pygame.Rect((466,410,30,60))
pygame.draw.rect(screen,(0,0,0),spot3)

reverse_spot3 = pygame.Rect((55,450,30,60))
pygame.draw.rect(screen,(0,0,0),reverse_spot3)

reverse_spot1 = pygame.Rect((295,160,30,30))
pygame.draw.rect(screen,(0,0,0),reverse_spot1)

reverse_spot2 = pygame.Rect((50,174,30,30))
pygame.draw.rect(screen,(0,0,0),reverse_spot2)

img = pygame.transform.scale(pygame.image.load("find difference2.jpg"),(800,600))
screen.blit(img,(0,0))



while run and level == 2:

    mouse_pos = pygame.mouse.get_pos() # get mouse position every loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if all_spotted == 6:
        win = pygame.transform.scale(pygame.image.load("you win.jpg"),(800,600))
        screen.blit(win,(0,0))
        time.sleep(0.1)
        level += 1

 # if pressed on mouse and one of position of hidden sqaures collide with mouse position create a circle
    if event.type == pygame.MOUSEBUTTONDOWN and spot1.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),20,5)
        pygame.draw.circle(screen , (0,255,0) , (295,170),20,5)
        spot1.x = 900
        reverse_spot1.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and spot2.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (50,174),40,5)
        spot2.x = 900
        reverse_spot2.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and spot3.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (55,450),40,5)
        spot3.x = 900
        reverse_spot3.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot1.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (700,160),40,5)
        reverse_spot1.x = 900
        spot1.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot2.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (475,185),40,5)
        reverse_spot2.x = 900
        spot2.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot3.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (482,440),40,5)
        reverse_spot3.x = 900
        spot3.x = 900
        all_spotted += 1


    pygame.display.update()


time.sleep(1)

# differences  (hidden sqaures if mouse pressed them create a circle)

spot1 = pygame.Rect((755,485,40,50))
pygame.draw.rect(screen,(255,255,255),spot1)

spot2 = pygame.Rect((645,280,30,50))
pygame.draw.rect(screen,(255,255,255),spot2)

spot3 = pygame.Rect((490,480,20,40))
pygame.draw.rect(screen,(255,255,255),spot3)

reverse_spot1 = pygame.Rect((350,485,40,50))
pygame.draw.rect(screen,(255,255,255),reverse_spot1)

reverse_spot2 = pygame.Rect((235,280,30,50))
pygame.draw.rect(screen,(255,255,255),reverse_spot2)

reverse_spot3 = pygame.Rect((90,465,20,40))
pygame.draw.rect(screen,(255,255,255),reverse_spot3)

# display images
img = pygame.transform.scale(pygame.image.load("find difference3.jpg"),(800,600))
screen.blit(img,(0,0))


run = True
# level 3
while run and level == 3:

    mouse_pos = pygame.mouse.get_pos() # get mouse position every loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if all_spotted == 9:
        win = pygame.transform.scale(pygame.image.load("you win.jpg"),(800,600))
        screen.blit(win,(0,0))
        time.sleep(0.1)
        level += 1

 # if pressed on mouse and one of position of hidden sqaures collide with mouse position create a circle
    if event.type == pygame.MOUSEBUTTONDOWN and spot1.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (370,505),40,5)
        spot1.x = 900
        reverse_spot1.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and spot2.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (245,300),40,5)
        spot2.x = 900
        reverse_spot2.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and spot3.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (90,465),40,5)
        spot3.x = 900
        reverse_spot3.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot1.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (755,485),40,5)
        reverse_spot1.x = 900
        spot1.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot2.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (655,300),40,5)
        reverse_spot2.x = 900
        spot2.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot3.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (490,510),40,5)
        reverse_spot3.x = 900
        spot3.x = 900
        all_spotted += 1


    pygame.display.update()


time.sleep(1)
# differences  (hidden sqaures if mouse pressed them create a circle)

spot1 = pygame.Rect((710,405,20,100))
pygame.draw.rect(screen,(0,0,0),spot1)

spot2 = pygame.Rect((600,395,30,50))
pygame.draw.rect(screen,(0,0,0),spot2)

spot3 = pygame.Rect((515,490,70,30))
pygame.draw.rect(screen,(0,0,0),spot3)

spot4 = pygame.Rect((490,185,60,60))
pygame.draw.rect(screen,(255,255,255),spot4)

spot5 = pygame.Rect((555,305,40,50))
pygame.draw.rect(screen,(0,0,0),spot5)

reverse_spot1 = pygame.Rect((315,405,20,100))
pygame.draw.rect(screen,(0,0,0),reverse_spot1)

reverse_spot2 = pygame.Rect((205,395,30,50))
pygame.draw.rect(screen,(0,0,0),reverse_spot2)

reverse_spot3 = pygame.Rect((125,490,70,20))
pygame.draw.rect(screen,(0,0,0),reverse_spot3)

reverse_spot4 = pygame.Rect((110,185,60,60))
pygame.draw.rect(screen,(0,0,0),reverse_spot4)

reverse_spot5 = pygame.Rect((170,305,40,40))
pygame.draw.rect(screen,(0,0,0),reverse_spot5)

# display images
img = pygame.transform.scale(pygame.image.load("find difference4.jpg"),(800,600))
screen.blit(img,(0,0))


run = True

# level 4
while run and level == 4:

    mouse_pos = pygame.mouse.get_pos() # get mouse position every loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if all_spotted == 14:
        win = pygame.transform.scale(pygame.image.load("you win.jpg"),(800,600))
        screen.blit(win,(0,0))
        time.sleep(0.1)
        level += 1

 # if pressed on mouse and one of position of hidden sqaures collide with mouse position create a circle
    if event.type == pygame.MOUSEBUTTONDOWN and spot1.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (315,445),40,5)
        spot1.x = 900
        reverse_spot1.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and spot2.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (220,415),40,5)
        spot2.x = 900
        reverse_spot2.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and spot3.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (160,490),40,5)
        spot3.x = 900
        reverse_spot3.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and spot4.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),50,5)
        pygame.draw.circle(screen , (0,255,0) , (140,210),50,5)
        spot4.x = 900
        reverse_spot4.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and spot5.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),30,5)
        pygame.draw.circle(screen , (0,255,0) , (180,315),30,5)
        spot5.x = 900
        reverse_spot5.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot1.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (710,445),40,5)
        reverse_spot1.x = 900
        spot1.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot2.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (615,420),40,5)
        reverse_spot2.x = 900
        spot2.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot3.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),40,5)
        pygame.draw.circle(screen , (0,255,0) , (550,500),40,5)
        reverse_spot3.x = 900
        spot3.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot4.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),50,5)
        pygame.draw.circle(screen , (0,255,0) , (530,200),50,5)
        reverse_spot4.x = 900
        spot4.x = 900
        all_spotted += 1

    if event.type == pygame.MOUSEBUTTONDOWN and reverse_spot5.collidepoint(mouse_pos):
        pygame.draw.circle(screen , (0,255,0) , (mouse_pos),30,5)
        pygame.draw.circle(screen , (0,255,0) , (575,325),30,5)
        reverse_spot5.x = 900
        spot5.x = 900
        all_spotted += 1



    pygame.display.update()

time.sleep(1)

pygame.quit()

