scores_part1 = { "A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
scores_part2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
input = [game for game in open("input/day2.txt", "r").read().split("\n")]
input_score = [sum(scores_part1[round] for round in input), sum(scores_part2[round] for round in input)]
print(f"Part 1 Score: {input_score[0]}\nPart 2 Score: {input_score[1]}")