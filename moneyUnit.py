import pygame

class MoneyUnit:
    val = None
    picture = None
    drawPosition = None

    def __init__(self, value, picture):
        self.val = value
        self.picture = picture
    
    def draw(self, win, position):
        self.drawPosition = position
    #     self.drawPosition = (position[0] - (self.picture.get_width()/2), position[1])
        win.blit(self.picture, self.drawPosition)
    
    def isSelected(self, mousePos):
        if mousePos[0] > self.drawPosition[0] and mousePos[1] > self.drawPosition[1]:
            if mousePos[0] < (self.drawPosition[0] + self.picture.get_width()) and mousePos[1] < (self.drawPosition[1] + self.picture.get_height()):
                return True
            else:
                return False
        else:
            return False