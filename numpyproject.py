"""
╔══════════════════════════════════════════════════════╗
║        Student Performance Analyzer                  ║
║        Built with NumPy | By Muhammad Talha          ║
║        University of Peshawar | AI Semester 2        ║
╚══════════════════════════════════════════════════════╝
"""

import numpy as np
import os
from datetime import datetime


# ── Constants ─────────────────────────────────────────────
PASS_MARK    = 50
REPORT_FILE  = "student_report.txt"
DIVIDER      = "=" * 55
THIN_DIV     = "-" * 55


# ══════════════════════════════════════════════════════════
# INPUT FUNCTIONS
# ══════════════════════════════════════════════════════════

def get_positive_int(prompt):
    """Safely take a positive integer input from user."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("  ⚠  Please enter a number greater than 0!")
            else:
                return value
        except ValueError:
            print("  ⚠  Invalid input! Please enter a whole number.")


def get_valid_mark(prompt):
    """Safely take a mark between 0 and 100."""
    while True:
        try:
            mark = float(input(prompt))
            if 0 <= mark <= 100:
                return mark
            else:
                print("  ⚠  Marks must be between 0 and 100!")
        except ValueError:
            print("  ⚠  Invalid input! Please enter a number.")


def collect_data():
    """Collect student names and marks from user."""
    print(f"\n{DIVIDER}")
    print("  📥  DATA ENTRY")
    print(DIVIDER)

    num_students = get_positive_int("  Enter number of students : ")
    num_subjects = get_positive_int("  Enter number of subjects : ")

    student_names = []
    subject_names = []
    data          = []

    # collect subject names
    print(f"\n{THIN_DIV}")
    print("  Enter Subject Names:")
    print(THIN_DIV)
    for j in range(num_subjects):
        name = input(f"  Subject {j+1} name : ").strip()
        subject_names.append(name if name else f"Subject {j+1}")

    # collect student names and marks
    print(f"\n{THIN_DIV}")
    print("  Enter Student Names and Marks:")
    print(THIN_DIV)
    for i in range(num_students):
        print(f"\n  Student {i+1}:")
        name = input(f"    Name : ").strip()
        student_names.append(name if name else f"Student {i+1}")

        student_marks = []
        for j, subject in enumerate(subject_names):
            mark = get_valid_mark(f"    {subject} marks : ")
            student_marks.append(mark)
        data.append(student_marks)

    marks_array = np.array(data)
    return marks_array, student_names, subject_names


# ══════════════════════════════════════════════════════════
# ANALYSIS FUNCTIONS
# ══════════════════════════════════════════════════════════

def analyze(marks_array, student_names, subject_names):
    """Run all analyses and return results dictionary."""
    results = {}

    results['marks']           = marks_array
    results['students']        = student_names
    results['subjects']        = subject_names

    # averages
    results['avg_per_student'] = np.mean(marks_array, axis=1)
    results['avg_per_subject'] = np.mean(marks_array, axis=0)

    # scores
    results['highest_per_student'] = np.max(marks_array, axis=1)
    results['lowest_per_student']  = np.min(marks_array, axis=1)
    results['total_per_student']   = np.sum(marks_array, axis=1)

    # topper
    topper_idx              = np.argmax(results['total_per_student'])
    results['topper_index'] = topper_idx
    results['topper_name']  = student_names[topper_idx]
    results['topper_total'] = results['total_per_student'][topper_idx]

    # pass / fail per student
    results['student_status'] = np.where(
        results['avg_per_student'] >= PASS_MARK, 'PASS', 'FAIL'
    )

    # standard deviation per subject
    results['std_per_subject'] = np.std(marks_array, axis=0)

    # grade per student
    results['grades'] = [
        get_grade(avg) for avg in results['avg_per_student']
    ]

    # class statistics
    results['class_avg'] = np.mean(marks_array)
    results['class_max'] = np.max(marks_array)
    results['class_min'] = np.min(marks_array)
    results['class_std'] = np.std(marks_array)

    return results


def get_grade(average):
    """Convert average marks to letter grade."""
    if average >= 90: return 'A+'
    elif average >= 80: return 'A'
    elif average >= 70: return 'B'
    elif average >= 60: return 'C'
    elif average >= 50: return 'D'
    else: return 'F'


# ══════════════════════════════════════════════════════════
# DISPLAY FUNCTIONS
# ══════════════════════════════════════════════════════════

def display_report(results):
    """Print full report to screen."""
    lines = build_report(results)
    for line in lines:
        print(line)


def build_report(results):
    """Build the full report as a list of lines."""
    lines = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines.append(f"\n{DIVIDER}")
    lines.append("       STUDENT PERFORMANCE ANALYSIS REPORT")
    lines.append(f"       Generated: {timestamp}")
    lines.append(DIVIDER)

    # ── marks table ──
    lines.append("\n  📊  MARKS TABLE")
    lines.append(THIN_DIV)
    header = f"  {'Student':<15}" + "".join(f"{s:<10}" for s in results['subjects']) + f"{'Total':<10}{'Avg':<8}{'Grade'}"
    lines.append(header)
    lines.append(THIN_DIV)

    for i, name in enumerate(results['students']):
        marks_row = "".join(f"{results['marks'][i][j]:<10.1f}" for j in range(len(results['subjects'])))
        total     = results['total_per_student'][i]
        avg       = results['avg_per_student'][i]
        grade     = results['grades'][i]
        status    = results['student_status'][i]
        lines.append(f"  {name:<15}{marks_row}{total:<10.1f}{avg:<8.1f}{grade}  [{status}]")

    lines.append(THIN_DIV)

    # ── subject averages ──
    lines.append("\n  📚  SUBJECT ANALYSIS")
    lines.append(THIN_DIV)
    for j, subject in enumerate(results['subjects']):
        lines.append(
            f"  {subject:<20} Avg: {results['avg_per_subject'][j]:.2f}"
            f"  |  Std Dev: {results['std_per_subject'][j]:.2f}"
        )
    lines.append(THIN_DIV)

    # ── topper ──
    lines.append(f"\n  🏆  CLASS TOPPER")
    lines.append(THIN_DIV)
    lines.append(f"  Name          : {results['topper_name']}")
    lines.append(f"  Total Marks   : {results['topper_total']:.1f}")
    lines.append(f"  Average       : {results['avg_per_student'][results['topper_index']]:.2f}")
    lines.append(f"  Grade         : {results['grades'][results['topper_index']]}")
    lines.append(THIN_DIV)

    # ── class stats ──
    lines.append(f"\n  📈  CLASS STATISTICS")
    lines.append(THIN_DIV)
    lines.append(f"  Class Average     : {results['class_avg']:.2f}")
    lines.append(f"  Highest Mark      : {results['class_max']:.1f}")
    lines.append(f"  Lowest Mark       : {results['class_min']:.1f}")
    lines.append(f"  Std Deviation     : {results['class_std']:.2f}")

    # pass fail count
    pass_count = np.sum(results['student_status'] == 'PASS')
    fail_count = np.sum(results['student_status'] == 'FAIL')
    lines.append(f"  Students Passed   : {pass_count}")
    lines.append(f"  Students Failed   : {fail_count}")
    lines.append(THIN_DIV)
    lines.append(f"{DIVIDER}\n")

    return lines


def save_report(results):
    """Save report to text file."""
    lines = build_report(results)
    with open(REPORT_FILE, "a",encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"\n   Report saved to '{REPORT_FILE}'")


def display_subject_comparison(results):
    """Show which subject is hardest/easiest."""
    print(f"\n{DIVIDER}")
    print("  📊  SUBJECT DIFFICULTY COMPARISON")
    print(DIVIDER)
    hardest_idx  = np.argmin(results['avg_per_subject'])
    easiest_idx  = np.argmax(results['avg_per_subject'])
    print(f"  Hardest Subject  : {results['subjects'][hardest_idx]}"
          f"  (avg: {results['avg_per_subject'][hardest_idx]:.2f})")
    print(f"  Easiest Subject  : {results['subjects'][easiest_idx]}"
          f"  (avg: {results['avg_per_subject'][easiest_idx]:.2f})")
    print(THIN_DIV)


def display_student_ranking(results):
    """Show students ranked by total marks."""
    print(f"\n{DIVIDER}")
    print("  🏅  STUDENT RANKING")
    print(DIVIDER)
    ranked_idx = np.argsort(results['total_per_student'])[::-1]
    for rank, idx in enumerate(ranked_idx):
        print(f"  #{rank+1}  {results['students'][idx]:<20}"
              f"Total: {results['total_per_student'][idx]:.1f}"
              f"  Grade: {results['grades'][idx]}")
    print(THIN_DIV)


# ══════════════════════════════════════════════════════════
# MENU
# ══════════════════════════════════════════════════════════

def show_menu():
    """Display main menu."""
    print(f"\n{DIVIDER}")
    print("  📋  MAIN MENU")
    print(THIN_DIV)
    print("  1.  Enter New Student Data")
    print("  2.  View Full Report")
    print("  3.  View Subject Comparison")
    print("  4.  View Student Ranking")
    print("  5.  Save Report to File")
    print("  6.  Exit")
    print(THIN_DIV)


def main():
    """Main program entry point."""
    print(DIVIDER)
    print("   STUDENT PERFORMANCE ANALYZER")
    print("   Powered by NumPy")
    print("   University of Peshawar | AI Semester 2")
    print(DIVIDER)

    results = None

    while True:
        show_menu()
        choice = input("  Enter your choice (1-6): ").strip()

        if choice == "1":
            try:
                marks_array, student_names, subject_names = collect_data()
                results = analyze(marks_array, student_names, subject_names)
                print("\n  ✅  Data collected and analyzed successfully!")
            except KeyboardInterrupt:
                print("\n  ⚠  Data entry cancelled.")

        elif choice == "2":
            if results is None:
                print("\n  ⚠  No data yet! Please enter student data first (Option 1).")
            else:
                display_report(results)

        elif choice == "3":
            if results is None:
                print("\n  ⚠  No data yet! Please enter student data first (Option 1).")
            else:
                display_subject_comparison(results)

        elif choice == "4":
            if results is None:
                print("\n  ⚠  No data yet! Please enter student data first (Option 1).")
            else:
                display_student_ranking(results)

        elif choice == "5":
            if results is None:
                print("\n  ⚠  No data yet! Please enter student data first (Option 1).")
            else:
                save_report(results)

        elif choice == "6":
            print(f"\n{DIVIDER}")
            print("  Goodbye! Thank you for using Student Analyzer.")
            print(DIVIDER)
            break

        else:
            print("\n  ⚠  Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()