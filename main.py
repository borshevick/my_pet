import pygame as pg
import setting
import dog
import buttons
import menu
import stats
import random
import json
import дз
import pygame.freetype as pgtype

class Game():
    def __init__(self):
        self.text_font = pgtype.Font("images/Acumin-ItPro_RUS.ttf", 50)
        file = open("saves.json", "r")
        self.file_read = json.load(file)
        self.game_over = False
        self.text_font = pgtype.Font("images/Acumin-ItPro_RUS.ttf", 20)
        self.window = pg.display.set_mode([setting.WINDOWX, setting.WINDOWY])
        self.fon = pg.image.load("images/background.png").convert_alpha()
        self.fon = pg.transform.scale(self.fon, [setting.WINDOWX, setting.WINDOWY])
        self.menufon = pg.image.load("images/menu/menu_page.png").convert_alpha()
        self.menufon = pg.transform.scale(self.menufon, [setting.WINDOWX, setting.WINDOWY])
        self.dog = dog.Dog([340, 175], [300, 400])
        self.food_button = buttons.Button("food", [200, 50], [10, 125], self.menufood)
        self.click_button = buttons.Button("Cliks", [200, 50], [10, 225], self.menuclicks)
        self.clothes_button = buttons.Button("clothes", [200, 50], [10, 325], self.menuclothes)
        self.minigame_button = buttons.Button("game", [200, 50], [10, 425], self.menuminigame)
        self.menu_game_picture = pg.image.load("images/game_background.png").convert_alpha()
        self.menu_game_picture = pg.transform.scale(self.menu_game_picture, [setting.WINDOWX, setting.WINDOWY])
        self.buttons = [self.food_button, self.click_button, self.clothes_button, self.minigame_button]
        self.clock = pg.time.Clock()
        self.menufoodobject = menu.MenuFood(self.menufon, self)
        self.menuclothesobject = menu.MenuClothes(self.menufon, self)
        self.menugameobject = menu.MenuMinigame(self.menu_game_picture, self)
        self.actualmenu = None
        self.happines_image = pg.image.load('images/happiness.png').convert_alpha()
        self.happines_image = pg.transform.scale(self.happines_image, [100, 100])
        self.happiness = stats.Stats([900, 400], self.happines_image, self.file_read["happines"])
        self.coins_image = pg.image.load('images/money.png').convert_alpha()
        self.coins_image = pg.transform.scale(self.coins_image, [100, 100])
        self.coins = stats.Stats([900, 300], self.coins_image, self.file_read["coins"])
        self.health_image = pg.image.load('images/health.png').convert_alpha()
        self.health_image = pg.transform.scale(self.health_image, [100, 100])
        self.health = stats.Stats([900, 200], self.health_image, self.file_read["health"])
        self.food_image = pg.image.load('images/satiety.png').convert_alpha()
        self.food_image = pg.transform.scale(self.food_image, [100, 100])
        self.food = stats.Stats([900, 100], self.food_image, self.file_read["food"])
        self.food_event = pg.USEREVENT+1
        self.bonus = self.file_read["bonus"]
        self.click = self.file_read["click"]
        pg.time.set_timer(self.food_event, random.randint(3000, 5000))
        self.happiness_event = pg.USEREVENT + 2
        pg.time.set_timer(self.happiness_event, random.randint(3000, 5000))
        self.health_event = pg.USEREVENT + 3
        pg.time.set_timer(self.health_event, random.randint(1000, 3000))
        self.auto_clicker_event = pg.USEREVENT + 4
        pg.time.set_timer(self.auto_clicker_event, 5000)

    def menufood(self):
        print('food')
        self.actualmenu = self.menufoodobject

    def menuclothes(self):
        print('clothes')
        self.actualmenu = self.menuclothesobject

    def menuminigame(self):
        print('gamme')
        self.actualmenu = self.menugameobject

    def menuclicks(self):
        print('click')
        for i in self.bonus:
            if self.bonus[i][0] == False and self.coins.counter >= int(i):
                self.coins.counter = self.coins.counter - int(i)
                self.click = self.bonus[i][1]
                self.bonus[i][0] = True
                break

    def run(self):
        while True:
            self.window.blit(self.fon, [0, 0])
            if self.actualmenu == None:
                self.event()
                self.update()
                self.draw()
            else:
                self.actualmenu.draw()
                self.actualmenu.logic()
                self.actualmenu.event()
            pg.display.flip()
            self.clock.tick(60)
            
    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                file = open("saves.json", "w")
                slovar = {"coins": self.coins.counter, "food": self.food.counter, "happines": self.happiness.counter, "health": self.health.counter, "clothes": self.menuclothesobject.slovari(), "bonus": self.bonus, "click": self.click}
                json.dump(slovar, file, indent=4)
                file.close()
                pg.quit()
                exit()
            if self.game_over == False:
                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in self.buttons:
                        if i.hitbox.collidepoint(event.pos):
                            i.click()
                    if self.dog.hitbox.collidepoint(event.pos):
                        self.coins.counter = self.coins.counter + self.click  
                if event.type == self.food_event and self.food.counter > 0:   
                    self.food.counter = self.food.counter - random.randint(1, 3) 
                    pg.time.set_timer(self.food_event, random.randint(1000, 3000))
                if event.type == self.happiness_event and self.happiness.counter > 0:   
                    self.happiness.counter = self.happiness.counter - random.randint(1, 3) 
                    pg.time.set_timer(self.happiness_event, random.randint(1000, 3000))
                if event.type == self.health_event and self.food.counter <= 20:  
                    self.health.counter = self.health.counter - random.randint(1, 3)
                if event.type == self.health_event and self.food.counter >= 70 and self.health.counter < 100:  
                    self.health.counter = self.health.counter + 1
                if event.type == self.auto_clicker_event:
                    self.coins.counter = self.coins.counter + self.click
                if self.food.counter <= 0:
                    self.game_over = True
                    self.health.counter = 0
            if self.game_over == True:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        self.__init__()

    def update(self):
        if self.game_over == False:
            for i in self.buttons:
                i.logic()
            if self.health.counter <= 0:
                дз.cp("saves copy.json", "saves.json")
                self.game_over = True

    def draw(self):
        for i in self.buttons:
            i.print(self.window)
        self.dog.print(self.window)
        self.happiness.print(self.window)
        self.coins.print(self.window)
        self.health.print(self.window)
        self.food.print(self.window)
        for i in self.menuclothesobject.clothing_obects:
            if i.wear == True: 
                i.print(self.window)
        if self.game_over == True:
            self.text_font.render_to(self.window, [500, 350], "GAME OVER, PRESS 'R' TO RESTART")
        for i in self.bonus:
            if self.bonus[i][0] == False:
                self.text_font.render_to(self.window, [self.click_button.txt_hitbox.right + 10, self.click_button.txt_hitbox.y], str(i))
                break

Mypet = Game()
Mypet.run()