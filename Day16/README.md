# 📅 Day 16 - Python Learning Log

## 🧠 Topics Covered
- Introduction to **Object-Oriented Programming (OOP)** in Python
- Working with Python **modules** like `turtle` and `prettytable`
- Creating **custom classes** to model real-world entities
- Building a modular and maintainable **Coffee Machine App** using:
  - `CoffeeMaker`, `Menu`, `MenuItem`, and `MoneyMachine` classes
  - Abstraction, encapsulation, and method-based interaction
- Hands-on exploration of how **classes**, **objects**, and **methods** work together

## 📂 Files Included

- `Lec1.py`:  
  - Introduces the `turtle` module for basic graphics.
  - Creates a `Turtle` object (`timmy`) and draws a simple line using `.forward()` method.
  - Uses `Screen()` class to manage the graphics window.

- `Lec2.py`:  
  - Uses `prettytable` to display structured data (Pokémon names and types) in tabular format.
  - Demonstrates `.add_column()` and `.align` properties for formatting output.

- `CoffeeOop.py`:  
  - Main application logic for a **CLI-based Coffee Machine**.
  - Accepts user input, checks resource sufficiency, processes coins, and serves drinks.
  - Tightly integrates OOP concepts via composition of custom class instances.

- `coffee_maker.py`:  
  - Contains the `CoffeeMaker` class:
    - Tracks internal resources (water, milk, coffee)
    - Handles resource validation and deduction
    - Provides `.report()` and `.make_coffee()` methods

- `menu.py`:  
  - Defines two classes:
    - `MenuItem`: Represents a single drink and its cost/ingredients.
    - `Menu`: Holds all menu items, returns available drinks, and searches for drink by name.

- `money_machine.py`:  
  - Contains `MoneyMachine` class to simulate money collection.
  - Handles:
    - Coin processing
    - Payment verification
    - Change calculation
    - Profit tracking via `self.profit`

## 📝 Summary
On Day 16, I:
- Explored the basics of **OOP in Python** using real-world examples like coffee vending machines.
- Got comfortable working with external libraries (`turtle`, `prettytable`).
- Understood the **importance of modular design** by splitting logic across multiple files.
- Learned how **object interactions** can simplify code flow and improve maintainability.

## 🚀 Key Learnings
- `class` is used to define blueprints for objects, and `self` refers to the instance itself.
- Composition (one class using another) is a powerful OOP pattern.
- Breaking code into multiple files (modular programming) promotes reusability and debugging ease.
- External libraries like `prettytable` and `turtle` are easy to use and improve visualization/output.

## 🔗 Resources Used
- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)
- [PrettyTable - PyPI](https://pypi.org/project/prettytable/)
- [Turtle Module - Docs](https://docs.python.org/3/library/turtle.html)

---

> 💬 These codes are written as part of my learning journey. While I’ve done my best (with help from online resources), mistakes or bugs are possible. **Feel free to share corrections, suggestions, or improvements!**

> 💡 This is part of my #100DaysOfPython challenge. Follow the journey [here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong).
