import random
from collections import defaultdict, deque
from math import floor


def topological_sort(graph):
    # Calculate in-degree for each node
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Add nodes with no incoming edges to queue
    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # Remove edges from node
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(graph):
        return None
    ret = {}
    for i in range(len(result)):
        ret[result[i]] = i
    return ret


def conform_to_rules(up, rules:dict[str,set]) -> bool:
    for i in range(len(up)-1):
        if up[i] in rules:
            forbidden_pages = rules[up[i]]
            for j in range(i+1, len(up)):
                if up[j] in forbidden_pages:
                    # print (f'{up} breaks rule {up[i]}|{forbidden_pages}')
                    return False
    return True


def fix_update(up, ordered_pages:dict[str,int]) -> list:
    return sorted(up, key=lambda x: ordered_pages[x])


def build_order_assuming_cyclic(forward_looking_edges: dict[str, set]) -> dict[str,int]:
    order: dict[str, int] = {}
    possible_roots = set()
    for page,consecutives in forward_looking_edges.items():
        possible_roots.add(page)
        for c in consecutives:
            possible_roots.add(c)


    while len(possible_roots) > 0:
        root = possible_roots.pop()
        fifo_queue = [root]
        already_seen = set()
        while len(fifo_queue) > 0:
            page = fifo_queue.pop(0)
            already_seen.add(page)
            if page in forward_looking_edges:
                for c in forward_looking_edges[page]:
                    if c not in already_seen:
                        possible_roots.discard(c)
                        fifo_queue.append(c)
        # print (possible_roots)


def has_cycle(forward_looking_edges: dict[str, set]) -> bool:
    visited = set()
    inPath = set()

    def is_cyclic_from_node(node):
        if node in inPath:
            return True
        if node in visited:
            return False

        visited.add(node)
        inPath.add(node)

        for next_node in forward_looking_edges[node]:
            if (next_node in forward_looking_edges and
                    is_cyclic_from_node(next_node)):
                return True

        inPath.remove(node)
        return False

    for node in list(forward_looking_edges.keys()):
        if node not in visited and node in forward_looking_edges:
            if is_cyclic_from_node(node):
                return True

    return False

def build_order_assuming_DAG(forward_looking_edges: dict[str, set]) -> dict[str,int]:
    failed_roots_candidates = defaultdict(int)
    for page, consecutives in forward_looking_edges.items():
        for c in consecutives:
            failed_roots_candidates[c] = 1
    roots = [ page for page in forward_looking_edges.keys() if page not in failed_roots_candidates]
    if not roots:
        print('No roots')
        return
    if has_cycle(forward_looking_edges):
        print('Has cycle')
        return

    order: dict[str, int] = defaultdict(int)
    fifo_queue = [] + roots
    iteration = 0
    while len(fifo_queue) > 0:
        iteration +=1
        # print (fifo_queue)
        page = fifo_queue.pop(0)
        # print(f'Processing {page}')
        if page in forward_looking_edges:
            for c in forward_looking_edges[page]:
                order[c] = order[page] + 1
                # print(f'Adding {c} to queue with order {order[c]}')
                fifo_queue.append(c)
    # print (f'Iterations {iteration}')
    return order


def extract_relevant_edges(up, forward_looking_edges: dict[str, set]):
    forward_looking_edges1: dict[str, set] = defaultdict(set)
    for page in up:
        if page in forward_looking_edges:
            for consecutive in forward_looking_edges[page]:
                if consecutive in up:
                    forward_looking_edges1[page].add(consecutive)
    return forward_looking_edges1


def run_1():
    # input = open('input/d5_sample', 'r')
    input = open('input/d5', 'r')
    lines = [l.strip() for l in input.readlines()]
    rules:dict[str,set]= defaultdict(set)
    forward_looking_edges: dict[str, set] = defaultdict(set)
    updates = []
    first_section = True
    for l in lines:
        if l.strip() == '':
            first_section = False
        else:
            if first_section:
                page1, page2 = l.split('|')
                rules[page2.strip()].add(page1.strip())
                forward_looking_edges[page1.strip()].add(page2.strip())
            else:
                pages = l.split(',')
                updates.append(pages)


    sum = 0
    sum2 = 0
    for up in updates:
        if not conform_to_rules(up, rules):
            forward_looking_edges1 = extract_relevant_edges(up, forward_looking_edges)
            # print(up)
            # ordered_pages: dict[str, int] = build_order_assuming_DAG(forward_looking_edges1)
            graph = complete_graph(forward_looking_edges1)
            ordered_pages: dict[str, int] = topological_sort(graph)
            corrected_update = fix_update(up, ordered_pages)
            # print(corrected_update)
            # print (f'Corrected {up} to {corrected_update}')
            mid_point = int(corrected_update[floor(len(corrected_update) / 2)])
            sum2 += mid_point


    for up in updates:
        if conform_to_rules(up, rules):
            sum += int(up[floor(len(up)/2)])


    print(sum)
    print(sum2)
    # wrong 6567


def run_2():
    # input = open('input/d5_sample', 'r')
    input = open('input/d5', 'r')
    lines = [l.strip() for l in input.readlines()]


def generate_random_forward_looking_edges():
    forward_looking_edges: dict[str, set] = defaultdict(set)
    for i in range(100):
        page1 = random.randint(1, 99)
        page2 = random.randint(page1+1, 100)
        forward_looking_edges[str(page1)].add(str(page2))
    return forward_looking_edges



def complete_graph(forward_looking_edges: dict[str, set]) -> dict[str, set]:
    ret:dict[str, set] = forward_looking_edges.copy()
    for page, consecutives in forward_looking_edges.items():
        for c in consecutives:
            if c not in forward_looking_edges:
                ret[c] = set()
    return ret

def run_tests():
    assert not conform_to_rules([61,13,29],{13:set([29])})
    forward_looking_edges: dict[str, set] = \
    {
        '1' : set(['2','3']),
        '2' : set(['3']),
    }
    order = build_order_assuming_DAG(forward_looking_edges)
    assert order['1'] == 0
    assert order['2'] == 1
    assert order['3'] == 2

    forward_looking_edges: dict[str, set] = \
    {
        'A' : set(['B','E']),
        'B' : set(['C']),
        'C' : set(['D']),
        'D' : set(['E']),
        'F' : set(['E']),
    }
    order = build_order_assuming_DAG(forward_looking_edges)
    # print(order)
    assert order['A'] == 0
    assert order['B'] == 1
    assert order['C'] == 2
    assert order['D'] == 3
    assert order['E'] == 4
    assert order['F'] == 0

    # forward_looking_edges = generate_random_forward_looking_edges()
    # print(forward_looking_edges)

    has_cycle_ = has_cycle(forward_looking_edges)
    assert not has_cycle_

    forward_looking_edges['E'] = set(['A'])
    has_cycle_ = has_cycle(forward_looking_edges)
    assert has_cycle_

    forward_looking_edges = {
        '27': {'19', '26', '34', '69', '87', '94'},
        '26': {'69', '94'},
        '19': {'26', '34', '69', '94'},
        '94': {'69'},
        '34': {'26', '69', '94'},
        '99': {'19', '25', '26', '27', '34', '69', '87', '94'},
        '87': {'19', '26', '34', '69', '94'},
        '25': {'19', '26', '27', '34', '69', '87', '94'}
    }
    graph = complete_graph(forward_looking_edges)

    order = topological_sort(graph)
    print(order)



if __name__ == "__main__":
    # run_tests()
    run_1()
    # run_2()
