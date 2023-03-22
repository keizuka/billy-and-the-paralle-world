# seulement pour lancer le jeu
import pygame
from game import Game

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
