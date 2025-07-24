# 📅 Day 13 - Python Learning Log

## 🧠 Topics Covered
- Identifying and fixing **logic bugs**, **indexing errors**, and **range issues**
- Using **print statements** to trace values and find bugs
- Applying **try-except** blocks to handle input errors gracefully
- Understanding **off-by-one errors** in `range()`
- Using debugging tools or strategic printouts to verify variable values
- Creating and using custom utility modules (`maths.py`)

## 📂 Files Included
- `Lec1.py`: Demonstrates an **off-by-one error** in a `for` loop range.
- `Lec2.py`: Fixes an **indexing bug** caused by `randint(1,6)` in a list of 0-based indexes.
- `Lec3.py`: Handles a missing boundary case (year 1994) in conditional logic.
- `Lec4.py`: Uses a **try-except block** to prevent `ValueError` during user input conversion.
- `Lec5.py`: Tracks and fixes a **variable assignment bug** using print statements.
- `Lec6.py`: Debugs logic related to list mutation and value aggregation using an imported module.
- `maths.py`: Custom utility module defining an `add()` function used in calculations.

## 📝 Summary
On Day 13, I:
- Focused on improving my **debugging skills** by analyzing real Python bugs.
- Learned how to use **descriptive error messages**, **print tracing**, and **step-by-step execution** to locate errors.
- Practiced identifying typical Python mistakes like:
  - Misconfigured `range()`
  - Misused list indices
  - Improper comparison or assignment (`==` vs `=`)
  - Unhandled exceptions
- Improved overall code reliability and readability using better structure and safeguards.

## 🚀 Key Learnings
- Off-by-one errors are common with `range()` and loops; always double-check boundaries.
- `randint()` includes both ends; for list indexing, always ensure the index range is valid.
- Always test **boundary cases** in conditional statements.
- `try-except` blocks can prevent your program from crashing due to input errors.
- Use custom modules like `maths.py` to make code **reusable and modular**.

## 🔗 Resources Used
- [Python Debugging - W3Schools](https://www.w3schools.com/python/ref_func_print.asp)
- [try-except in Python](https://www.w3schools.com/python/python_try_except.asp)
- [Off-by-One Errors - Wikipedia](https://en.wikipedia.org/wiki/Off-by-one_error)
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

> 💬 These codes are written as part of my learning journey. While I’ve done my best (with help from online resources), mistakes or bugs are possible. **Feel free to share corrections, suggestions, or improvements!**

> 💡 This is part of my #100DaysOfPython challenge. Follow the journey [here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong).
