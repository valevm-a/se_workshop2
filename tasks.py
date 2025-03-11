import re


def task(value):
    if value == '':
        return 0

    custom_delimiter = None

    if value.startswith('//'):
        parts = value.split('\n', 1)
        delimiter_part = parts[0][2:]

        if delimiter_part.startswith('[') and delimiter_part.endswith(']'):
            custom_delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
        else:
            custom_delimiters = [delimiter_part]

        value = parts[1]
        re_pattern = "|".join(custom_delimiters)
        #re_pattern = '|'.join(map(re.escape, custom_delimiters)) ?
    else:
        re_pattern = r'[,\s\n]+'

    numbers = re.split(re_pattern, value)

    total = 0
    for number in numbers:
        if int(number) < 0:
            raise ValueError("No negative numbers!")
        if int(number) > 1000:
            continue

        total += int(number)

    return total
