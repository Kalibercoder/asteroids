import pygame
from player import Player 
from constants import * 
def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")  # Optional: set a window title
    clock = pygame.time.Clock()
    dt = 0
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Allow window close
                running = False        
      
        screen.fill((0, 0, 0))

        player.draw(screen)
       

        # Refresh the display
        pygame.display.flip()
        dt = clock.tick(60) / 1000   
    pygame.quit()

if __name__ == "__main__":
    main()
