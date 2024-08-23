import random
import pygame

class Map:
    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.grid = []
        self.tiles = []
    

    def generate_map(self, colors):
        self.colors = colors
        number_colors = len(colors)
        tiles_x = self.x // self.block_size
        tiles_y = self.y // self.block_size

        for i in range(tiles_x):
            row = []
            for j in range(tiles_y):
                x = random.randint(0, number_colors - 1)
                row.append(x)
            self.grid.append(row)
    
    def draw(self, surface):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                rect = pygame.Rect(i *  self.block_size, j * self.block_size, self.block_size, self.block_size)
                pygame.draw.rect(surface, self.colors[self.grid[i][j]], rect)

        



    