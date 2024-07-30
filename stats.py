import pygame as pg 
import pygame.freetype as pgtype


class Stats():
    def __init__(self, xy, picture, counter,):
        self.picture = picture
        self.hitbox = pg.rect.Rect(xy, [self.picture.get_width(), self.picture.get_height()])
        # self.picture.center = self.hitbox.center 
        self.counter = counter
        self.text_font = pgtype.Font("images/Acumin-ItPro_RUS.ttf", 30)

    def print(self, window):
        txt_list = self.text_font.render(str(self.counter))
        self.txt_picture = txt_list[0]
        self.txt_hitbox = txt_list[1]
        self.txt_hitbox.centerx = self.hitbox.centerx - 50
        self.txt_hitbox.centery = self.hitbox.centery 
        window.blit(self.picture, self.hitbox)
        window.blit(self.txt_picture, self.txt_hitbox)
