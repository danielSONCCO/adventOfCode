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

# 368640*a + b + 521344
def runChangedProgram(sequence, a, b):
    copy = list(sequence)
    copy[1], copy[2] = a, b
    runProgram(copy)
    return copy[0]

def solve(filename):
    sequence = readSequence(filename)
    return runChangedProgram(sequence, 12, 2)

if __name__ == "__main__":
    res = solve("day2/input.txt")
    print res
