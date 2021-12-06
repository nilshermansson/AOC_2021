f = open('input.txt')
lines = f.read().split()

def problem1():
    res_arr = [0 for x in range(len(lines[0]))]
    for line in lines:
        for index in range(len(line)):
            res_arr[index] += int(line[index])
    res_arr = list(map(lambda x: x / len(lines), res_arr))
    gamma = list(map(round, res_arr))
    epsilon = [1 if x == 0 else 0 for x in gamma]
    gamma = int("".join(str(i) for i in gamma),2)
    epsilon = int("".join(str(i) for i in epsilon),2)

    print(gamma * epsilon)


def problem2():
    oxygen = lines.copy()
    current_index = 0
    while len(oxygen) > 1: 
        ones = len([1 for line in oxygen if line[current_index] == '1'])
        zeros = len(oxygen) - ones

        most_common = '1' if ones >= zeros else '0'

        oxygen = [line for line in oxygen if line[current_index] == most_common]
        current_index += 1

    co2 = lines.copy()
    current_index = 0
    while len(co2) > 1:
        ones = len([1 for line in co2 if line[current_index] == '1'])
        zeros = len(co2) - ones

        least_common = '0' if zeros <= ones else '1'

        co2 = [line for line in co2 if line[current_index] == least_common]
        current_index += 1

    oxygen_int = int(oxygen[0], 2)
    co2_int = int(co2[0], 2)
    print(oxygen_int * co2_int)
problem1()
problem2()
