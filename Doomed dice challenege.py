#PART-A

# 1.Total Combinations
total_combinations = 6 * 6
print("Total Combinations:", total_combinations)

# 2.Distribution of all possible combinations
distribution_combinations= [[i + j for j in range(1, 7)] for i in range(1, 7)]

for row in distribution_combinations:
    print(row)
# 3.Probability of all Possible Sums
probability_sums = {}

for i in range(2, 13):
    count = sum(row.count(i) for row in distribution_combinations)
    probability = count / total_combinations
    probability_sums[i] = probability

print("Probability of Sums:")
for key, value in probability_sums.items():
    print(f"P(Sum = {key}) = {value:.4f}")


#PART-B
target = {
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 5,
    9: 4,
    10: 3,
    11: 2,
    12: 1
}

dieA = [1, 2, 3, 4, 0, 0]
dieB = [1, 3, 4, 5, 6, 0]


def validate_cur_combination():
    cur = {}
    for i in range(6):
        for j in range(6):
            if dieA[i] + dieB[j] in cur:
                cur[dieA[i] + dieB[j]] += 1
            else:
                cur[dieA[i] + dieB[j]] = 1
    return cur == target


def print_die():
    print("Die A is:", end=" ")
    print(*dieA)
    print("Die B is:", end=" ")
    print(*dieB)


def backtrack(curA, curB):
    if curA == 6 and curB == 6:
        if validate_cur_combination():
            print_die()
            exit(1)
        return

    for k in range(4):
        curAHit = k + 1
        for l in range(11):
            curBHit = l + 1
            dieA[curA] = curAHit
            dieB[curB] = curBHit
            backtrack(curA + 1, curB + 1)


if _name_ == "_main_":
    backtrack(4, 4)