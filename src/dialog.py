import pygame


class DialogBox:

    X_POSITION = 850/4
    Y_POSITION = 850/2

    def __init__(self):
        self.box = pygame.image.load('C:/Users/babou/Documents/GitHub/billy-and-the-paralle-world/dialogs/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (500, 50))
        self.texts = []
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font("C:/Users/babou/Documents/GitHub/billy-and-the-paralle-world/dialogs/dialog_font.ttf", 18)
        self.reading = False

    def execute(self, dialog=[]):
        if self.reading:
            self.next_text()
        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog

    def render(self, screen):
        if self.reading:
            self.letter_index += 1

            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index

            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
            screen.blit(text, (self.X_POSITION + 30, self.Y_POSITION + 10))

    def next_text(self):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            self.reading = False
