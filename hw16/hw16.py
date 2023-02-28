import re


def chesboard_pattern(width, height):
    """chesboard = []
    for i in range(height):
        pattern = []
        for j in range(width):
            if i % 2 == 0:
                if j % 2 == 0:
                    pattern.append(0)
                else:
                    pattern.append(1)
            else:
                if j % 2 == 0:
                    pattern.append(1)
                else:
                    pattern.append(0)
        chesboard.append(pattern)
    return chesboard"""

    chessboard = []
    pattern = [0, 1]
    for i in range(height):
        if i % 2 == 0:
            if width % 2 == 0:
                raw = pattern * int(width / 2)
            else:
                raw = (pattern * int((width + 1) / 2))[:-1]
        else:
            if width % 2 == 0:
                raw = pattern[::-1] * int(width / 2)
            else:
                raw = (pattern[::-1] * int((width + 1) / 2))[:-1]
        chessboard.append(raw)
    return chessboard

assert chesboard_pattern(4, 4) == [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
assert chesboard_pattern(3, 3) == [[0, 1, 0], [1, 0, 1], [0, 1, 0]]


def inc_str(text):
    match = re.search(r'\d+$', text)
    if match:
        result = text[:-1] + str(int(match.group()[-1]) + 1)
    else:
        result = text + '1'
    return result


assert inc_str("foobar") == "foobar1"
assert inc_str("foobar0") == "foobar1"
assert inc_str("foobar00") == "foobar01"
assert inc_str("foobar00001") == "foobar00002"
assert inc_str("foobar0010") == "foobar0011"
assert inc_str("foobar00101") == "foobar00102"