from __future__ import annotations
from pygame.math import Vector2
from pygame.draw import circle
from typing import List, Tuple
from pygame import Surface


class Boid:
    position: Vector2
    velocity: Vector2
    acceleration: Vector2
    
    __slots__ = "position", "velocity", "acceleration"
    
    def __init__(self, position: Vector2 = (0.0, 0.0), velocity: Vector2 = (0.0, 0.0), acceleration: Vector2 = (0.0, 0.0)) -> None:
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.acceleration = Vector2(acceleration)
    
    def update(self, surface: Surface, color: Tuple[int, int, int], flock: List[Boid]) -> None:
        self.position += self.velocity
        self.velocity += self.acceleration
        
        circle(
            surface=surface,
            color=color,
            center=(self.position.x, self.position.y),
            radius=5,
            width=0,
        )