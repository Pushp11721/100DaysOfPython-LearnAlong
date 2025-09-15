# 📅 Day 19 - Python Learning Log

## 🧠 Topics Covered
- Handling **keyboard events** with `onkey()` and `listen()`
- Moving a turtle using **custom functions** mapped to keys
- Building an **Etch-a-Sketch clone** with directional keys
- Creating a **Turtle Race Game**:
  - Multiple turtles initialized with different colors
  - Taking user bets using `textinput()`
  - Randomized turtle movement
  - Detecting race winner and comparing with user’s bet

## 📂 Files Included

- `Lec1.py`:  
  - Demonstrates simple key binding where pressing the `space` key moves the turtle forward.

- `SketchApp_Lec2.py`:  
  - A mini drawing app:
    - `W` → Move forward  
    - `S` → Move backward  
    - `A` → Turn left  
    - `D` → Turn right  
    - `C` → Clear drawing and reset position  

- `game.py`:  
  - Implements a **turtle race** game:
    - Six turtles are lined up with different colors.
    - User places a bet on which turtle will win.
    - Turtles move forward randomly until one crosses the finish line.
    - The program announces if the user won or lost.

## 📝 Summary
On Day 19, I explored **event-driven programming** with Turtle:
- Learned to bind keys to functions using `onkey()` for interactive movement.
- Built a fun **Sketch App** (Etch-a-Sketch style) with full reset functionality.
- Implemented a **Turtle Race Game** where randomness decides the winner, and user input makes the game engaging.

## 🚀 Key Learnings
- `screen.listen()` activates key detection for user input.
- `onkey(function, key)` maps keyboard keys to specific turtle actions.
- `textinput()` allows interactive user input via dialog boxes.
- Combining loops, randomness, and user input creates **game-like experiences** in Python.

## 🔗 Resources Used
- [Python Turtle onkey() – Docs](https://docs.python.org/3/library/turtle.html#turtle.onkey)
- [Event Handling with Turtle](https://medium.com/@sjalexandre/python-tutorial-turtle-events-4b3d0064e85e)
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

> 💬 These codes are part of my hands-on learning journey. Suggestions and improvements are always welcome!  

> 💡 This is part of my #100DaysOfPython challenge. Follow the journey on GitHub: [Here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong)
