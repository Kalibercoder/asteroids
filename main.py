import pygame
from constants import * 
def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")  # Optional: set a window title
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Allow window close
                running = False
        
      
        screen.fill((0, 0, 0))

        # Refresh the display
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
