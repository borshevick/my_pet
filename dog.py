import pygame as pg


class Dog():
    def __init__(self, xy, size):
        self.picture = pg.image.load("images/dog.png")
        self.picture = pg.transform.scale(self.picture, size)
        self.hitbox = pg.rect.Rect(xy, self.picture.get_size())
        
    def print(self, window):
        window.blit(self.picture, self.hitbox)
        # pg.draw.rect(window, [255, 255, 255], self.hitbox)

class Mini_dog(Dog):
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] == True and self.hitbox.left > 100:
            self.hitbox.x = self.hitbox.x -3
        if keys[pg.K_RIGHT] == True and self.hitbox.left < 775:
            self.hitbox.x = self.hitbox.x +3


