import random
import pygame

class WanderingMonster:
    def __init__(self, name, health, power, position):
        self.name = name
        self.health = health
        self.power = power
        self.position = position  # Position as a tuple (x, y)

    @staticmethod
    def new_random_monster(grid_size):
        # Create a monster with random attributes
        name = "Monster"  # You can enhance this to generate random names
        health = random.randint(10, 50)
        power = random.randint(1, 10)
        position = (random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1))
        return WanderingMonster(name, health, power, position)
    def move(self,grid_size):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                new_x, new_y = x, y  # Reset new position to current position
                if event.key == pygame.K_LEFT:
                    new_x -= 32
                elif event.key == pygame.K_RIGHT:
                    new_x += 32
                elif event.key == pygame.K_UP:
                    new_y -= 32
                elif event.key == pygame.K_DOWN:
                    new_y += 32
                elif event.key == pygame.K_SPACE:
                    gameExit = True
