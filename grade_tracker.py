"""Student grade report generator.

Reads data/students.csv, calculates student averages and letter grades,
prints a formatted summary report to the terminal, and saves it to a text file.
"""
# below is to include the csv and data structure of input and where to output data
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "data" / "students.csv"
OUTPUT_FILE = BASE_DIR / "output" / "report.txt"

NAME_COLUMN = "student_name"
GRADE_ORDER = ["A", "B", "C", "D", "F", "N/A"]


def load_students(filepath):
    """Read the CSV and return a list of dicts (one per student).

    Returns an empty list if the file does not exist.
    """
    #it will return an empty list so that the program does not crash
    try:
        with open(filepath, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Error: could not find '{filepath}'. Check the path and try again.")
        return []


def calculate_average(grades):
    """Return the average of valid grades, and will be rounded to 1 decimal place.

    Empty strings, None, and non-numeric values are ignored.
    Returns None if there are no valid grades.
    """
    # in order to insure the program doesnt crash listed above.
    valid = []
    for grade in grades:
        if grade is None:
            continue
        text = str(grade).strip()
        if not text:
            continue
        try:
            valid.append(float(text))
        except ValueError:
            continue  # will ignore any non numberic values

    if not valid:
        return None
    return round(sum(valid) / len(valid), 1)


def get_letter_grade(average):
    """Convert a numeric average to a letter grade, or 'N/A' if average is None."""
    if average is None:
        return "N/A"
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def generate_report(students):
    """Build a summary dict from the full student list.

    Keys:
        total_students, class_average, highest_average, lowest_average,
        grade_distribution, students (list of name/average/grade dicts)
    """
    results = []
    for student in students:
        grades = [value for key, value in student.items() if key != NAME_COLUMN]
        average = calculate_average(grades)
        results.append(
            {
                "name": (student.get(NAME_COLUMN) or "").strip(),
                "average": average,
                "grade": get_letter_grade(average),
            }
        )

    # Only students with minimum of one valid grade count toward class stats
    averages = [r["average"] for r in results if r["average"] is not None]
# below will include the for loop with the the different statistics that will be calculated and displayed in the report
    distribution = {grade: 0 for grade in GRADE_ORDER}
    for r in results:
        distribution[r["grade"]] += 1

    return {
        "total_students": len(results),
        "class_average": round(sum(averages) / len(averages), 1) if averages else None,
        "highest_average": max(averages) if averages else None,
        "lowest_average": min(averages) if averages else None,
        "grade_distribution": distribution,
        "students": results,
    }


def _fmt(value):
    """Format an average for display, showing 'N/A' when missing."""
    return "N/A" if value is None else f"{value:.1f}"


def format_report(report):
    """Build the report as a single string."""
    width = 44
    lines = [
        "=" * width,
        "STUDENT GRADE REPORT".center(width),
        "=" * width,
        "",
        "CLASS SUMMARY",
        "-" * width,
        f"Total students:   {report['total_students']}",
        f"Class average:    {_fmt(report['class_average'])}",
        f"Highest average:  {_fmt(report['highest_average'])}",
        f"Lowest average:   {_fmt(report['lowest_average'])}",
        "",
        "GRADE DISTRIBUTION",
        "-" * width,
    ]

    for grade in GRADE_ORDER:
        count = report["grade_distribution"][grade]
        lines.append(f"{grade:<4}{count:>3}  {'*' * count}")

    lines += [
        "",
        "INDIVIDUAL RESULTS",
        "-" * width,
        f"{'Name':<24}{'Average':>10}{'Grade':>8}",
    ]
# below will include the formatting of the report and destination of where the report will be saved to
    for r in report["students"]:
        lines.append(f"{r['name']:<24}{_fmt(r['average']):>10}{r['grade']:>8}")

    lines.append("=" * width)
    return "\n".join(lines) + "\n"


def write_report(report, filepath):
    """Write a formatted text report to filepath."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(format_report(report), encoding="utf-8")


def main():
    students = load_students(INPUT_FILE)
    if not students:
        return

    report = generate_report(students)
    print(format_report(report))
    write_report(report, OUTPUT_FILE)
    print(f"Report also saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()