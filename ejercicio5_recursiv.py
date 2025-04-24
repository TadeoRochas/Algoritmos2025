#libreria
roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def romano_a_decimal(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}

    if len(s) == 0:
        return 0
    if len(s) == 1:
        return roman_values[s[0]]
    
    #compara el valor actual con el siguiente
    if roman_values[s[0]] < roman_values[s[1]]:
        # Ej: IV → 5 - 1 = 4
        return roman_values[s[1]] - roman_values[s[0]] + romano_a_decimal(s[2:])
    else:
        return roman_values[s[0]] + romano_a_decimal(s[1:])

print(romano_a_decimal("XIV"))   # 14
print(romano_a_decimal("XXII"))    # 22
print(romano_a_decimal("MCMXCIV"))  # 1994
