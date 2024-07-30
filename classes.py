import pygame as pg
import random
import os


class Food():
    def __init__(self, picture, xy, size, price, food_points):
        self.picture = picture.convert_alpha()
        self.xy = xy
        self.size = size
        self.hitbox = pg.rect.Rect(xy, size)
        self.price = price
        self.food_points = food_points
        self.food_event = pg.USEREVENT
    def print(self, window):
        window.blit(self.picture, self.hitbox)

    def logic(self):
        pg.time.set_timer(self.food_event, 2000)
    

class Clothes():
    def __init__(self, picture, xy, size, price, buy, wear):
        self.picture = picture.convert_alpha()
        self.xy = xy
        self.size = size
        self.hitbox = pg.rect.Rect(xy, size)
        self.price = price
        self.buy = buy
        self.wear = wear
    def print(self, window):
        window.blit(self.picture, self.hitbox)
    def slovar(self):
        slovar = {"price": self.price, "buy": self.buy, "wear": self.wear}
        return slovar

class Toys():

    list_toys_names = os.listdir('images/toys')
    toys_list_pic = []
    for i in list_toys_names:
        pic = pg.image.load('images/toys/'+i)
        pic = pg.transform.scale(pic, [200, 200])
        toys_list_pic.append(pic)

    def __init__(self):
        self.picture_index = random.randint(0, len(Toys.toys_list_pic) - 1)
        self.picture = self.toys_list_pic[self.picture_index].convert_alpha()
        self.hitbox = pg.Rect([random.randint(100, 400), 100], self.picture.get_size())
        self.hitbox2 = pg.Rect([0, 0], [self.hitbox.width//2, self.hitbox.height//3])
    
    def print(self, window):
        window.blit(self.picture, self.hitbox)
        
    def move(self):
        self.hitbox.y = self.hitbox.y + 1
        self.hitbox2.center = self.hitbox.center