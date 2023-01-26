import pygame


class SoundManager:

    def __int__(self):
        self.sounds = {
            'mainBGM': pygame.mixer.Sound("asset/sounds/mainBGM.ogg")
        }

    def play(self, name):
        self.sounds[name].play()
