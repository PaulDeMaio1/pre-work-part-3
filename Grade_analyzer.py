scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

# This is to see where students scores fall based on their numerical score will be for a letter grade.
grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for score in scores:
    if score >= 90:
        grades["A"] += 1
    elif score >= 80:
        grades["B"] += 1
    elif score >= 70:
        grades["C"] += 1
    elif score >= 60:
        grades["D"] += 1
    else:
        grades["F"] += 1

#This is to determine the statistics of the test scores, and to determine what is and isnt a passing grade.
total = len(scores)
average = sum(scores) / total
highest = max(scores)
lowest = min(scores)
passing = grades["A"] + grades["B"] + grades["C"] + grades["D"]
failing = grades["F"]

# This is to print all the score statistics of the students.
print("=== Grade Analyzer ===")
print(f"Total scores: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Passing: {passing} ({passing / total * 100:.1f}%)")
print(f"Failing: {failing} ({failing / total * 100:.1f}%)")
#This is to list the score distribution of their letter grades based on their numerical scores.
print("\nGrade Distribution:")
for letter, count in grades.items():
    print(f"{letter}: {count} students")

# This is the "while loop" to allow the user to input additional scores 
print("\n--- Add More Scores ---")
while True:
    entry = input("Enter a score (or 'end' to finish): ").strip()

    if entry.lower() == "end":
        break

    try:
        new_score = float(entry)
    except ValueError:
        print("Please enter a valid number or 'end'.")
        continue

    if new_score < 0 or new_score > 100:
        print("Score must be between 0 and 100.")
        continue

    scores.append(new_score)
    print(f"Updated average: {sum(scores) / len(scores):.1f}")

print(f"\nFinal average: {sum(scores) / len(scores):.1f}")