import random


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def is_step_safe(x, y, dir):
    if sign(y - x) != dir or \
            abs(y - x) > 3:
        return False
    return True

def remove_at_index(lst, i):
    return lst[:i] + lst[i+1:]

def generate_random_report():
    r = list(range(1, 10))
    spot = random.randint(0, 9)
    n = random.randint(0, 9)
    r = r[:spot] + [n] + r[spot:]
    return r



def run_tests():
    assert is_report_safe([4, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert not is_report_safe([1, 2, 1, 1])
    assert is_report_safe([5, 1, 2, 3])
    assert is_report_safe([1, 2, 3])
    assert is_report_safe([3, 2, 1])
    assert is_report_safe([1, 2, 1])
    assert is_report_safe([3, 2, 4 , 5])

    for i in range(1000):
        r = generate_random_report()
        if not is_report_safe(r):
            print ("Should be safe")
            print(r)
            exit(1)

    print("All tests passed")

def is_report_safe(r,with_removal = True):
    is_report_safe_ = True
    dir = sign(r[1] - r[0])
    if dir == 0:
        is_report_safe_ = False
        i = 1
    else:
        for i in range(1, len(r)):
            if not is_step_safe(r[i - 1], r[i], dir):
                is_report_safe_ = False
                break
    if not is_report_safe_ and with_removal:
        is_report_safe_ = (is_report_safe(remove_at_index(r,i), False)
                          or is_report_safe(remove_at_index(r,i-1), False))
        if i == 2 and not is_report_safe_:
            is_report_safe_ = is_report_safe(remove_at_index(r,0), False)


    return is_report_safe_




def run_2():
    # input = open('input/d2_sample', 'r')
    input = open('input/d2', 'r')
    reports = []
    for line in input:
        reports.append([int(d.strip()) for d in line.split(' ') if d])

    safe_reports_counter = 0
    for r in reports:
        if is_report_safe(r):
            safe_reports_counter += 1

    print(safe_reports_counter)


if __name__ == "__main__":
    # run_tests()
    run_2()
