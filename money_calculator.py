import sys
import pygame
import math
from startMenu import StartMenu
from returnMenu import ReturnMenu
from uiElement import UIElement
from moneyUnit import MoneyUnit

pygame.init()

width = 1028
height = 720

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Money System")
pygame.display.toggle_fullscreen()

myFont = pygame.font.SysFont("Arial", 100)

startMenu = StartMenu()
returnMenu = ReturnMenu(startMenu.moneyUnitList)

amount = 0.0
price = float(sys.argv[1])

activeMenu = 0

running = True
while running:
    win.fill((150, 230, 170))
    
    if activeMenu == 0:
        startMenu.draw(win, myFont, amount, price, width, height)
    elif activeMenu == 1:
        returnMenu.draw(win, amount, price, width, height)

    #Poll events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            selection = None

            if activeMenu == 0:
                selection = startMenu.checkMouseSelection()
            elif activeMenu == 1:
                selection = returnMenu.checkMouseSelection()
            
            if selection is not None:
                if isinstance(selection, MoneyUnit) and activeMenu == 0: 
                    amount = round(amount + selection.val, 2)
                if isinstance(selection, UIElement):
                    if amount >= price:
                        if activeMenu == 1:
                            running = False
                        else:
                            activeMenu = selection.menu
    #update display
    pygame.display.flip()

pygame.quit()