class UIElement:
    picture = None
    drawPosition = None
    menu = None

    def __init__(self, picture, menu):
        self.picture = picture
        self.menu = menu

    def draw(self, win, position):
        self.drawPosition = position
        win.blit(self.picture, position)
    
    def isSelected(self, mousePos):
        if mousePos[0] > self.drawPosition[0] and mousePos[1] > self.drawPosition[1]:
            if mousePos[0] < (self.drawPosition[0] + self.picture.get_width()) and mousePos[1] < (self.drawPosition[1] + self.picture.get_height()):
                return True
            else:
                return False
        else:
            return False