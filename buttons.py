import pygame as pg
import pygame.freetype as pgtype
pg.init()


class Button():
    def __init__(self, text, size, xy, function):
        self.picture = pg.image.load("images/button.png").convert_alpha()
        self.picture = pg.transform.scale(self.picture, size)
        self.picture_clicked = pg.image.load("images/button_clicked.png").convert_alpha()
        self.picture_clicked = pg.transform.scale(self.picture_clicked, size)
        self.actual_picture = self.picture
        self.hitbox = pg.rect.Rect(xy, size)
        self.click_time = 0
        self.text = text
        self.text_font = pgtype.Font("images/Acumin-ItPro_RUS.ttf", 30)
        txt_list = self.text_font.render(text)
        self.txt_picture = txt_list[0]
        self.txt_hitbox = txt_list[1]
        self.txt_hitbox.center = self.hitbox.center
        self.function = function

    def print(self, window):
        window.blit(self.actual_picture, self.hitbox)
        window.blit(self.txt_picture, self.txt_hitbox)

    def click(self):
        self.actual_picture = self.picture_clicked
        self.click_time = pg.time.get_ticks()
        self.function()

    def logic(self):
        if pg.time.get_ticks() - self.click_time >= 5:
            self.actual_picture = self.picture
            