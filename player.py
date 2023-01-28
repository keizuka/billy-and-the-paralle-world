import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.sprite_sheet = pygame.image.load('assets/Male/Male 01-1.png')
        self.image = self.get_image(32, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
