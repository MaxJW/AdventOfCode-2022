calElf_input = sorted([sum(map(int, elf.split("\n"))) for elf in open("input/day1.txt", "r").read().split("\n\n")])
print(f"Top: {calElf_input[-1]}\nTop 3 Total: {sum(calElf_input[-3:])}")