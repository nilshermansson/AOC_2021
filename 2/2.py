f = open('input.txt')
lines = f.read().split('\n')

def problem1():
    hpos = vpos = 0
    for line in lines:
        if line.split()[0] == 'down':
            vpos += int(line.split()[1])
        elif line.split()[0] == 'forward':
            hpos += int(line.split()[1])
        elif line.split()[0] == 'up':
            vpos -= int(line.split()[1])
    print(vpos * hpos)


def problem2():
    hpos = vpos = aim = 0
    for line in lines:
        if line.split()[0] == 'down':
            aim += int(line.split()[1])
        elif line.split()[0] == 'forward':
            hpos += int(line.split()[1])
            vpos += aim * int(line.split()[1])
        elif line.split()[0] == 'up':
            aim -= int(line.split()[1])
    print(hpos * vpos) 

problem1()
problem2()
