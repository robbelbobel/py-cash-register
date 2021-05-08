import pygame
import math
from moneyUnit import MoneyUnit
from uiElement import UIElement

class ReturnMenu:
    MAIN_MENU = 0
    RETURN_MENU = 1

    moneyHeight = None
    UIHeight = None

    MoneyUnitList = []
    MoneyValueList = []
    UIElementList = []

    def __init__(self, MoneyUnitList):
        self.moneyHeight = 100
        self.UIHeight = 200
        self.MoneyUnitList = MoneyUnitList

        self.UIElementList.append(UIElement(self.scaleImage(pygame.image.load("assets/UI/next.jpg"), self.UIHeight), self.MAIN_MENU))

        for x in self.MoneyUnitList:
            self.MoneyValueList.append(x.val)
    
    def scaleImage(self, pic, resize_h):
        pic_width = pic.get_width()
        pic_height = pic.get_height()

        pic_resize_height = resize_h
        pic_resize_width = math.floor(pic_width / (pic_height/pic_resize_height))

        pic_resized = pygame.transform.smoothscale(pic, (pic_resize_width, pic_resize_height))

        return pic_resized
    
    def checkMouseSelection(self):
        mousePos = pygame.mouse.get_pos()
        
        for x in range(len(self.UIElementList)):
            if self.UIElementList[x].isSelected(mousePos):
                return self.UIElementList[x]

    def draw(self, win, amount, price, width, height):
        amount_abstr = amount - price

        units = []

        for x in range(len(self.MoneyUnitList)):
            while self.MoneyUnitList[x].val <= amount_abstr:
                units.append(self.MoneyUnitList[x])
                amount_abstr -= self.MoneyUnitList[x].val
        

        l = 0
        # Draw the money
        for x in units:
            x.draw(win, (width/4 + ((height/2) * (l%2)), (height / (math.ceil(len(self.MoneyUnitList) / 2))) * (math.floor(l/2))))
            l += 1
        
        for x in range(len(self.UIElementList)):
            self.UIElementList[x].draw(win, (width - self.UIHeight, height - self.UIHeight))
        