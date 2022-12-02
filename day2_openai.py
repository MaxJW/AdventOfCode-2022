# This solution was written purely using ChatGPT by OpenAI - https://chat.openai.com/
# Note that this only solves part 1 of the advent challenge, but could be easily expanded upon

# Read the input from the file and split it into a list of tuples
opp_recs = [(x[0], x[2]) for x in open('input/day2.txt').read().split('\n') if x]

# Create dictionaries to map each move and outcome to a score
move_score  = {'X': 1, 'Y': 2, 'Z': 3}
outcome_score  = {'W': 6, 'D': 3, 'L': 0}

# Create a dictionary to map each move to the corresponding outcome
outcomes = {'A': {'X': 'D', 'Y': 'W', 'Z': 'L'}, 'B': {'X': 'L', 'Y': 'D', 'Z': 'W'}, 'C': {'X': 'W', 'Y': 'L', 'Z': 'D'}}

# Calculate your total score by summing the scores for each round
total_score = sum([move_score [rec] + outcome_score[outcomes[opp][rec]] for opp, rec in opp_recs])

# Print your total score
print(total_score)