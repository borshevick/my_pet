import pygame as pg
import buttons
import classes 
import os
import pygame.freetype as pgtype
import random
import dog
import json


class Menu():
    def __init__(self, picture, game):
        self.picture = picture
        self.game = game
        self.list_buttons = []

    def logic(self):
        for i in self.list_buttons:
            i.logic()

    def draw(self):
        self.game.window.blit(self.picture, [0, 0])
        for i in self.list_buttons:
            i.print(self.game.window)

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                file = open("saves.json", "w")
                slovar = {"coins": self.game.coins.counter, "food": self.game.food.counter, "happines": self.game.happiness.counter, "health": self.game.health.counter, "clothes": self.game.menuclothesobject.slovari(), "bonus": self.game.bonus, "click": self.game.click}
                json.dump(slovar, file)

                file.close()
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.game.actualmenu = None
            if event.type == pg.MOUSEBUTTONDOWN:
                for i in self.list_buttons:
                    if i.hitbox.collidepoint(event.pos):
                        i.click()
            self.ft(event)

    def ft(self, event_object):
        pass

class MenuFood(Menu):
    def __init__(self, picture, game):
        super().__init__(picture, game)
        self.food_left = buttons.Button('<-', [200, 50], [200, 525], self.food_select_left)
        self.food_right = buttons.Button('->', [200, 50], [600, 525], self.food_select_right)
        self.food_eat = buttons.Button('Eat', [200, 50], [400, 525], self.eat)
        self.list_buttons = [self.food_left, self.food_right, self.food_eat]
        self.list_food_names = os.listdir('images/food')
        food_list_pic = []
        self.food_obects = [] 
        self.text_font = pgtype.Font("images/Acumin-ItPro_RUS.ttf", 20)
        for i in self.list_food_names:
            pic = pg.image.load('images/food/'+i).convert_alpha()
            pic = pg.transform.scale(pic, [300, 300])
            food_list_pic.append(pic)
        price = 100
        food_points = 5
        for i in food_list_pic:
            object = classes.Food(i, [self.food_right.hitbox.x-250, 220], [i.get_width(), i.get_height()], price, food_points)
            price = price + 50
            food_points = food_points + 25
            self.food_obects.append(object)
        self.index = 0

    def eat(self):
        
        if self.food_obects[self.index].price <= self.game.coins.counter:
            self.game.coins.counter = self.game.coins.counter - self.food_obects[self.index].price
            if self.index == len(self.food_obects) - 1:
                self.game.health.counter = self.game.health.counter + 20 
                self.game.food.counter = self.game.food.counter + self.food_obects[self.index].food_points 
            else:
                self.game.food.counter = self.game.food.counter + self.food_obects[self.index].food_points 
            if self.game.food.counter > 100:
                self.game.food.counter = 100
            

    def food_select_left(self):
        if self.index == 0:
            self.index = len(self.food_obects)-1
        else:
            self.index = self.index-1

    def food_select_right(self):
        if self.index == len(self.food_obects)-1:
            self.index = 0
        else:
            self.index = self.index+1
    
    def draw(self):
        super().draw()
        self.food_obects[self.index].print(self.game.window)
        self.text_font.render_to(self.game.window, [450, 220], str(self.food_obects[self.index].price))
        self.text_font.render_to(self.game.window, [450, 200], str(self.list_food_names[self.index][0:-4]))
class MenuClothes(Menu):
    def __init__(self, picture, game):
        super().__init__(picture, game)
        clothes_saves = game.file_read["clothes"]
        self.clothing_left = buttons.Button('<-', [200, 50], [200, 500], self.clothing_select_left)
        self.clothing_right = buttons.Button('->', [200, 50], [600, 500], self.clothing_select_right)
        self.buy = buttons.Button('Buy', [200, 50], [400, 500], self.buy_clothes) 
        self.wear = buttons.Button('Wear', [200, 50], [400, 550], self.wear_clothes)
        self.list_buttons = [self.clothing_left, self.clothing_right, self. buy, self.wear]
        self.list_clothes_names = os.listdir('images/items')
        clothes_list_pic = []
        self.clothing_obects = [] 
        self.text_font = pgtype.Font("images/Acumin-ItPro_RUS.ttf", 20)
        for i in self.list_clothes_names:
            pic = pg.image.load('images/items/'+i).convert_alpha()
            pic = pg.transform.scale(pic, [300, 400])
            clothes_list_pic.append(pic)
        price = 30
        index = 0
        for i in clothes_list_pic:
            slovar = clothes_saves[index]
            object = classes.Clothes(i, [340, 175], [i.get_width(), i.get_height()], price, slovar["buy"], slovar["wear"] )
            price = price + 5
            self.clothing_obects.append(object)
            index = index + 1
        self.index = 0
        dog

    def clothing_select_left(self):
        if self.index == 0:
            self.index = len(self.clothing_obects)-1
        else:
            self.index = self.index-1

    def clothing_select_right(self):
        if self.index == len(self.clothing_obects)-1:
            self.index = 0
        else:
            self.index = self.index+1
    
    def buy_clothes(self):
        object = self.clothing_obects[self.index]
        if object.price <= self.game.coins.counter:
            self.game.coins.counter = self.game.coins.counter - object.price
            object.buy = True

    def wear_clothes(self):
        object = self.clothing_obects[self.index]
        if object.buy == True and object.wear == False:
             object.wear = True

        elif object.buy == True and object.wear == True:
            object.wear = False

    def draw(self):
        super().draw()
        self.clothing_obects[self.index].print(self.game.window)
        self.text_font.render_to(self.game.window, [450, 220], str(self.clothing_obects[self.index].price))
        self.text_font.render_to(self.game.window, [450, 200], str(self.list_clothes_names[self.index][0:-4]))
        if self.clothing_obects[self.index].buy == True:
            self.text_font.render_to(self.game.window, [640, 400], 'Bought', [0, 255, 0])
        if self.clothing_obects[self.index].buy == False:
            self.text_font.render_to(self.game.window, [640, 400],"Didn't bought", [255, 0, 0])
        if self.clothing_obects[self.index].wear == True:
            self.text_font.render_to(self.game.window, [640, 450], 'Wear', [0, 255, 0])
        if self.clothing_obects[self.index].wear == False:
            self.text_font.render_to(self.game.window, [640, 450],"Didn't wear", [255, 0, 0])

    def slovari(self):
        slovar_list = []
        for i in self.clothing_obects:
            r = i.slovar()
            slovar_list.append(r)
        return slovar_list

class MenuMinigame(Menu):
    def __init__(self, picture, game):
        super().__init__(picture, game)
        self.dog = dog.Mini_dog([100, 475], [120, 150])
        self.toy_event = pg.USEREVENT
        pg.time.set_timer(self.toy_event, 2000)
        self.list_toys = []
        self.score = 0
    def draw(self):
        super().draw()
        self.dog.print(self.game.window)
        for i in self.list_toys:
            i.print(self.game.window)

    def logic(self):
        super().logic()
        self.dog.move()
        for i in self.list_toys:
            i.move()
        for i in self.list_toys:
            if i.hitbox2.colliderect(self.dog.hitbox):
                self.score = self.score + 1
                self.list_toys.remove(i)
                if self.game.happiness.counter < 100:
                    self.game.happiness.counter = self.game.happiness.counter + 1

        for i in self.list_toys:
            if i.hitbox2.bottom >= 650:
                self.list_toys.remove(i)

    def ft(self, event):
        super().ft(event)
        if event.type == self.toy_event:
            toy_object = classes.Toys()
            self.list_toys.append(toy_object)
