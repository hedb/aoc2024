from collections import defaultdict

l1, l2 = [], []
# input = open('input/d1_sample', 'r')
input = open('input/d1', 'r')
for line in input:
    vals = [int(d.strip()) for d in line.split(' ') if d]
    l1.append(vals[0])
    l2.append(vals[1])

l1.sort()
l2.sort()

sum_ = 0
for i in range(len(l1)):
    sum_ += abs(l1[i] - l2[i])

# assert sum_ == 2580760

counters = defaultdict(int)
for i in range(len(l2)):
    counters[l2[i]] += 1

sum = 0
for i in range(len(l1)):
    sum += l1[i]*counters[l1[i]]

print(sum)

