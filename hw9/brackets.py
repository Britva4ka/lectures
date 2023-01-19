"""
перевірити коректнсть дужок.
"""
def brackets(string): #Достатньо легка задачка після підказок в лекції. Важкість 2/10. Цікава на 5-6/10
    stack = []
    for x in string:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

assert brackets("())")==False
assert brackets("())(")==False
assert brackets("(s(sss)sssssssssssssssssssssssssss)")==True