def valid_coourd(x, y, lines):
    return x >= 0 and y < len(lines) and x < len(lines[y]) and y >= 0


def extract_xmas(lines, x_, y_):
    x, y = x_, y_
    ret_found_occurances = []
    searched_str = 'XMAS'
    for dir in [(0, 1), (0, -1),
                (1, 1), (1, 0), (1, -1),
                (-1, -1), (-1, 0), (-1, 1)]:
        found_word = True
        for letter_index in range(0, len(searched_str)):
            if letter_index == 0:
                x = x_
                y = y_
            else:
                x += dir[0]
                y += dir[1]
                if not valid_coourd(x, y, lines) or lines[y][x] != searched_str[letter_index]:
                    found_word = False
                    break
        if found_word:
            ret_found_occurances.append((x_, y_, dir))
    return ret_found_occurances


def match_word(lines, x, y, d1, d2, searched_str):
    ret = False
    if ((valid_coourd(x + d1[0], y + d1[1], lines)
         and valid_coourd(x + d2[0], y + d2[1], lines))
            and lines[y + d1[1]][x + d1[0]] == searched_str[0]
            and lines[y + d2[1]][x + d2[0]] == searched_str[0]):
        if ((valid_coourd(x - d1[0], y - d1[1], lines)
             and valid_coourd(x - d2[0], y - d2[1], lines))
                and lines[y - d1[1]][x - d1[0]] == searched_str[1]
                and lines[y - d2[1]][x - d2[0]] == searched_str[1]):
            ret = True
    return ret


def extract_x_mas(lines, x, y):
    ret_found_occurances = []
    dirs1 = [(1, 1), (-1, -1)]
    dirs2 = [(-1, 1), (1, -1)]
    searched_str = 'MS'
    for d1 in dirs1:
        for d2 in dirs2:
            if match_word(lines, x, y, d1, d2, searched_str):
                ret_found_occurances.append((x, y, d1, d2))
    return ret_found_occurances


def run_1():
    # input = open('input/d4_sample', 'r')
    input = open('input/d4', 'r')
    lines = [l.strip() for l in input.readlines()]

    found_ocuurances = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == 'X':
                found_ocuurances += extract_xmas(lines, x, y)

    print(len(found_ocuurances))
    # for occurance in found_ocuurances:
    #     print(occurance)


def run_2():
    # input = open('input/d4_sample', 'r')
    input = open('input/d4', 'r')
    lines = [l.strip() for l in input.readlines()]

    found_ocuurances = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == 'A':
                found_ocuurances += extract_x_mas(lines, x, y)

    print(len(found_ocuurances))
    # for occurance in found_ocuurances:
    #     print(occurance)


def run_tests():
    input = open('input/d4_sample', 'r')
    lines = [l.strip() for l in input.readlines()]
    ret = extract_x_mas(lines, 7, 0)
    print(ret)



if __name__ == "__main__":
    # run_tests()
    # run_1()
    run_2()
