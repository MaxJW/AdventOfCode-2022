score, score_p2 = 0, 0
for rucksack in open("input/day3.txt", "r"):
	common = ''.join(set(rucksack[:len(rucksack) // 2]).intersection(rucksack[len(rucksack) // 2:]))
	score += ord(common) - 38 if common.isupper() else ord(common) - 96
print(score)

teams = [line for line in open("input/day3.txt", "r").read().split("\n")]
for team in [teams[x:x+3] for x in range(0, len(teams),3)]:
	common = ''.join(set(set(team[0]).intersection(team[1])).intersection(team[2]))
	score_p2 += ord(common) - 38 if common.isupper() else ord(common) - 96
print(score_p2)