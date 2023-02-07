def create_board(r:int, c:int) -> list:
    """
    creating board for chess
    :param r: raw amount
    :param c: columns amount
    :return: list with r elements with c elementes in each
    """
    board = []
    for cols in range(c):
        line = []
        for raw in range(r):
            line.append(0)
        board.append(line)
    return board

def flatten(array):
    list1 = []
    for i in array:
        if type(i) == list:
            list1.extend(flatten(i))
        else:
            list1.append(i)
    return list1

def check(board, r, c):
    #raws
    for element in board[r]:
        if element == 1:
            return False
    #cols
    for raw in board:
        if raw[c] == 1:
            return False
    #1st
    count = 0
    while r > 0 and c > 0:
        r -= 1
        c -= 1
        count += 1
        if board[r][c] == 1:
            return False
    r += count
    c += count
    count = 0
    while r < len(board)-1 and c < len(board[0])-1:
        r += 1
        c += 1
        count += 1
        if board[r][c] == 1:
            return False
    r -= count
    c -= count
    count = 0

    #2nd
    while r > 0 and c < len(board[0]) - 1:
        r -= 1
        c += 1
        count += 1
        if board[r][c] == 1:
            return False
    r += count
    c -= count
    count = 0
    while r < len(board) - 1 and c > 0:
        r += 1
        c -= 1
        count += 1
        if board[r][c] == 1:
            return False
    r -= count
    c += count
    return True

for j in range(8):
    for k in range(8):
        board = create_board(8, 8)
        board[j][k] = 1
        for i in range(len(board)):
            for x in range(len(board[i])):
                if check(board, i, x):
                    board[i][x] = 1
        if sum(flatten(board)) == 8:
            print(*board, sep='\n')
            print('\n\n\n')
        # print(*board, sep='\n')
        # print('\n\n\n')

# def do_it_bitch(board, r=0, c=0):
#     board[r][c] = 1
#     for i in range(len(board) - 1):
#         for x in range(len(board[i]) - 1):
#             if check(board, i, x):
#                 board[i][x] = 1
#
#             return board
#
# print(*do_it_bitch(board), sep='\n')

