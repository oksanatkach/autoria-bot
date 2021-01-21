transliteration_key = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
    'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'P': 7, 'R': 9,
    'S': 2, 'T': 3, 'U': 4, 'V': 5, 'W': 6, 'X': 7, 'Y': 8, 'Z': 9
}

weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]


def get_check_digit(vin_code):
    integers = []

    for ind, char in enumerate(vin_code):
        if ind == 8:
            integers.append(0)
        elif char.isdigit():
            integers.append(int(char) * weights[ind])
        else:
            if char in transliteration_key:
                integers.append(transliteration_key[char] * weights[ind])
            else:
                raise Exception('Invalid VIN!')

    integer_sum = sum(integers)
    divisor = integer_sum % 11
    check_digit = str(divisor) if divisor < 10 else 'X'

    return check_digit


def generate_variants(vin_code):
    variants = []
    for num in range(0, 10):
        vin_code_variant = vin_code[:11] + str(num) + vin_code[12:]
        check_digit = get_check_digit(vin_code_variant)
        variants.append(vin_code_variant[:8] + check_digit + vin_code_variant[9:])
    return variants


def generate_variants_longer(vin_code):
    variants = []
    for num in range(0, 10):
        vin_code_variant = vin_code[:11] + str(num) + vin_code[12:]
        check_digit = get_check_digit(vin_code_variant)
        variants.append(vin_code_variant[:8] + check_digit + vin_code_variant[9:])
    return variants

# for code in generate_variants('3VWF17ATхFMх31624'):
#     print(code)
