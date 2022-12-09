def calc(curr, list):
	trees = 0
	for tree in list:
		trees += 1
		if curr <= tree:
			break
	return trees

grid = [list(map(int, line)) for line in open("input/day8.txt").read().split("\n")]
num_trees_visible, viewing_distances = 0, []
for x, row in enumerate(grid):
	for y, col in enumerate(row):
		if x == 0 or y == 0 or x == len(grid)-1 or y == len(row)-1 or col > max(row[:y]) or col > max(row[y+1:]) or col > max([row[y] for row in grid[:x]]) or col > max([row[y] for row in grid[x+1:]]):
			num_trees_visible += 1
		left = calc(col, reversed(row[:y]))
		right = calc(col, row[y+1:])
		up = calc(col, reversed([row[y] for row in grid[:x]]))
		down = calc(col, [row[y] for row in grid[x+1:]])
		viewing_distances.append(left*right*up*down)
print(f"Part 1: {num_trees_visible}\nPart 2: {max(viewing_distances)}")