# Really just gave up on this one, please don't look :<

f = open('input.txt')
numbers = f.readline().split(',')
f.readline()
boards = f.read().split('\n\n')
boards = list(map(lambda x: x.split('\n'), boards))
boards = [[x.split() for x in line] for line in boards]

def detect_winner() -> bool: 
    for board in boards:
        for i in range (5): 
            #rows
            if all(x == 'marked' for x in board[i]):
                return board
            #coulumns
            if all(x == 'marked' for x in [row[i] for row in board]):
                return board
    return False  


def problem1():
    # Find the winning board and mark numbers processed
    current_number = None
    winning_board = None
    while not winning_board:
        current_number = numbers.pop(0)
        for i in range(len(boards)):
            for j in range(len(boards[0])):
                for k in range(len(boards[0][0])):
                    if boards[i][j][k] == current_number:
                        boards[i][j][k] = 'marked'
        winning_board = detect_winner()

    # Calc result
    res = 0
    for line in winning_board:
        for num in line: 
            if num != 'marked':
                res += int(num)
    
    print(res * int(current_number))


def remove_winners():
    indexes_to_remove = set()
    for board_idx in range(len(boards)):
        for row_col_idx in range(5): 
            #rows
            if all(x == 'marked' for x in boards[board_idx][row_col_idx]):
                indexes_to_remove.add(board_idx)
            #coulumns
            if all(x == 'marked' for x in [row[row_col_idx] for row in boards[board_idx]]):
                indexes_to_remove.add(board_idx)
    for index in sorted(indexes_to_remove, reverse=True):
        if len(boards) > 1:
            del boards[index]
        else:
            res = boards[0]
            del boards[0]
            return res


def problem2():
    # Find the winning boards and remove them
    current_number = None
    losing_board = None
    while len(boards):
        current_number = numbers.pop(0)
        for i in range(len(boards)):
            for j in range(len(boards[0])):
                for k in range(len(boards[0][0])):
                    if boards[i][j][k] == current_number:
                        boards[i][j][k] = 'marked'
        losing_board = remove_winners()

    # Calc result
    res = 0
    for line in losing_board:
        for num in line: 
            if num != 'marked':
                res += int(num)
    
    print(res * int(current_number))

problem1()
f = open('input.txt')
numbers = f.readline().split(',')
f.readline()
boards = f.read().split('\n\n')
boards = list(map(lambda x: x.split('\n'), boards))
boards = [[x.split() for x in line] for line in boards]
problem2()