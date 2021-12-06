def problem1():
    f = open('input.txt')
    lanternFish = [int(fish) for fish in f.read().split(',')]


    for i in range(80):
        newFish = 0
        for i in range(len(lanternFish)):
            lanternFish[i] -= 1
            if lanternFish[i] == -1:
                newFish += 1
                lanternFish[i] = 6
        lanternFish += [8 for x in range(newFish)]

    print(len(lanternFish)) 
            
def problem2():
    f = open('input.txt')
    startFish = [int(fish) for fish in f.read().split(',')]
    fishArr = [0] * 9

    for fish in startFish:
        fishArr[fish] += 1

    for i in range(256):
        spawnedFish = fishArr.pop(0)
        fishArr[6] += spawnedFish
        fishArr += [spawnedFish]
    
    print(sum(fishArr))

    

problem1()
problem2()