def readSequence(filename):
    with open(filename, "r") as file:
        line = file.readline()
    return [int(number) for number in line.split(",")]

def runProgram(sequence):
    for i in xrange(0, len(sequence), 4):
        if sequence[i] == 99:
            break
        elif sequence[i] == 1:
            j1, j2, k = sequence[i + 1], sequence[i + 2], sequence[i + 3]
            sequence[k] = sequence[j1] + sequence[j2]
        elif sequence[i] == 2:
            j1, j2, k = sequence[i + 1], sequence[i + 2], sequence[i + 3]
            sequence[k] = sequence[j1] * sequence[j2]
        else:
            raise Exception()

def solve(filename):
    sequence = readSequence(filename)
    sequence[1] = 12
    sequence[2] = 2
    runProgram(sequence)
    return sequence[0]

if __name__ == "__main__":
    print solve("day2/input.txt")
