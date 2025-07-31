# 📅 Day 17 - Python Learning Log

## 🧠 Topics Covered
- Deep dive into **Object-Oriented Programming (OOP)**:
  - Creating and using **classes** and **constructors (`__init__`)**
  - Setting **default attributes**
  - Defining **instance methods** (e.g., `.follow()`, `.enter_race_mode()`)
- OOP naming conventions:
  - PascalCase for class names
  - camelCase for method names
- Building an interactive **True/False Quiz App** using:
  - Multiple Python files/modules
  - Lists of object instances
  - Loop-based question prompting and scoring

## 📂 Files Included

### 🔸 Core OOP Practice
- `Lec1.py`:  
  - Demonstrates OOP naming conventions and simple method invocation (`doSomething()`).

- `Lec1.1.py`:  
  - Implements a `User` class with a constructor and a `.follow()` method to simulate followers/following logic.
  - Shows how object attributes (`self.followers`, `self.following`) can track state changes.

- `Lec2.py`:  
  - `Car` class with methods to dynamically change attributes (switch to race mode with fewer seats).

### 📁 Quiz App (`Quiz/`)
- `Quiz.py`:  
  - Main app logic to run the quiz game.
  - Loops through questions using the `QuizBrain` class and prints the final score.

- `question_model.py`:  
  - Defines a `Question` class with `text` and `answer` attributes.

- `data.py`:  
  - Stores a list of quiz questions in dictionary format.
  - Each dictionary holds a question and its correct answer (`"True"` or `"False"`).

- `quiz_brain.py`:  
  - Controls the quiz logic via the `QuizBrain` class.
  - Includes methods:
    - `.next_question()` – displays the question and takes user input.
    - `.check_answer()` – verifies the user's response.
    - `.still_has_question()` – checks if more questions remain.
  - Tracks score and progress.

## 📝 Summary
On Day 17, I:
- Practiced creating **custom Python classes** with constructors and methods.
- Understood how to structure a class-based program, like a quiz game, across multiple files.
- Gained confidence in using **object lists** (like `question_bank`) and dynamically creating object instances in loops.
- Applied OOP principles like **encapsulation**, modularity, and data management.

## 🚀 Key Learnings
- `__init__()` allows default attribute setup when an object is created.
- Class methods can manipulate both **self attributes** and other object attributes (`user1.follow(user2)`).
- Splitting logic across files improves clarity and separation of responsibilities.
- A list of class instances enables batch processing, ideal for quizzes, games, or simulations.

## 🔗 Resources Used
- [Python Classes and Objects - W3Schools](https://www.w3schools.com/python/python_classes.asp)
- [Python OOP Explained - Real Python](https://realpython.com/python3-object-oriented-programming/)
- [Python Constructor (`__init__`) Guide](https://www.geeksforgeeks.org/__init__-in-python/)
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

> 💬 These codes are part of my hands-on learning. If you spot bugs or have suggestions, feel free to contribute or share feedback!

> 💡 This is part of my #100DaysOfPython challenge. Track my progress [here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong).
