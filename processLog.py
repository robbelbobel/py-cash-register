#open log
f = open("log.txt", 'r')
#read log
logText = f.readlines()
#close log
f.close()

last = 0

splitLogs = []

indices = [0]

dates = []
dummyOrders = []
orderList = []
totalPrices = []
BTW21Prices = []
BTW6Prices = []

n = 0
for x in logText:
    if x == "@\n":
        indices.append(n + 1)
    n += 1

for x in range(0, len(indices) - 1):
    splitLogs.append(logText[indices[x] : indices[x+1] - 1])

for l in splitLogs:

    dummyMode = l[0][11:]
    if dummyMode == "False\n":
        dummyMode = False
    else:
        dummyMode = True

    date = l[1][0:10]
    orders = l[2 : len(l) - 3]
    totalPrice = l[len(l) - 3].strip("Total Price: \n")
    alcoBTW = l[len(l) - 2][10:].strip("\n")
    softBTW = l[len(l) - 1][9:].strip("\n")

    if date not in dates:
        dates.append(date)
        dummyOrders.append([])
        orderList.append([])
        totalPrices.append([])
        BTW21Prices.append([])
        BTW6Prices.append([])
    
    if dummyMode:
        dummyOrders[dates.index(date)].append(orders)
        orderList[dates.index(date)].append('')
    else:
        orderList[dates.index(date)].append(orders)
        dummyOrders[dates.index(date)].append('')

    totalPrices[dates.index(date)].append(totalPrice)
    BTW21Prices[dates.index(date)].append(alcoBTW)
    BTW6Prices[dates.index(date)].append(softBTW)


f = open("dagKassa.txt", 'w')
f.truncate()
for l in dates:

    dummyOrderCounts = []
    orderCounts = []
    countedOrders = []
    countedDummyOrders = []
    
    dupes = []
    for p in dummyOrders[dates.index(l)]:
        for q in p:
            if q not in dupes:
                dummyOrderCounts.append(1)
                dupes.append(q)
                countedDummyOrders.append(q)
            else:
                dummyOrderCounts[dupes.index(q)] += 1

    dupes = []
    for p in orderList[dates.index(l)]:
        for q in p:
            if q not in dupes:
                orderCounts.append(1)
                dupes.append(q)
                countedOrders.append(q)
            else:
                orderCounts[dupes.index(q)] += 1

    f.write(str(l) + ":\n")
    f.write("Dummy Orders:\n")
    for p in countedDummyOrders:
        f.write(str(dummyOrderCounts[countedDummyOrders.index(p)]) + "x " + str(p))
    f.write("Orders:\n")
    for p in countedOrders:
        f.write(str(orderCounts[countedOrders.index(p)]) + "x " + str(p))
    tot = 0
    k = 0
    for p in totalPrices[dates.index(l)]:
        if dummyOrders[dates.index(l)][k] == '':
            tot += float(p)
        k += 1
    f.write("Total: " + str(tot) + "\n")
    tot = 0
    k = 0
    for p in BTW21Prices[dates.index(l)]:
        if dummyOrders[dates.index(l)][k] == '':
            tot += float(p)
        k += 1
    f.write("Total(21%): " + str(tot) + "\n")
    tot = 0
    k = 0
    for p in BTW6Prices[dates.index(l)]:
        if dummyOrders[dates.index(l)][k] == '':
            tot += float(p)
        k += 1
    f.write("Total(6%): " + str(tot) + "\n")
    f.write("\n")

f.close()
