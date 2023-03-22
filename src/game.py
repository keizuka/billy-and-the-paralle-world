import pygame
import pytmx
import pyscroll
from player import Player
from src.map import MapManager


class Game:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((850, 850))
        pygame.display.set_caption("billy and the paralle world")
        pygame.mixer.music.load('G:/GitHub/billy-and-the-paralle-world/assets/Music/village-music.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

        # generer le joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)

    def handle_input(self):

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_z]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_s]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_q]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_d]:
            self.player.move_right()
            self.player.change_animation('right')
        # elif pressed[pygame.K_ESCAPE]:

    def update(self):
        self.map_manager.update()

    def run(self):

        clock = pygame.time.Clock()

        running = True
        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
