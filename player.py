import pygame


class Player:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.movement_x = [False, False]
        self.movement_y = [False, False]
        self.speed = speed

    def update_direction(self, direction):
        match direction:
            case "up":
                self.movement_y[0] = True
                self.movement_y[1] = False
            case "down":
                self.movement_y[1] = True
                self.movement_y[0] = False
                
            case "left":
                self.movement_x[0] = True
                self.movement_x[1] = False
            case "right":
                self.movement_x[1] = True
                self.movement_x[0] = False
            case "letgo_w":
                self.movement_y = [False, False]
            case "letgo_s":
                self.movement_y = [False, False]
            case "letgo_a":
                self.movement_x = [False, False]
            case "letgo_d":
                self.movement_x = [False, False]


        
        
    
    def move(self):
        self.rect.x += ((self.movement_x[1] - self.movement_x[0]) * self.speed)
        self.rect.y -= ((self.movement_y[0] - self.movement_y[1]) * self.speed)


    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)
    
