import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode(display_width, display_height)

pygame.display.set_caption("Car racing game")

clock = pygame.time.clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            crashed = True
        print(event)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()