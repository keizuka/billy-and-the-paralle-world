import pygame
import pytmx
import pyscroll

from player import Player


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("billy and the paralle world")

        # charger la carte(tmx)
        tmx_data = pytmx.util_pygame.load_pygame('map1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # generer le joueur
        self.player = Player()

        # dessiner le group de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=10)
        self.group.add(self.player)

    def run(self):

        running = True
        while running:

            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
