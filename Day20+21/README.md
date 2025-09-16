# 📅 Day 20 + 21 - Python Learning Log

## 🧠 Topics Covered
- **Python Slicing**:
  - Using `[start:end]` for sublists.
  - Reversing lists/strings with `[::-1]`.
- **OOP Inheritance**:
  - Creating parent (`Animal`) and child (`Fish`) classes.
  - Using `super()` to call parent class methods.
  - Overriding methods and extending behavior.
- **Snake Game (Full Project)**:
  - Building a multi-file project with **OOP principles**.
  - Snake movement and body extension.
  - Randomly generated food items.
  - Score tracking with high score persistence (saved in a text file).
  - Collision detection with walls and self.

## 📂 Files Included

- `slicing.py`:  
  - Demonstrates slicing in Python by printing sublists and reversing a list.

- `inheritance.py`:  
  - Example of **inheritance and method overriding**.  
  - `Fish` inherits from `Animal` and extends the `breathe` method.

### 🐍 Snake Game Project
- `main.py`:  
  - Sets up the game screen, initializes Snake, Food, and ScoreBoard classes.  
  - Contains the main game loop with collision detection and controls.

- `snake.py`:  
  - Defines the `Snake` class:
    - Creates and manages snake segments.
    - Moves snake smoothly by shifting positions.
    - Adds new segments when food is eaten.
    - Resets when collisions occur.

- `food.py`:  
  - Defines the `Food` class:
    - Inherits from `Turtle`.
    - Places food randomly on screen.
    - Refreshes after being eaten.

- `scorecard.py`:  
  - Defines the `ScoreBoard` class:
    - Tracks current score and high score.
    - Saves and reads high score from `data.txt`.
    - Displays scores on the screen.

- `data.txt`:  
  - Stores the high score persistently (e.g., `14`).

## 📝 Summary
Over Day 20 and 21, I:
- Practiced Python slicing and understood its use in data manipulation.
- Learned how **inheritance and method overriding** make code reusable and extendable.
- Completed the **Snake Game project**:
  - Implemented a playable game with snake movement, food generation, and score tracking.
  - Added collision detection with walls and tail.
  - Used file handling to persist high scores.

## 🚀 Key Learnings
- List slicing is a powerful way to manipulate sequences (`[::-1]` for reversing).
- Inheritance allows code reuse, while `super()` helps extend parent functionality.
- Large projects are best handled with multiple files/modules for **modularity**.
- Persistent storage (via files like `data.txt`) lets games save progress across runs.
- Event-driven programming (`onkey`) can be combined with loops for interactive games.

## 🔗 Resources Used
- [Python Slicing - W3Schools](https://www.w3schools.com/python/python_strings_slicing.asp)  
- [Inheritance in Python - GeeksforGeeks](https://www.geeksforgeeks.org/inheritance-in-python/)  
- [Turtle Graphics Documentation](https://docs.python.org/3/library/turtle.html)  
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

> 💬 This was my **first complete game project in Python**. Excited to build more complex ones!  

> 💡 Part of my #100DaysOfPython challenge. Follow along here: [Here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong)
