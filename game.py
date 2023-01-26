import pygame

pygame.init()


class Game:

    def __int__(self):
        pygame.init()
        pygame.display.set_mode((800, 600))
        pygame.display.set_caption("billy and the paralle world")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


pygame.quit()
