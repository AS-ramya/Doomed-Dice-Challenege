import itertools

# Part-A
# 1. Total combinations
total_combinations = 6 * 6  # Two six-sided dice
print("Total Combinations:", total_combinations)

# 2. Distribution of all possible combinations
combinations = list(itertools.product(range(1, 7), repeat=2))
print("Distribution of Combinations:")
for combo in combinations:
    print(combo)

# 3. Probability of all Possible Sums
sum_probabilities = {}
for combo in combinations:
    total = sum(combo)
    if total not in sum_probabilities:
        sum_probabilities[total] = 1
    else:
        sum_probabilities[total] += 1

print("Probability of Sums:")
for key, value in sum_probabilities.items():
    probability = value / total_combinations
    print(f"P(Sum = {key}) = {probability:.4f}")
# Part-B
def undoom_dice(Die_A, Die_B):
    # Helper function to calculate the probability of a sum given dice
    def calculate_probability(dice):
        total_combinations = len(dice) * len(dice[0])
        sum_probabilities = {}
        for combo in itertools.product(*dice):
            total = sum(combo)
            if total not in sum_probabilities:
                sum_probabilities[total] = 1
            else:
                sum_probabilities[total] += 1

        return {key: value / total_combinations for key, value in sum_probabilities.items()}

    # Calculate the original probabilities
    original_probabilities = calculate_probability([Die_A, Die_B])

    New_Die_A = [min(4, x) for x in Die_A]  # Restrict Die_A to have no more than 4 spots
    New_Die_B = Die_B  # Die_B can have as many spots as necessary

    # Calculate the new probabilities
    new_probabilities = calculate_probability([New_Die_A, New_Die_B])

    # Output the new dice
    return New_Die_A, New_Die_B

Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]
New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)

print("Original Dice A:", Die_A)
print("Original Dice B:", Die_B)
print("New Dice A:", New_Die_A)
print("New Dice B:", New_Die_B)