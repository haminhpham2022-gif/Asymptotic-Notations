names = ["Steve", "Maria", "Will", "Daria", "Trent"]
score = [64, 78, 24, 57, 100]
n = len(score)

print(f"'=== Score Tracker (n = {n}, Players) ===")
for i in range(n):
    print(f"{i + 1}. {names[i]} : {score[i]}")
print()

print("=================")

print()
step = 1
print(f"score at index 0: {score[0]} | steps = {step} | Theta(1) - tight bound")
print()
print("=================")

target = "Maria"
steps = 0

for name in names:
    steps += 1
    if name == target:
        break
print()
print(f"Found {target} at index {names.index(name)} | steps = {step} | Omega(n) - lower bound")
print()
print("=================")

steps = 0
target_sum = 150
print("Pairs with sum of less than or equal to 150:")
for i in range(n):
    for j in range(i+1,n):
        steps += 1
        if score[i] + score[j]<=target_sum:
            print(f"{names[i]} + {names[j]} = {score[i]} + {score[j]}")
print(f"Total comparisons: {steps} | O(n^2)")