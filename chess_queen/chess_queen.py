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

def flatten(array:list) -> list:
    """
    Returns flat list
    :param array: input chaotic array
    :return: flat list
    """
    list1 = []
    for i in array:
        if type(i) == list:
            list1.extend(flatten(i))
        else:
            list1.append(i)
    return list1

def check(board:list, r:int, c:int) -> bool:
    """
    Function that check if u can place queen on selected place
    :param board:
    :param r: raw
    :param c: column
    :return: True or False
    """
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
def do_it(raw:int, col:int) -> int:
    """
    Main function.
    :param raw: number of raws
    :param col: number of columns
    :return: number of solution
    """
    count = 0
    for j in range(raw):
        for k in range(col): #creating 64 boards with different start (0,0) (0,1) etc
            board = create_board(raw, col)
            board[j][k] = 1
            for i in range(raw):       #Checking availible place for placing queen from beggining of the board (0,0)
                for x in range(col):
                    if check(board, i, x):
                        board[i][x] = 1 #Place queen in the first availible spot
            # print(*board, sep='\n')
            # print('\n\n\n')
            if sum(flatten(board)) == 8:   #Printing board if amount of queen == 8.
                count += 1
                print(*board, sep='\n')
                print('\n\n\n')

    return count

print(do_it(8, 8))
# for j in range(8):
#     for k in range(8):
#         board = create_board(8, 8)
#         board[j][k] = 1
#         for i in range(len(board)):
#             for x in range(len(board[i])):
#                 if check(board, i, x):
#                     board[i][x] = 1
#         if sum(flatten(board)) == 8:
#             print(*board, sep='\n')
#             print('\n\n\n')
