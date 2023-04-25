import pygame
import pytmx
import pyscroll
from player import Player
from src.dialog import DialogBox
from src.map import MapManager


class Game:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_icon(pygame.image.load('C:/Users/babou/Documents/GitHub/billy-and-the-paralle-world/assets/Icons/gameIcon.png'))
        pygame.display.set_caption("billy and the paralle world")
        pygame.mixer.music.load('C:/Users/babou/Documents/GitHub/billy-and-the-paralle-world/assets/Music/village-music.mp3'),
        pygame.mixer.music.play(-1),
        pygame.mixer.music.set_volume(0.1)

        # generer le joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()

    def handle_input(self):

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_z]:
            self.player.move_up()
        elif pressed[pygame.K_s]:
            self.player.move_down()
        elif pressed[pygame.K_q]:
            self.player.move_left()
        elif pressed[pygame.K_d]:
            self.player.move_right()
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
            self.dialog_box.render(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collision(self.dialog_box)

            clock.tick(60)

        pygame.quit()
