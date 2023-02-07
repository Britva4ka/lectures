def roman_to_decimal(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    for i in range(len(s)):
        if i > 0 and roman_values[s[i]] > roman_values[s[i - 1]]:
            decimal += roman_values[s[i]] - 2 * roman_values[s[i - 1]]
        else:
            decimal += roman_values[s[i]]
    return decimal

assert roman_to_decimal('XIV') == 14
assert roman_to_decimal('XXI') == 21