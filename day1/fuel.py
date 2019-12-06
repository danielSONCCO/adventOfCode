def getFuel(x):
    fuel = x/3 - 2
    if fuel <= 0: return 0
    return fuel + getFuel(fuel)

def readMasses(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return [int(line) for line in lines]

def solve(filename):
    masses = readMasses(filename)
    return sum(getFuel(mass) for mass in masses)

if __name__ == "__main__":
    print solve("day1/input.txt")
