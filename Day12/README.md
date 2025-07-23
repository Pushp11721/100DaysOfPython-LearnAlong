# 📅 Day 12 - Python Learning Log

## 🧠 Topics Covered
- **Variable Scope in Python**:
  - Local scope vs global scope
  - Global variable modification using `global` keyword
  - Creating and using global **constants**
- Function nesting and visibility of variables
- Building a **Number Guessing Game** with difficulty levels and feedback

## 📂 Files Included
- `Lec1.py`: Demonstrates the difference between **local** and **global** variables.
- `Lec2.py`: Shows that variables defined inside a function are **not accessible globally**.
- `Lec3.py`: Uses the `global` keyword to modify a global variable from inside a function.
- `Lec4.py`: Defines and uses a **global constant** (`PI`) using capital naming convention.
- `Project.py`: A fun and interactive **Number Guessing Game** that:
  - Randomly selects a number between 1 and 100
  - Lets users choose difficulty levels (`easy` or `hard`)
  - Tracks remaining attempts and gives hints based on proximity
- `art.py`: Contains a stylized ASCII art logo used as a game header.

## 📝 Summary
On Day 12, I:
- Gained a deep understanding of **scope rules** in Python — how variables behave inside and outside functions.
- Practiced declaring and modifying **global variables and constants**.
- Built a terminal-based **Number Guessing Game** with randomized values and user-controlled flow.
- Used conditional logic and loops to create an interactive experience with graded hints.

## 🚀 Key Learnings
- Variables defined **inside functions** have **local scope** and aren't accessible outside.
- To change a **global variable** from within a function, use the `global` keyword.
- Constants in Python are typically written in **all caps** and should not be changed once declared.
- Using feedback like “Too high” or “Too low” makes guessing games more user-friendly.
- Game difficulty can be easily implemented using variable control (number of lives).

## 🔗 Resources Used
- [Python Variable Scope - W3Schools](https://www.w3schools.com/python/python_scope.asp)
- [Global vs Local Variables - GeeksforGeeks](https://www.geeksforgeeks.org/global-local-variables-python/)
- [Python Constants](https://peps.python.org/pep-0008/#constants)
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

> 💬 These codes are written as part of my learning journey. While I’ve done my best (with help from online resources), mistakes or bugs are possible. **Feel free to share corrections, suggestions, or improvements!**

> 💡 This is part of my #100DaysOfPython challenge. Follow the journey [here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong).
