import pygame
import math
from moneyUnit import MoneyUnit
from uiElement import UIElement

MAIN_MENU = 0
RETURN_MENU = 1

class StartMenu:
    moneyUnitList = []
    UIElementList = []

    moneyHeight = None
    UIHeight = None

    def __init__(self):
        self.moneyHeight = 100
        self.UIHeight = 200

        self.moneyUnitList.append(MoneyUnit(10.0, self.scaleImage(pygame.image.load("assets/money/euro_10.jpg"), self.moneyHeight)))
        self.moneyUnitList.append(MoneyUnit(5.0, self.scaleImage(pygame.image.load("assets/money/euro_5.png"), self.moneyHeight)))
        self.moneyUnitList.append(MoneyUnit(2.0, self.scaleImage(pygame.image.load("assets/money/euro_2.jpg"), self.moneyHeight)))
        self.moneyUnitList.append(MoneyUnit(1.0, self.scaleImage(pygame.image.load("assets/money/euro_1.png"), self.moneyHeight)))
        self.moneyUnitList.append(MoneyUnit(0.50, self.scaleImage(pygame.image.load("assets/money/cent_50.jpg"), self.moneyHeight)))
        self.moneyUnitList.append(MoneyUnit(0.20, self.scaleImage(pygame.image.load("assets/money/cent_20.jpg"), self.moneyHeight)))
        self.moneyUnitList.append(MoneyUnit(0.10, self.scaleImage(pygame.image.load("assets/money/cent_10.jpg"), self.moneyHeight)))
        self.moneyUnitList.append(MoneyUnit(0.05, self.scaleImage(pygame.image.load("assets/money/cent_5.jpg"), self.moneyHeight)))
        
        

        self.UIElementList.append(UIElement(self.scaleImage(pygame.image.load("assets/UI/next.jpg"), self.UIHeight), RETURN_MENU))
    
    def scaleImage(self, pic, resize_h):
        pic_width = pic.get_width()
        pic_height = pic.get_height()

        pic_resize_height = resize_h
        pic_resize_width = math.floor(pic_width / (pic_height/pic_resize_height))

        pic_resized = pygame.transform.smoothscale(pic, (pic_resize_width, pic_resize_height))

        return pic_resized

    def drawMoney(self, win, width, height):
        for x in range(len(self.moneyUnitList)):
            self.moneyUnitList[x].draw(win, (width/4 + ((height/2) * (x%2)), (height / (math.ceil(len(self.moneyUnitList) / 2))) * (math.floor(x/2))))

    def drawUI(self, win, myFont, amount, price, width, height):
        win.blit(myFont.render(str(amount), True, (0, 0, 0)), (0, 0))
        priceRender = myFont.render(str(price), True, (0, 0, 0))
        win.blit(priceRender, (width - priceRender.get_width(), 0))

        for x in range(len(self.UIElementList)):
            self.UIElementList[x].draw(win, (width - self.UIHeight, height - self.UIHeight))
    
    def draw(self, win, myFont, amount, price, width, height):
        self.drawMoney(win, width, height)
        self.drawUI(win, myFont, amount, price, width, height)

    def checkMouseSelection(self):
        mousePos = pygame.mouse.get_pos()

        for x in range(len(self.moneyUnitList)):
            if self.moneyUnitList[x].isSelected(mousePos):
                return self.moneyUnitList[x]
        for x in range(len(self.UIElementList)):
            if self.UIElementList[x].isSelected(mousePos):
                return self.UIElementList[x]
        return None