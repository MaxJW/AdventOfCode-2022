fully_contained, partly_contained = 0, 0
for pair in [elves.split(",") for elves in open("input/day4.txt", "r").read().split("\n")]:
	range_1 = list(range(int((pair[0].split("-"))[0]), int((pair[0].split("-"))[1])+1))
	range_2 = list(range(int((pair[1].split("-"))[0]), int((pair[1].split("-"))[1])+1))
	fully_contained += set(range_1).issubset(range_2) or set(range_2).issubset(range_1)
	partly_contained += any(x in range_1 for x in range_2) or any(x in range_2 for x in range_1)
print(fully_contained, partly_contained)