def getFuel(x):
    fuel = x/3 - 2
    if fuel <= 0: return 0
    return fuel + getFuel(fuel)

textFile = open("input.txt", "r")
lines = textFile.readlines();
masses = [int(line) for line in lines]
print sum(getFuel(mass) for mass in masses)
