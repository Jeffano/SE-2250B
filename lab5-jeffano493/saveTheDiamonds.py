import pygame, time, random
import gameobjects

pygame.init()

# Initialize the game
bg_img = pygame.image.load('background.jpg')
bg_rect = bg_img.get_rect()

takenCount = 0
savedCount = 0

backgroundColor = (68, 115, 197)
font = pygame.font.Font("CoffeeHealing.ttf", 35)

screen = pygame.display.set_mode((1400, bg_rect.height))

screen_rect = pygame.Rect(200,0,1200,bg_rect.height)
left_rect = pygame.Rect(0,0,200,bg_rect.height)
right_rect = pygame.Rect(1200,0,1400,bg_rect.height)


no_of_diamonds = 10
diamond_group = pygame.sprite.Group()
for i in range(no_of_diamonds):
   diamond_group.add(gameobjects.Diamond(screen_rect))

no_of_spaceships = 1
spaceship_group = pygame.sprite.Group()
for i in range(no_of_spaceships):
   spaceship_group.add(gameobjects.Spaceship(screen_rect))

taken_group = pygame.sprite.Group()
saved_group = pygame.sprite.Group()


def render():
    screen.fill(backgroundColor)
    screen.blit(bg_img,(200,0))
    
    diamond_group.update()
    diamond_group.draw(screen)

    spaceship_group.update()
    spaceship_group.draw(screen)

    # Render taken count
    textTaken = font.render("Taken: " + str(takenCount), True, pygame.Color(255, 255, 255))
    screen.blit(textTaken, (0,0))
    taken_group.update()
    taken_group.draw(screen)

    # Render saved count
    textSaved = font.render("Saved: " + str(savedCount), True, pygame.Color(255, 255, 255))
    screen.blit(textSaved, (1200,0))
    saved_group.update()
    saved_group.draw(screen)

    pygame.display.flip()


render()
running = True
# gameloop
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in diamond_group.sprites():
                if sprite.rect.collidepoint(event.pos):
                    diamond_group.remove(sprite)
                    diamond_group.update()
                    diamond_group.draw(screen)


                    saved_group.add(gameobjects.collectDiamonds(right_rect))
                    saved_group.update()
                    saved_group.draw(screen)
                    savedCount += 1
                          
    #game logic
    collision = pygame.sprite.groupcollide(diamond_group,spaceship_group,True,False)
    for sprite in collision:
        taken_group.add(gameobjects.collectDiamonds(left_rect))
        taken_group.update()
        taken_group.draw(screen)
        takenCount += 1

    #render
    render()
    time.sleep(0.05)

pygame.quit()