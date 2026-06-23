# 📊 Student Performance Analyzer

A command-line application built with **NumPy** that analyzes student exam data and generates detailed performance reports.

> Built by **Muhammad Talha** | University of Peshawar | AI Semester 2

---

## 🚀 Features

- ✅ Enter any number of students and subjects
- ✅ Calculate average marks per student (row-wise)
- ✅ Calculate average marks per subject (column-wise)
- ✅ Find class topper using `np.argmax()`
- ✅ Assign letter grades (A+, A, B, C, D, F)
- ✅ Pass / Fail status per student
- ✅ Student ranking leaderboard
- ✅ Subject difficulty comparison
- ✅ Class-wide statistics (mean, std dev, max, min)
- ✅ Save full report to `.txt` file
- ✅ Interactive menu system
- ✅ Full input validation and error handling

---

## 📦 Requirements

```
Python 3.x
NumPy
```

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/student-performance-analyzer.git

# Go into the folder
cd student-performance-analyzer

# Install NumPy
pip install numpy

# Run the program
python main.py
```

---

## 🖥️ How to Use

1. Run `python main.py`
2. Select **Option 1** to enter student data
3. Enter number of students and subjects
4. Enter subject names
5. Enter student names and their marks
6. Use the menu to:
   - View full report
   - View subject comparison
   - View student ranking
   - Save report to file

---

## 📋 Sample Output

```
=======================================================
   STUDENT PERFORMANCE ANALYSIS REPORT
   Generated: 2024-06-23 10:30:00
=======================================================

  📊  MARKS TABLE
-------------------------------------------------------
  Student        Math      Physics   English   Total     Avg     Grade
-------------------------------------------------------
  Talha          85.0      90.0      78.0      253.0     84.3    A     [PASS]
  Ali            70.0      65.0      88.0      223.0     74.3    B     [PASS]
  Sara           92.0      87.0      95.0      274.0     91.3    A+    [PASS]
-------------------------------------------------------

  🏆  CLASS TOPPER
-------------------------------------------------------
  Name          : Sara
  Total Marks   : 274.0
  Average       : 91.33
  Grade         : A+
-------------------------------------------------------

  🏅  STUDENT RANKING
-------------------------------------------------------
  #1  Sara                Total: 274.0  Grade: A+
  #2  Talha               Total: 253.0  Grade: A
  #3  Ali                 Total: 223.0  Grade: B
-------------------------------------------------------
```

---

## 📁 Project Structure

```
student-performance-analyzer/
│
├── main.py          # Main program file
├── README.md        # Project documentation
└── student_report.txt  # Generated after saving report
```

---

## 🧠 NumPy Concepts Used

| Concept | Where Used |
|---|---|
| `np.array()` | Store marks as 2D array |
| `np.mean(axis=1)` | Average per student |
| `np.mean(axis=0)` | Average per subject |
| `np.sum(axis=1)` | Total marks per student |
| `np.argmax()` | Find topper index |
| `np.argsort()` | Rank students |
| `np.std(axis=0)` | Subject difficulty |
| `np.where()` | Pass/Fail status |
| `np.max() / np.min()` | Highest/lowest marks |

---

## 📄 License

MIT License — free to use and modify.

