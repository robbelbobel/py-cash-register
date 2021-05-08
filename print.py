import os
import sys
from datetime import date


datetoday = date.today()
cmdargs = sys.argv
cmdargs.pop(0)
isDummy = cmdargs.pop(len(cmdargs) - 1)
foodBtwAmount = cmdargs.pop(len(cmdargs) - 1)
alcoBtwAmount = cmdargs.pop(len(cmdargs) - 1)
softBtwAmount = cmdargs.pop(len(cmdargs) - 1)
btwamount = cmdargs.pop(len(cmdargs) - 1)
x=0
items = []
prices = []
for e in cmdargs:
	if x == 0 :
		items.append(e)
		x = 1
	elif x == 1 :
		prices.append(e)
		x = 0
os.system("lp -o fit-to-page -o portrait assets/bijzonder_pic.jpg")
total = float(0)
count = []
multiples = []
r = 0
while r < len(items):
	if items.count(items[r]) > 1:
	    if items[r] in multiples:
		    prices.pop(r)
		    items.pop(r)
	    else:
		    multiples.append(items[r])
		    count.append(items.count(items[r]))
		    r += 1
	
	elif items.count(items[r]) == 1:
		count.append(1)
		r += 1

#Calculate total price
for k in prices:
    total += float(k) * count[prices.index(k)]

#Remove underscores from item names
for k in items:
	items[items.index(k)] = k.replace("_", " ")

r = int(0)
postPrintString = "------------------\\n" + "Totaal: " + str(format(total, '.2f')) + "€\\n" + "Waarvan BTW: " + str(btwamount) + "€\n" + "6% BTW: " + str(float(softBtwAmount) + float(foodBtwAmount)) + "€\n" + "21% BTW: " + str(alcoBtwAmount) + "€\n" + "\nBTW: 0642.822.661\nCosta Hoppa\nBijzonder\nBroekstraat 31\n3300 Tienen\n" + str(datetoday) + "\n.\n.\n.\n."

if isDummy == True:
	postPrintString = "***WERKNEMER***" + postPrintString

orderPrintString = ""    
while x < len(items):
    orderPrintString += str(count[x]) + "x" + str(items[x]) + "-" + str(prices[x] + "€\\n")
    x += 1

os.system("echo \"" + orderPrintString + postPrintString + "\" |lp")

