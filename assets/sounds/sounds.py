import pygame


class SoundManager:

    def __init__(self):
        self.sounds = {
            'mainBGM': pygame.mixer.Sound("asset/sounds/mainBGM.ogg")
        }

    def play(self, name):
        self.sounds[name].play()
