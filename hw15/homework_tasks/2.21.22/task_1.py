
"""
Переписати алгоритм щоб складність була менша за O(n**2)
"""
def chesboard_pattern(width, height):
    chesboard = []
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
    return chesboard

def inc_str(text):
    pass

assert inc_str("foobar") == "foobar1"
assert inc_str("foobar0") == "foobar1"
assert inc_str("foobar00") == "foobar01"
assert inc_str("foobar00001") == "foobar00002"
assert inc_str("foobar0010") == "foobar0011"
assert inc_str("foobar00101") == "foobar00102"