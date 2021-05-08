amount = 83.65

values = [50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.50, 0.20, 0.10, 0.05]

units = []

for x in range(len(values)):
    if amount >= values[x]:
        units.append(values[x])
        amount -= values[x]

print(units)