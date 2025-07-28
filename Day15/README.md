# 📅 Day 15 - Python Learning Log

## 🧠 Topics Covered
- Project: **Coffee Machine Simulation**
- Working with nested dictionaries for menu items and ingredients
- Checking system resources (water, milk, coffee)
- Accepting user input for currency and simulating transaction logic
- Making change, refunding money, and updating resources dynamically
- Using multiple helper functions for:
  - `report()`: Shows remaining resources and earnings
  - `check_resources()`: Ensures enough ingredients for the drink
  - `ask_for_money()`: Takes coin input and handles transactions
  - `deduct()`: Updates the resource levels after a successful purchase
- Controlling program flow using loops and commands (`report`, `off`, etc.)

## 📂 Files Included
- `CoffeeMachine.py`: 
  - Implements a command-line simulation of a real-world coffee vending machine.
  - Supports three drink options: `espresso`, `latte`, and `cappuccino`.
  - Users can check the machine’s internal state with `report`, or turn it off with `off`.

## 📝 Summary
On Day 15, I:
- Created a working **coffee machine** that accepts user input, processes payments, and dispenses drinks.
- Handled logical branching for resource management and error feedback.
- Designed **realistic money-handling logic** using coin input simulation.
- Learned how to organize a Python program into **well-named helper functions** to make it more readable and maintainable.

## 🚀 Key Learnings
- Nested dictionaries are powerful for representing structured data like menu items and their ingredients.
- Floating-point arithmetic must be handled carefully when working with currency (e.g., rounding to 2 decimal places).
- Splitting logic into functions improves **modularity**, **reusability**, and **testability** of your code.
- Always account for user input variations like `"off"` and `"report"` when building interactive systems.

## 🔗 Resources Used
- [Python Nested Dictionaries](https://www.w3schools.com/python/python_dictionaries_nested.asp)
- [Working with Currency in Python](https://realpython.com/python-rounding/)
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

> 💬 These codes are written as part of my learning journey. While I’ve done my best (with help from online resources), mistakes or bugs are possible. **Feel free to share corrections, suggestions, or improvements!**

> 💡 This is part of my #100DaysOfPython challenge. Follow the journey [here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong).
