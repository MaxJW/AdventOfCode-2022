(stacks, steps) = open('input/day5.txt').read().split("\n\n")
stacks = stacks.split("\n")[:-1]
stacks = [[level[i] for level in stacks if level[i] != ' '] for i in range(1, len(stacks[0]), 4)]
steps = [[int(step[1]), int(step[3]), int(step[5])] for step in map(str.split, steps.split("\n"))]

def move(multi):
    curr_stacks = [i[:] for i in stacks]
    for step in steps:
        num, prev, to = step
        curr = []
        for _ in range(num):
            curr.append(curr_stacks[prev-1].pop(0))
        if multi:
            curr = curr[::-1]
        for item in curr:
            curr_stacks[to-1].insert(0, item)

    for element in curr_stacks:
        print(element[0], end = '')
    print("\n")

move(True)
move(False)