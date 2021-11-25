import pygame

# Colors
BACKGROUND_COLOR = (26, 26, 26)

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()


def main():
    global screen
    global clock
    
    pygame.display.set_caption("Boids")
    
    while True:
        width, height = screen.get_size()
        screen.fill(BACKGROUND_COLOR)
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return
        
        pygame.display.flip()


if __name__ == "__main__":
    main()