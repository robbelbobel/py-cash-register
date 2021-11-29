import pygame
from pygame.locals import *
import math
import os
from datetime import date
from datetime import datetime
 
# test

def printOrders():
    global alco_totalBTW
    global soft_totalBTW
    global food_totalBTW
 
    global isBijzonder
 
    # print(orderList)
    printList = []
    printPrices = []
    printNames = []
    for x in orderList:
        printPrices.append(priceList[-x])
        printNames.append(nameList[-x])
    o = 0
    p = 0
    arraylength = len(printPrices) + len(printNames)
    while o < len(orderList):
        if(p == 0):
            printList.append(printNames[o])
            p = 1
 
        if(p == 1):
            printList.append(format(printPrices[o], '.2f'))
            p = 0
            o += 1
    printList.append(format(totalBTW, '.2f'))
    printString = ""
    s = 0
    for x in printList:
        if s == 0:
            printString = printString + str(x)
            s += 1
        elif s != 0:
            printString = printString + " " + str(x)
 
    btwString = str(format(round(soft_totalBTW, 2), '.2f')) + " " + str(format(round(alco_totalBTW, 2), '.2f')) + " " + str(format(food_totalBTW, '.2f'))
    os.system("python3 print.py " + printString + " " + btwString + " " + str(isBijzonder))
 
    logTotalPrice = 0
    for x in orderList:
        logTotalPrice += priceList[-x]
 
    #Write orders to log
    f = open("log.txt", 'a')
    logString = "werknemer: " + str(isBijzonder) + "\n" + str(datetime.now()) + ":\n"
    f.write(logString)
    for x in orderList:
        f.write(str(nameList[-x]) + " " + str(priceList[-x]) + "\n")
    f.write("Total Price: " + str(logTotalPrice) + "\n")
    f.write("BTW(21%): " + str(round(alco_totalBTW, 2)) + "\n")
    f.write("BTW(6%): " + str(round(soft_totalBTW, 2)) + "\n")
    f.write("@\n")
    f.close()
 
    isBijzonder = False
 
def blitDrinks(objnumX, objnumY, Drinks, DrinksID):
 
    x = 0
 
    while x < len(Drinks):
 
        placeX = x - (math.trunc(x/objnumX) * objnumX)
        placeY = math.trunc(x/objnumX)
 
        win.blit(Drinks[x], getCoordinates(Drinks[x], objnumX, objnumY, placeX, placeY, False, True, DrinksID[x])) #main_ID should be replaced with drinkID list in this function
 
        x += 1
 
def updatePrice(price):
 
    for x in orderList:
 
        price = price + priceList[-x]
 
 
    return price
 
def drawOrders(tBTW):
    #defining global BTW variables
    global alco_totalBTW
    global soft_totalBTW
    global food_totalBTW
 
    #check for doubles
    seen = []    
    doubles = []
 
    m = w_tot / 1000
 
    m_y = h_tot / 40
 
    num = 0
 
 
    for x in orderList:
        num += 1
 
        price = priceList[-x]

        if x in alcoDrinksID:
            btw = 21/100        # Alcohol BTW
            alco_totalBTW += price - (price / (1 + btw))
        elif x in softDrinksID:
            btw = 21/100         # Softdrinks BTW
            soft_totalBTW += price - (price / (1 + btw))
        else:
            btw = 12/100        # Food BTW
            food_totalBTW += price - (price / (1 + btw))
 
        tBTW += price - (price / (1 + btw))
 
        name = nameList[-x]
 
        x = w_tot - (w_tot - w) + m
 
        y = h_tot/100 + m_y * num
 
        t_name = sideFont.render(name + " *prijs: " + str(price) + " euro ", True,(255, 255, 255))
 
        win.blit(t_name, (x, y - (t_name.get_height())/2))
 
    return tBTW
 
def sideBar(totalBTW):
 
    x_rect = 5/6*w_tot
    y_rect = 0
 
    width_rect = 1/6*w_tot
    height_rect = h
 
    pygame.draw.rect(win, (0, 0, 0), (x_rect, y_rect, width_rect, height_rect))
 
    totalBTW = round(drawOrders(totalBTW), 2)
 
    t_totalPrice = sideFont.render("TOTALE PRIJS: " + str(totalPrice) + " euro", True, (255, 255, 255))
    t_totalBTW = sideFont.render("waarvan BTW: " + str(round(totalBTW, 2)) + " euro", True, (255, 255, 255))
 
    win.blit(t_totalPrice, (5/6 * w_tot, h - t_totalPrice.get_height() - t_totalBTW.get_height()))
    win.blit(t_totalBTW, (5/6 * w_tot, h- t_totalPrice.get_height()))
 
    return totalBTW
 
def checkOut():
    bg_ = pygame.transform.scale(bg, (int(w_tot), int(h)))
 
    win.blit(bg_, (0, 0))
 
    t_checkoutMenu = titelFont.render("Bevestigen", True, (255, 255, 255))
    t_totalPrice = myFont.render("Totale prijs: " + str(totalPrice) + "euro", True, (255, 255, 255))
    t_totalBTW = myFont.render("waarvan BTW: " + str(totalBTW) + "euro", True, (255, 255, 255))
 
    win.blit(t_checkoutMenu, (w/2 - (t_checkoutMenu.get_width()/2), 0))
    win.blit(t_totalPrice, (int(w_tot) - int(t_totalPrice.get_width()), int(h) - int(t_totalPrice.get_height()) - int(t_totalBTW.get_height())))
    win.blit(t_totalBTW, (int(w_tot) - int(t_totalBTW.get_width()), int(h) - int(t_totalBTW.get_height())))
 
    place=0
    last=0
    trig = 0
    renderY = 0
 
    for x in orderList:
        name = nameList[-x]
        price = priceList[-x]
        t_checkout_order = myFont.render(str(name)+ " " + str(price) + "€", True, (255, 255, 255))
 
        if renderY < h_tot and trig == 0:
 
            renderX = w_tot/20
 
            renderY = place*h_tot/10 + back.get_height()
 
            win.blit(t_checkout_order, (renderX, renderY))
 
            last = place
 
        if renderY > h_tot:
 
            trig = 1
 
            renderX = w_tot/3
 
            renderedY = (place - last)*h_tot/10  + t_checkoutMenu.get_height()
 
            win.blit(t_checkout_order, (renderX, renderedY))
 
        place = place + 1
 
    win.blit(back, getCoordinates(back, 10, 5, 0, 0, False, True, main_ID))
    win.blit(complete, getCoordinates(complete, 10, 5, 9, 0, False, True, complete_ID))
 
def hotMenu():
    win.blit(bg, (0, 0))
 
    hot_objnumX = 3
    hot_objnumY = 2
 
    blitDrinks(hot_objnumX, hot_objnumY, hotDrinks, hotDrinksID)
 
    # t_hotMenu = myFont.render("hotMenu", False, (255, 255, 255))
    # win.blit(t_hotMenu, getCoordinates(t_hotMenu, 1,1, 0, 0 ,True, False, 0))
 
def coldMenu():
    win.blit(bg, (0, 0))
 
    cold_objnumX = 5
    cold_objnumY = 4
 
    blitDrinks(cold_objnumX, cold_objnumY, softDrinks, softDrinksID)
 
    # t_coldMenu = myFont.render("coldMenu", False, (255, 255, 255))
    # win.blit(t_coldMenu, getCoordinates(t_coldMenu, 1,1, 0, 0 ,True, False, 0))
 
def alcoMenu():
    win.blit(bg, (0, 0))
 
    alco_objnumX = 6
    alco_objnumY = 3
 
    blitDrinks(alco_objnumX, alco_objnumY, alcoDrinks, alcoDrinksID)
 
def foodMenu():
    win.blit(bg, (0, 0))
 
    food_objnumX = 4
    food_objnumY = 2
 
    #win.blit(back, getCoordinates(back, food_objnumX, food_objnumY, 0, 0, False, False, main_ID))
    blitDrinks(food_objnumX, food_objnumY, food, foodID)
 
def buttonHandler(c_menu):
 
    mouse_pos = pygame.mouse.get_pos()
 
    l=0
 
    while l < len(buttons):
        if buttons[l] != None:
            button = buttons[l]
            #print(button[4])
            if button[5] == False or button[4] == main_ID:
                #print("3")
 
                if mouse_pos[0] > button[0] and mouse_pos[0] < button[0] + button[2]:
 
                   if mouse_pos[1] > button[1] and mouse_pos[1] < button[1] + button[3]:
                        #print("b4:" + str(button[4]))
                        return button[4]
 
            if button[5] == True and button[4] != main_ID:
 
                if mouse_pos[0] > button[0] and mouse_pos[0] < button[0] + button[2]:
 
                   if mouse_pos[1] > button[1] and mouse_pos[1] < button[1] + button[3]:
 
                       if button[4] == clear_ID or button[4] == delete_ID or button[4] == complete_ID or button[4] == bijzonder_ID:
                           return button[4]
                       else:
                           orderList.append(button[4])
 
        l += 1
    return c_menu
 
def mainMenu():
 
    win.blit(bg, (0,0))
 
    main_objNumX = 4
    main_objNumY = 2
 
    win.blit(hot_menu_pic, getCoordinates(hot_menu_pic, main_objNumX, main_objNumY, 0, 0, False, False, hot_ID))
    win.blit(soft_menu_pic, getCoordinates(soft_menu_pic, main_objNumX, main_objNumY, 1, 0, False, False, soft_ID))
    win.blit(alco_menu_pic, getCoordinates(alco_menu_pic, main_objNumX, main_objNumY, 2, 0, False, False, alco_ID))
    win.blit(food_menu_pic, getCoordinates(food_menu_pic, main_objNumX, main_objNumY, 3, 0, False, False, food_ID))
 
    win.blit(bijzonder_pic, getCoordinates(bijzonder_pic, main_objNumX, main_objNumY, 0, 1, False, True, bijzonder_ID))
    win.blit(clear, getCoordinates(clear, main_objNumX, main_objNumY, 1, 1, False, True, clear_ID))
    win.blit(delete, getCoordinates(delete, main_objNumX, main_objNumY, 2, 1, False, True, delete_ID))
    win.blit(checkout, getCoordinates(checkout, main_objNumX, main_objNumY, 3, 1, False, False, checkout_ID))
 
def getCoordinates(obj, objNumberX, objNumberY, placeX, placeY, isText, isDrink, ID):
 
    if isText == False:
 
        obj_width = obj.get_width()
        obj_height = obj.get_height()
 
        x = (w/objNumberX)/2 #midden van stuk
        x = x + placeX * w/objNumberX #add a place by adding place amount of times width divided by amount of spaces needed
        y = (h/objNumberY)/2
        y = y + placeY * h/objNumberY
        x -= obj_width/2
        y -= obj_height/2
 
        coord = [x, y, obj_width, obj_height, ID, isDrink]
 
        buttons.append(coord)
 
    if isText:
 
        m = 20
 
        x = (w/objNumberX)/2
 
        x = x + placeX * w/objNumberX
 
        y = (h/objNumberY)/2 + pic_y/2 + m
 
        y = y + placeY * h/objNumberY
 
        x -= obj.get_width()/2
 
    return (x, y)
 
pygame.init()
pygame.font.init()
 
w = 1920
h = 980
 
c_menu = 4
 
win = pygame.display.set_mode((w, h))
 
h_tot = h
w_tot = w
w -= w/6 # add black border to the right
 
pygame.display.set_caption("Kassa")
 
active = True
 
m_pic_x = int(w_tot/8)
m_pic_y = m_pic_x
 
pic_x = int(w_tot/5)
pic_y = pic_x
 
 
#Weird
buttons = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
 
#Alcoholic Drinks
cava = pygame.image.load("assets/alcohol/cava.png")
cava = pygame.transform.smoothscale(cava, (m_pic_x, m_pic_y))
cava_ID = -1
 
cava_fles = pygame.image.load("assets/alcohol/cava_fles.png")
cava_fles = pygame.transform.smoothscale(cava_fles, (m_pic_x, m_pic_y))
cava_fles_ID = -2
 
census = pygame.image.load("assets/alcohol/census.png")
census = pygame.transform.smoothscale(census, (m_pic_x, m_pic_y))
census_ID = -3
 
climax = pygame.image.load("assets/alcohol/climax.png")
climax = pygame.transform.smoothscale(climax, (m_pic_x, m_pic_y))
climax_ID = -4
 
hugo = pygame.image.load("assets/alcohol/hugo.png")
hugo = pygame.transform.smoothscale(hugo, (m_pic_x, m_pic_y))
hugo_ID = -5
 
bier_cocktail = pygame.image.load("assets/alcohol/cocktail.png")
bier_cocktail = pygame.transform.smoothscale(bier_cocktail, (m_pic_x, m_pic_y))
bier_cocktail_ID = -7
 
rose = pygame.image.load("assets/alcohol/rose.png")
rose = pygame.transform.smoothscale(rose, (m_pic_x, m_pic_y))
rose_ID = -8
 
rose_fles = pygame.image.load("assets/alcohol/rose_fles.png")
rose_fles = pygame.transform.smoothscale(rose_fles, (m_pic_x, m_pic_y))
rose_fles_ID = -9
 
r_wijn = pygame.image.load("assets/alcohol/r_wijn.png")
r_wijn = pygame.transform.smoothscale(r_wijn, (m_pic_x, m_pic_y))
r_wijn_ID = -10
 
r_wijn_fles = pygame.image.load("assets/alcohol/r_wijn_fles.png")
r_wijn_fles = pygame.transform.smoothscale(r_wijn_fles, (m_pic_x, m_pic_y))
r_wijn_fles_ID = -11
 
w_wijn = pygame.image.load("assets/alcohol/w_wijn.png")
w_wijn = pygame.transform.smoothscale(w_wijn, (m_pic_x, m_pic_y))
w_wijn_ID = -12
 
w_wijn_fles = pygame.image.load("assets/alcohol/w_wijn_fles.png")
w_wijn_fles = pygame.transform.smoothscale(w_wijn_fles, (m_pic_x, m_pic_y))
w_wijn_fles_ID = -13
 
club_mate = pygame.image.load("assets/soft_drinks/club_mate.jpeg")
club_mate = pygame.transform.smoothscale(club_mate, (m_pic_x, m_pic_y))
club_mate_ID = -14
 
fritz_kola = pygame.image.load("assets/soft_drinks/fritz_kola.png")
fritz_kola = pygame.transform.smoothscale(fritz_kola, (m_pic_x, m_pic_y))
fritz_kola_ID = -15
 
fritz_limo = pygame.image.load("assets/soft_drinks/fritz_limo.png")
fritz_limo = pygame.transform.smoothscale(fritz_limo, (m_pic_x, m_pic_y))
fritz_limo_ID = -16
 
fruitsap = pygame.image.load("assets/soft_drinks/fruitsap.png")
fruitsap = pygame.transform.smoothscale(fruitsap, (m_pic_x, m_pic_y))
fruitsap_ID = -17
 
koffie = pygame.image.load("assets/soft_drinks/koffie.png")
koffie = pygame.transform.smoothscale(koffie, (m_pic_x, m_pic_y))
koffie_ID = -18
 
thee = pygame.image.load("assets/soft_drinks/thee.png")
thee = pygame.transform.smoothscale(thee, (m_pic_x, m_pic_y))
thee_ID = -19
 
water = pygame.image.load("assets/soft_drinks/water.png")
water = pygame.transform.smoothscale(water, (m_pic_x, m_pic_y))
water_ID = -20
 
wostok = pygame.image.load("assets/soft_drinks/wostok.png")
wostok = pygame.transform.smoothscale(wostok, (m_pic_x, m_pic_y))
wostok_ID = -21
 
hugo_junior = pygame.image.load("assets/soft_drinks/hugo_junior.png")
hugo_junior = pygame.transform.smoothscale(hugo_junior, (m_pic_x, m_pic_y))
hugo_junior_ID = -22
 
chips = pygame.image.load("assets/food/chips.png")
chips = pygame.transform.smoothscale(chips, (m_pic_x, m_pic_y))
chips_ID = -24
 
chocomelk = pygame.image.load("assets/soft_drinks/chocomelk.png")
chocomelk = pygame.transform.smoothscale(chocomelk, (m_pic_x, m_pic_y))
chocomelk_ID = -25
 
confituur = pygame.image.load("assets/food/confituur.png")
confituur = pygame.transform.smoothscale(confituur, (m_pic_x, m_pic_y))
confituur_ID = -26
 
soep = pygame.image.load("assets/food/soep.png")
soep = pygame.transform.smoothscale(soep, (m_pic_x, m_pic_y))
soep_ID = -27
 
pancake = pygame.image.load("assets/food/pannenkoek.png")
pancake = pygame.transform.smoothscale(pancake, (m_pic_x, m_pic_y))
pancake_ID = -28
 
latte_macchiato = pygame.image.load("assets/soft_drinks/latte_macchiato.png")
latte_macchiato = pygame.transform.smoothscale(latte_macchiato, (m_pic_x, m_pic_y))
latte_macchiato_ID = -29
 
desperados = pygame.image.load("assets/alcohol/desperados.jpg")
desperados = pygame.transform.smoothscale(desperados, (m_pic_x, m_pic_y))
desperados_ID = -30
 
desperados_6 = pygame.image.load("assets/alcohol/desperados_6.jpg")
desperados_6 = pygame.transform.smoothscale(desperados_6, (m_pic_x, m_pic_y))
desperados_6_ID = -31
 
lokales = pygame.image.load("assets/alcohol/lokales.jpg")
lokales = pygame.transform.smoothscale(lokales, (m_pic_x, m_pic_y))
lokales_ID = -32
 
almdudler = pygame.image.load("assets/soft_drinks/almdudler.png")
almdudler = pygame.transform.smoothscale(almdudler, (m_pic_x, m_pic_y))
almdudler_ID = -33
 
cappucino = pygame.image.load("assets/soft_drinks/capuccino.png")
cappucino = pygame.transform.smoothscale(cappucino, (m_pic_x, m_pic_y))
cappucino_ID = -34
 
taart = pygame.image.load("assets/food/taart.png")
taart = pygame.transform.smoothscale(taart, (m_pic_x, m_pic_y))
taart_ID = -35
 
koffie_taart = pygame.image.load("assets/food/koffie_taart.png")
koffie_taart = pygame.transform.smoothscale(koffie_taart, (m_pic_x, m_pic_y))
koffie_taart_ID = -36

iced_latte = pygame.image.load("assets/soft_drinks/iced_latte.png")
iced_latte = pygame.transform.smoothscale(iced_latte, (m_pic_x, m_pic_y))
iced_latte_ID = -37

soep_liter = pygame.image.load("assets/food/soep_liter.png")
soep_liter = pygame.transform.smoothscale(soep_liter, (m_pic_x, m_pic_y))
soep_liter_ID = -38

spec_1 = pygame.image.load("assets/spec_1.png")
spec_1 = pygame.transform.smoothscale(spec_1, (m_pic_x, m_pic_y))
spec_1_ID = -39

spec_1_5 = pygame.image.load("assets/spec_1_5.png")
spec_1_5 = pygame.transform.smoothscale(spec_1_5, (m_pic_x, m_pic_y))
spec_1_5_ID = -40

spec_2 = pygame.image.load("assets/spec_2.png")
spec_2 = pygame.transform.smoothscale(spec_2, (m_pic_x, m_pic_y))
spec_2_ID = -41

spec_2_5 = pygame.image.load("assets/spec_2_5.png")
spec_2_5 = pygame.transform.smoothscale(spec_2_5, (m_pic_x, m_pic_y))
spec_2_5_ID = -42

spec_3 = pygame.image.load("assets/spec_3.png")
spec_3 = pygame.transform.smoothscale(spec_3, (m_pic_x, m_pic_y))
spec_3_ID = -43

spec_3_5 = pygame.image.load("assets/spec_3_5.png")
spec_3_5 = pygame.transform.smoothscale(spec_3_5, (m_pic_x, m_pic_y))
spec_3_5_ID = -44

spec_4 = pygame.image.load("assets/spec_4.png")
spec_4 = pygame.transform.smoothscale(spec_4, (m_pic_x, m_pic_y))
spec_4_ID = -45
 
spec_4_5 = pygame.image.load("assets/spec_4_5.png")
spec_4_5 = pygame.transform.smoothscale(spec_4_5, (m_pic_x, m_pic_y))
spec_4_5_ID = -46

spec_5 = pygame.image.load("assets/spec_5.png")
spec_5 = pygame.transform.smoothscale(spec_5, (m_pic_x, m_pic_y))
spec_5_ID = -47

delete = pygame.image.load("assets/delete.png")
delete = pygame.transform.smoothscale(delete, (pic_x, pic_y))
 
clear = pygame.image.load("assets/clear.png")
clear = pygame.transform.smoothscale(clear, (pic_x, pic_y))
 
hot_menu_pic = pygame.image.load("assets/hot_menu_pic.png")
hot_menu_pic = pygame.transform.smoothscale(hot_menu_pic, (pic_x, pic_y))
 
soft_menu_pic = pygame.image.load("assets/cold_menu_pic.png")
soft_menu_pic = pygame.transform.smoothscale(soft_menu_pic, (pic_x, pic_y))
 
alco_menu_pic = pygame.image.load("assets/alco_menu_pic.png")
alco_menu_pic = pygame.transform.smoothscale(alco_menu_pic, (pic_x, pic_y))
 
food_menu_pic = pygame.image.load("assets/food_menu_pic.png")
food_menu_pic = pygame.transform.smoothscale(food_menu_pic, (pic_x, pic_y))
 
bijzonder_pic = pygame.image.load("assets/bijzonder_pic.jpg")
bijzonder_pic = pygame.transform.smoothscale(bijzonder_pic, (pic_x, pic_y))
 
back = pygame.image.load("assets/back.png")
back = pygame.transform.smoothscale(back, (m_pic_x, m_pic_y))
 
checkout = pygame.image.load("assets/checkout.png")
checkout = pygame.transform.smoothscale(checkout, (pic_x, pic_y))
 
complete = pygame.image.load("assets/next.jpeg")
complete = pygame.transform.smoothscale(complete, (m_pic_x, m_pic_y))
 
#Fonts
 
sideFont = pygame.font.SysFont("Arial", 17)
myFont = pygame.font.SysFont("Arial", 30)
titelFont = pygame.font.SysFont("Arial", int(w_tot/15))
 
t_dummy = myFont.render("Bijzonder modus", True, (255, 255, 255))
 
bijzonder_ID = -300
delete_ID = -200
clear_ID = -100
complete_ID = -1000
hot_ID = 0
soft_ID = 1
food_ID = 2
alco_ID = 3
main_ID = 4
checkout_ID = 5 #Checkout ID
 
#Drink lists
alcoDrinks = [cava, cava_fles, census, climax, hugo, bier_cocktail, rose, rose_fles, r_wijn, r_wijn_fles, w_wijn, w_wijn_fles, desperados, desperados_6, lokales, back]
alcoDrinksID = [cava_ID, cava_fles_ID, census_ID, climax_ID, hugo_ID, bier_cocktail_ID, rose_ID, rose_fles_ID,r_wijn_ID, r_wijn_fles_ID, w_wijn_ID, w_wijn_fles_ID, desperados_ID, desperados_6_ID, lokales_ID, main_ID]
 
softDrinks = [club_mate, fritz_kola, fritz_limo, fruitsap, water, wostok, hugo_junior, almdudler, iced_latte, spec_1, spec_1_5, spec_2, spec_2_5, spec_3, spec_3_5, spec_4, spec_4_5, spec_5, back]
softDrinksID =[club_mate_ID, fritz_kola_ID, fritz_limo_ID, fruitsap_ID, water_ID, wostok_ID, hugo_junior_ID, almdudler_ID, iced_latte_ID, spec_1_ID, spec_1_5_ID, spec_2_ID, spec_2_5_ID, spec_3_ID, spec_3_5_ID, spec_4_ID, spec_4_5_ID, spec_5_ID, main_ID]
 
hotDrinks = [koffie, thee, chocomelk, latte_macchiato, cappucino, back]
hotDrinksID = [koffie_ID, thee_ID, chocomelk_ID, latte_macchiato_ID, cappucino_ID, main_ID]
 
food = [chips, confituur, soep, pancake, taart, koffie_taart, soep_liter, back]
foodID = [chips_ID, confituur_ID, soep_ID, pancake_ID, taart_ID, koffie_taart_ID, soep_liter_ID, main_ID]
 
checkOutButtons = [back, complete]
 
orderList = []
priceList = [None, 4.50, 18.00, 3.50, 3.50, 7.00, 8.00, 8.00, 3.50, 16.00, 3.50, 16.00, 3.50, 16.00, 3.00, 3.00, 3.00, 2.50, 2.50, 2.50, 2.50, 3.00, 5.00, 2.50, 2.50, 2.50, 2.00, 4.00, 2.00, 3.00, 4.50, 22.50, 4.50, 3.00, 3.00, 3.00, 5.00, 4.00, 5.00, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00]
nameList = [None, "Cava", "Cava_Fles", "Census", "Climax", "Hugo", "NA", "bier_cocktail", "Rose", "Rose_Fles", "Rode_Wijn", "R_Wijn_Fl", "Witte_Wijn", "W_Wijn_Fl", "Club_Mate", "Fritz_Kola", "Fritz_Limo", "Fruitsap", "Koffie", "Thee", "Water", "Wostok" , "Hugo_Jr.", "NA", "Chips", "Chocomelk", "Confituur", "Soep", "Pannenkoek", "Latte", "Desperados", "Desperados_5+1", "Lokales", "almdudler", "cappuccino", "taart", "koff_taart", "iced_latte", "soep_liter", "spec_1", "spec_1_5", "spec_2", "spec_2_5", "spec_3", "spec_3_5", "spec_4", "spec_4_5", "spec_5"]
 
bg = pygame.image.load("assets/bg.jpeg")
bg = pygame.transform.scale(bg, (int(w), int(h)))
 
#Total BTW variables
totalBTW = 0
global alco_totalBTW
global soft_totalBTW
global food_totalBTW
 
alco_totalBTW = 0
soft_totalBTW = 0
food_totalBTW = 0
 
global isBijzonder
isBijzonder = False
 
while active:    
    totalPrice = 0
    totalPrice = updatePrice(totalPrice)
 
    #print(orderList)
 
    del buttons
    buttons = []
 
    #print(c_menu)
 
    win.fill((255,255,255))
 
    if c_menu == main_ID:
        mainMenu()
    if c_menu == hot_ID:
        hotMenu()
    if c_menu == soft_ID:
        coldMenu()
    if c_menu == alco_ID:
        alcoMenu()
    if c_menu == food_ID:
        foodMenu()
    if c_menu == checkout_ID:
        checkOut()
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                isBijzonder = not isBijzonder
        if event.type == pygame.MOUSEBUTTONDOWN:
 
            #print("clicked")
 
            i = buttonHandler(c_menu)
 
            # print ("i:" + str(i))
 
            if i < 0 :
                if i == bijzonder_ID:
                    isBijzonder = not isBijzonder
 
                if i == delete_ID and len(orderList) != 0:
                    del orderList[len(orderList)-1]
 
                if i == clear_ID :
                    orderList = []
 
                if i == complete_ID:
                    if not isBijzonder:
                        printOrders()
 
                    orderList = []
                    c_menu = main_ID
 
            else:
                # if i == checkout_ID and isBijzonder == False and c_menu != checkout_ID:
                #     os.system("python3 money_calculator.py " + str(totalPrice))
                c_menu = i
    if c_menu != checkout_ID:
        totalBTW = 0
        alco_totalBTW = 0
        soft_totalBTW = 0
        food_totalBTW = 0
        totalBTW = sideBar(totalBTW)
    pygame.time.delay(100)
 
    # print("alco BTW: " + str(alco_totalBTW) + "\n")
    # print("soft BTW: " + str(soft_totalBTW) + "\n")
 
    if(isBijzonder):
        win.blit(t_dummy, (0,0))
 
    pygame.display.update()
 
pygame.quit()