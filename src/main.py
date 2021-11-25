import pygame

from pygame.math import Vector2
from typing import List, Tuple
from random import uniform
from boid import Boid

# Colors
BACKGROUND_COLOR: Tuple[int, int, int] = (26, 26, 26)
BOID_COLOR: Tuple[int, int, int] = (248, 248, 248)

# Boid Settings
BOID_COUNT: int = 50

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
flock: List[Boid] = [  ]


def create_flock() -> None:
    global screen
    global flock

    width, height = screen.get_size()

    for _ in range(0, BOID_COUNT):
        new_boid = Boid(position=(width / 2, height / 2))
        new_boid.acceleration = Vector2(uniform(0.1, 0.5), uniform(0.1, 0.5))
        flock.append(new_boid)


def check_bounds() -> None:
    global screen
    global flock
    
    width, height = screen.get_size()
    
    for boid in flock:
        if boid.position.x < 0.0 or boid.position.y < 0.0:
            boid.position = Vector2(0.0, 0.0)
            boid.velocity = Vector2(0.0, 0.0)
        elif boid.position.x > width or boid.position.y > height:
            boid.position = Vector2(0.0, 0.0)
            boid.velocity = Vector2(0.0, 0.0)


def main() -> None:
    global screen
    global clock
    global flock
    
    pygame.display.set_caption("Boids")
    create_flock()
    
    while True:
        clock.tick(60)
        width, height = screen.get_size()
        screen.fill(BACKGROUND_COLOR)
        
        for boid in flock:
            boid.update(surface=screen, color=BOID_COLOR, flock=flock)
        
        check_bounds()
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return
        
        pygame.display.flip()


if __name__ == "__main__":
    main()