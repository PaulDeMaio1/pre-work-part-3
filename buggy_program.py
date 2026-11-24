
# first bug is listed below. Needed to add a colon after (number) in line 3. I was able to find this bug on my own and it is a syntax error.
def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count

    above_average = []
    for num in numbers:
        # second bug is listed below. the if num > average did not have a colon at the end of the line and was a syntax error. I used AI to assist in debugging this line.
        if num > average:
            above_average.append(num)

    return {
        "total": total,
        "average": average,
        "above_average": above_average,
        "above_count": len(above_average)
    }
# 3rd error was listen below. The 70 needed to be converted into an integer. I was able to see this on my own, and this was a data type error.
scores = [85, 92, 78, 95, 88, 70, 93]
result = calculate_stats(scores)

print(f"Total: {result['total']}")
# the fourth error was listed below. the result['average'] is the corrected version, there cannot be quotation marks and needs a bracket [ and ' symbol to be the correct variation. This was a name error, and I used AI to assist in this.
print(f"Average: {result['average']}")
print(f"Above average: {result['above_count']} scores")
