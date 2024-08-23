import pygame

from sys import exit

from player import Player

from tilemap import Map


class Game:
    def __init__(self):
        pygame.init()

        self.WIDTH, self.HEIGTH = 640, 480
        self.BLOCK_SIZE = 40
        self.PLAYER_SPEED = 5


        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGTH))
        pygame.display.set_caption("Testando Joguinho")

        self.clock = pygame.time.Clock()

        self.player = Player(self.WIDTH//2, self.HEIGTH//2, self.BLOCK_SIZE, self.PLAYER_SPEED)

        self.colors = ["yellow", "blue", "orange", "green"]

        self.generate_new_map()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player.update_direction("up")
                    if event.key == pygame.K_s:
                        self.player.update_direction("down")
                    if event.key == pygame.K_a:
                        self.player.update_direction("left")
                    if event.key == pygame.K_d:
                        self.player.update_direction("right")
                    if event.key == pygame.K_SPACE:
                        self.generate_new_map
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.player.update_direction("letgo_w")
                    if event.key == pygame.K_s:
                        self.player.update_direction("letgo_s")
                    if event.key == pygame.K_a:
                        self.player.update_direction("letgo_a")
                    if event.key == pygame.K_d:
                        self.player.update_direction("letgo_d")



            self.screen.fill("green")
            self.player.move()
            self.realocate_player()
            self.map.draw(self.screen)
            self.player.draw(self.screen, "red")
            pygame.display.update()
            self.clock.tick(60)
    
    def realocate_player(self):
        if self.player.rect.x < 0:
            self.generate_new_map()
            self.player.rect.x += self.WIDTH
        if self.player.rect.x > self.WIDTH:
            self.generate_new_map()
            self.player.rect.x -= self.WIDTH
        if self.player.rect.y < 0:
            self.generate_new_map()
            self.player.rect.y += self.HEIGTH
        if self.player.rect.y > self.HEIGTH:
            self.generate_new_map()
            self.player.rect.y -= self.HEIGTH
    
    def generate_new_map(self):
        self.map = Map(self.WIDTH, self.HEIGTH, self.BLOCK_SIZE)
        self.map.generate_map(self.colors)


Game().run()
    



