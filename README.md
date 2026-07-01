#  Student Grade Calculator

A simple Python program that calculates a student's average marks across five subjects and assigns a grade based on predefined grading criteria. The project also includes automated unit testing using **Pytest** to verify grading logic and ensure code reliability.

---

## Features

- Accepts marks for five subjects
- Validates user input
- Calculates average marks
- Assigns grades automatically
- Handles invalid inputs gracefully
- Includes automated unit tests with Pytest

---

## Technologies Used

- Python 3
- Pytest

---

## Project Structure

```
student-grade-prediction/
│
├── src/
│   └── grade.py
│
├── test/
│   └── test_grade.py
│
├── requirements.txt
│
├── README.md

```

---

## Grade Criteria

| Average Marks | Grade |
|--------------|-------|
| 90 - 100 | A+ |
| 75 - 89 | A |
| 60 - 74 | B |
| 50 - 59 | C |
| Below 50 | Fail |

---

## Installation

Clone the repository.

```bash
git clone https://github.com/sakshiSE/student-grade-prediction.git
```

Move into the project.

```bash
cd student-grade-prediction
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python src/grade.py
```

---

## Run Unit Tests

```bash
pytest
```

---

## Sample Output

```
Enter marks for 5 subjects (0-100)

Subject 1: 85
Subject 2: 78
Subject 3: 90
Subject 4: 88
Subject 5: 92

------ Result ------
Average : 86.60
Grade   : A
```
