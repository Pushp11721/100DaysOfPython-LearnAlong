# 📅 Day 14 - Python Learning Log

## 🧠 Topics Covered
- Project: **Higher or Lower Game**
- Importing external files (`game_data.py`, `art.py`) for modular design
- Random selection of dictionary entries using `random.choice()` and `random.randint()`
- Data comparison logic using nested conditionals
- Keeping track of previous choices to avoid repetition
- Tracking and displaying user score
- Creating reusable functions (`format_data()`, `check_answer()`)
- Game flow control using loops and conditionals

## 📂 Files Included
- `main.py`: 
  - Full gameplay logic where the user compares two options based on their follower counts.
  - Avoids repeat selections and keeps track of scores using a `list_of_chosen`.
  - Interactive round-by-round design for continued play until a wrong guess.
  
- `game.py`: 
  - Contains a **refactored and modular** version of the game.
  - Includes functions like `format_data()` to cleanly display data and `check_answer()` to validate logic.
  
- `art.py`: 
  - Includes ASCII art assets: game logo and VS symbol, improving visual clarity in the terminal.

- `game_data.py`: 
  - Stores a large list of dictionaries, each containing name, follower count, description, and country of well-known people and brands.

## 📝 Summary
On Day 14, I:
- Developed a **"Higher or Lower"** game from scratch based on follower counts.
- Practiced breaking logic into clean, reusable **functions** for formatting and validation.
- Ensured **random selection** without repetition using list tracking.
- Learned how to manage game state (score, guesses, game over) through loops and conditions.
- Improved **code modularity** by splitting content into multiple files (`data`, `art`, logic).

## 🚀 Key Learnings
- Use `random.choice()` and `random.randint()` to pick values dynamically from lists.
- Avoid repeating selections by maintaining a **history list**.
- `if-else` logic helps in building validation for real-time games.
- Creating **separate modules** makes code more maintainable and scalable.
- Using functions improves readability and reuse across different parts of the game.

## 🔗 Resources Used
- [random.choice() - Python Docs](https://docs.python.org/3/library/random.html#random.choice)
- [Python Dictionaries - W3Schools](https://www.w3schools.com/python/python_dictionaries.asp)
- [ASCII Art Generator](https://patorjk.com/software/taag/)
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

> 💬 These codes are written as part of my learning journey. While I’ve done my best (with help from online resources), mistakes or bugs are possible. **Feel free to share corrections, suggestions, or improvements!**

> 💡 This is part of my #100DaysOfPython challenge. Follow the journey [here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong).
