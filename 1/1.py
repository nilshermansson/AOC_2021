f = open('input.txt')
lines = f.read().split()
lines = list(map(int, lines))
def problem1():
    res = 0
    for i in range (1, len(lines)):
        if lines[i] > lines[i - 1]:
            res += 1
    print(res)

def problem2():
    res_arr = [0 for x in range(len(lines) - 2)]
    for i in range(len(res_arr)):
        res_arr[i] = sum(lines[i:i+3])
    res = 0
    for i in range (1, len(res_arr)):
        if res_arr[i] > res_arr[i - 1]:
            res += 1
    print(res)

problem1()
problem2()