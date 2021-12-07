

def problem1():
    f = open('input.txt')
    crabs = f.read().split(',')
    crabs = [int(x) for x in crabs]
    res = None

    for i in range(len(crabs)):
        totalFuel = 0
        for crab in crabs:
            totalFuel += abs(crab - i)

        if res == None:
            res = totalFuel
        else:
            res = min(res, totalFuel)

    print(res)

def problem2():
    f = open('input.txt')
    crabs = f.read().split(',')
    crabs = [int(x) for x in crabs]
    res = None

    for i in range(len(crabs)):
        totalFuel = 0
        for crab in crabs:
            totalFuel += abs(crab - i) * (abs(crab - i) + 1) / 2
        if res == None:
            res = totalFuel
        else:
            res = min(res, totalFuel)
    print(int(res))

problem1()
problem2()