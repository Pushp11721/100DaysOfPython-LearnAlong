# 📅 Day 10 - Python Learning Log

## 🧠 Topics Covered
- Function documentation using **docstrings**
- Using `.title()` for string formatting
- Nesting functions (function inside function call)
- Creating a **reusable calculator** using:
  - Dictionary-based function mapping
  - User-defined arithmetic functions
  - Recursion for restarting the calculator
- Integrating external files (ASCII art via `art.py`)

## 📂 Files Included
- `func_desc.py`: 
  - Demonstrates function composition and use of docstrings (`'''...'''`) to document what a function does.
  - Examples of passing strings, doubling them, and chaining functions.
- `Calculator.py`: 
  - A complete command-line calculator that supports addition, subtraction, multiplication, and division.
  - Uses a dictionary to map operations to functions.
  - Includes looped and recursive logic to allow continuous calculations or fresh restarts.
- `art.py`: 
  - Contains a multi-line string variable `calc_diag` that holds the ASCII art for the calculator UI.

## 📝 Summary
On Day 10, I:
- Practiced writing **well-documented functions** using docstrings.
- Explored how one function can be used inside another (function chaining).
- Built a professional-style **command-line calculator** that keeps the program running based on user input.
- Separated the UI (ASCII art) from logic to improve code modularity.

## 🚀 Key Learnings
- Triple-quoted strings (`'''docstring'''`) are used to describe what a function does — useful for documentation and IDEs.
- Dictionary-function mapping allows dynamic operation calling (e.g., `operations["+"](2, 3)`).
- Recursive function calls (`calculator()` inside itself) can be used to restart programs cleanly.
- Splitting UI into a separate file improves **code readability and organization**.

## 🔗 Resources Used
- [Python Docstrings - W3Schools](https://w3schools.tech/tutorial/python/python_docstrings)
- [Python Function Arguments](https://www.geeksforgeeks.org/functions-in-python/)
- [Calculator CLI Logic - Real Python](https://realpython.com/python-thinking-recursively/)
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

> 💬 These codes are written as part of my learning journey. While I’ve done my best (with help from online resources), mistakes or bugs are possible. **Feel free to share corrections, suggestions, or improvements!**

> 💡 This is part of my #100DaysOfPython challenge. Follow the journey [here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong).
