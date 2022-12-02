# Parse the input data
calories = []
current_elf = []
for line in open('input/day1.txt'):
	line = line.strip()
	if line:
		current_elf.append(int(line))
	else:
		calories.append(current_elf)
		current_elf = []

# Find the top three Elves carrying the most Calories
calories_by_elf = [(sum(elf), i) for i, elf in enumerate(calories)]
calories_by_elf.sort(reverse=True)
total_calories = sum(sum(calories[i]) for _, i in calories_by_elf[:3])

# Find the Elf carrying the most Calories
max_calories, max_elf = calories_by_elf[0]

# Print the result
print(f"Elf {max_elf + 1} is carrying the most Calories: {max_calories}")
print(f"Top three Elves are carrying {total_calories} Calories")