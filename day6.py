
def tuning(num):
	for input in open("input/day6.txt", "r").read().split("\n"):
		for x, code in enumerate([input[x:x+num] for x in range(len(input))]):
			if len(set(code)) == num:
				return x+num
print(f"Part 1: {tuning(4)}\nPart 2: {tuning(14)}")