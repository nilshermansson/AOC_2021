def problem1():
    f = open('input.txt')
    lines = f.read().split('\n')
    res_arr = [[0 for x in range (1000)] for y in range (1000)]

    for i in range (len(lines)):
        line = lines[i]
        line = line.replace(' -> ', ',')
        line = line.replace('\n', '')
        line = line.split(',')
        line = [int(x) for x in line]
        lines[i] = line

    # Populate
    for line in lines:
        x1, y1, x2, y2 = (line[0], line[1], line[2], line[3])
        # Horizontal
        if y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                res_arr[i][y1] += 1
        # Vertical
        elif x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                res_arr[x1][i] += 1

    # Calc
    res = 0
    for line in res_arr:
        for vent in line:
            if vent >= 2:
                res += 1

    print(res)

            

            



def problem2():
    f = open('input.txt')
    lines = f.read().split('\n')
    res_arr = [[0 for x in range (1000)] for y in range (1000)]

    for i in range (len(lines)):
        line = lines[i]
        line = line.replace(' -> ', ',')
        line = line.replace('\n', '')
        line = line.split(',')
        line = [int(x) for x in line]
        lines[i] = line

    # Populate
    for line in lines:
        x1, y1, x2, y2 = (line[0], line[1], line[2], line[3])
        # Horizontal
        if y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                res_arr[i][y1] += 1
        # Vertical
        elif x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                res_arr[x1][i] += 1
        # Diagonal down slope
        elif x1 - y1 == x2 - y2:
            if x1 < x2:
                topx, topy, botx = x1, y1, x2
            else:
                topx, topy, botx = x2, y2, x1
            for i in range (botx - topx + 1):
                res_arr[topx + i][topy + i] += 1
        # Diagonal up slope
        elif x1 + y1 == x2 + y2:
            if x1 < x2:
                botx, boty, topx = x1, y1, x2
            else:
                botx, boty, topx = x2, y2, x1
            for i in range(topx - botx + 1):
                res_arr[botx + i][boty - i] += 1


    # Calc
    res = 0
    for line in res_arr:
        for vent in line:
            if vent >= 2:
                res += 1

    print(res)

problem1()
problem2()