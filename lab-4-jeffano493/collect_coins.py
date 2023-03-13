import pygame
import time
import random

pygame.init()

# Initialize the screen with width = 1000 and height = 1000
screen = pygame.display.set_mode((1000,1000))

# Initialize the coin image
# -- Load the image
coin_image = pygame.image.load("coin.png")
# -- get its rect object
coin_rect = coin_image.get_rect()
# -- place it in the middle of the top border
coin_rect.centerx = screen.get_rect().centerx
# -- blit it on the screen
screen.blit(coin_image,coin_rect)

# Initialize the bank image
# -- Load the image
bank_image = pygame.image.load("bank.png")
# -- get its rect object
bank_rect = bank_image.get_rect()
# -- place it at the middle of the buttom border
bank_rect.centerx = screen.get_rect().centerx
bank_rect.bottom = screen.get_rect().bottom
# -- blit it on the screen
screen.blit(bank_image,bank_rect)

# call flip to refresh the screen
pygame.display.flip()

coin_count = 0
coin_speed = 20
bank_speed = 50
remaining_count = 10

speed = [0,coin_speed]

# The Game Loop
running = True
while running:
   
   # Event loop
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
        
   # Game Logic
   # --> The coin keeps falling from the sky so, z doesn't change but y is incremented by coint_speed
   coin_rect = coin_rect.move(speed)
    
   # --> if it goes out of the screen it comes back from the top at a random x coordinate between 100, 900
   if coin_rect.y > screen.get_rect().height:
      coin_rect.center = (random.randint(100, 900), 0)
      
   # --> if it collides with the bank the coin counter gets increamented by 1
   if bank_rect.colliderect(coin_rect):
      coin_rect.center = (random.randint(100, 900), 0)
      coin_count = coin_count + 1
      # --> the count remaining to move to next level gets decremented by 1
      remaining_count = remaining_count - 1
      # --> print the new coin_count to the terminal
      print(coin_count)
      # --> if the remaining_count is zero 
      if remaining_count == 0:
         # ### --> double the speed 
         coin_speed = coin_speed * 2
         speed = [0, coin_speed]
         # ### --> print ">>>>> New Level Activated"
         print(">>>>> New Level Activated")
         # ### --> reset the remaining_count to 10
         remaining_count = 10
    
   # --> The end user can move the bank left and right using the arrow keys so it would be handled in the event loop
   key_input = pygame.key.get_pressed()
   if key_input[pygame.K_LEFT]:
      bank_rect.x -= bank_speed
   if key_input[pygame.K_RIGHT]:
      bank_rect.x += bank_speed

   # Render
   # --> refill the screen with black
   screen.fill((0,0,0))
   # --> blit the coin
   screen.blit(coin_image,coin_rect)
   # --> blit the bank
   screen.blit(bank_image,bank_rect)
   # --> flip to refresh
   pygame.display.flip()
    
   # slow down the loop a little bit to be able to see the effects
   time.sleep(0.05)

pygame.quit()