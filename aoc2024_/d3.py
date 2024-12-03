import re


def run_1():
    # input = open('input/d3_sample', 'r')
    input = open('input/d3', 'r')
    s = input.read()
    pattern1 = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
    muls = re.findall(pattern1, s)
    sum_ = 0
    for mul in muls:
        operands1, operands2 = mul[4:-1].split(',')
        sum_ += int(operands1) * int(operands2)

    print(sum_)


def interweave_lists(list1, list2):
    combined_list = list1 + list2
    combined_list.sort(key=lambda x: x[0])
    return combined_list


def run_2():
    # input = open('input/d3_sample', 'r')
    input = open('input/d3', 'r')
    s = input.read()
    pattern1 = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
    pattern2 = r'do\(\)'
    pattern3 = r"don't\(\)"
    muls = [(match.start(), match.group(), 'mul') for match in re.finditer(pattern1, s)]
    dos = [(match.start(),match.group(), 'do') for match in re.finditer(pattern2, s)]
    donts = [(match.start(),match.group(), 'dont') for match in re.finditer(pattern3, s)]
    instructions = interweave_lists(muls, interweave_lists(dos, donts))
    sum_ = 0
    peform = True
    for ind, instruction,  type in instructions:
        print(instruction, ind, type)
        if type == 'mul':
            if peform:
                operands1, operands2 = instruction[4:-1].split(',')
                sum_ += int(operands1) * int(operands2)
        elif type == 'dont':
            peform = False
        elif type == 'do':
            peform = True
        else:
            raise ValueError(f'Unknown type: ' + type)

    print(sum_)


if __name__ == "__main__":
    # run_tests()
    # run_1()
    run_2()
