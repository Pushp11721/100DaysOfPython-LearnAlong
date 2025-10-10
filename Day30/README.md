# 📅 Day 30 - Python Learning Log

## 🧠 Topics Covered
- **Error and Exception Handling**:
  - Understanding common errors:
    - `FileNotFoundError`, `KeyError`, `IndexError`, `TypeError`, `ValueError`.
  - Using:
    - `try`: Code block that might raise an error.
    - `except`: Handles specific exceptions gracefully.
    - `else`: Executes when no exceptions occur.
    - `finally`: Always executes, regardless of errors.
  - Preventing crashes by anticipating potential exceptions.

- **Raising Custom Exceptions**:
  - Using `raise` to trigger specific errors manually.
  - Example: Restricting unrealistic user inputs (e.g., height > 3 meters).

- **JSON Refresher**:
  - Review of methods:
    - `json.dump()` → Write JSON data.
    - `json.load()` → Read JSON data.
    - `json.update()` → Modify existing JSON data.
  - Reinforcing JSON’s use for structured, persistent data storage.

- **Enhanced NATO Project (Error Handling)**:
  - Improved version of the **NATO Phonetic Alphabet Converter**.
  - Handles **KeyError** gracefully when users enter non-alphabetic characters.
  - Uses recursion to re-prompt user input after invalid entries.

---

## 📂 Files Included

- `main.py`:  
  - Introduces **basic exception types** and `try/except/else/finally` structure.

- `main1.py`:  
  - Demonstrates handling multiple exceptions:
    - Creates missing files automatically.
    - Prints specific error messages using `as error_message`.
    - Ensures files are closed with `finally`.

- `main3.py`:  
  - Shows how to **raise custom exceptions** (`ValueError`).
  - Calculates BMI but prevents unrealistic height inputs.

- `main4.py`:  
  - Short notes on **JSON operations**: write, read, and update methods.

- `a_file.txt`:  
  - A simple text file created during file-handling demonstrations.

---

### 📘 Project: NATO Phonetic Alphabet (Error-Handled Version)
- `NATO/main.py`:  
  - Reads `nato_phonetic_alphabet.csv` into a dictionary.
  - Converts user input into phonetic code words.
  - Handles non-letter inputs (`KeyError`) and re-prompts until valid input.
  - Demonstrates robust error handling and clean user interaction.

- `NATO/nato_phonetic_alphabet.csv`:  
  - CSV file mapping letters to NATO phonetic codes (A → Alfa, B → Bravo, etc.).

---

## 📝 Summary
On Day 30, I:  
- Learned how to **handle runtime errors gracefully** using `try`, `except`, `else`, and `finally`.  
- Practiced raising **custom exceptions** to maintain input integrity.  
- Reviewed **JSON operations** for reliable data management.  
- Upgraded the **NATO Phonetic Alphabet Converter** to handle invalid inputs without crashing.  
- Understood how **exception handling** improves code stability, user experience, and maintainability.  

---

## 🚀 Key Learnings
- Always anticipate possible errors — **defensive programming** saves debugging time.  
- `try/except` ensures smooth user experience without breaking program flow.  
- `finally` is useful for cleanup tasks like closing files or releasing resources.  
- Custom exceptions help enforce data validation and program logic.  
- Error handling + recursion can create user-friendly, fail-safe loops.  

---

## 🔗 Resources Used
- [Python Exceptions - W3Schools](https://www.w3schools.com/python/python_try_except.asp)  
- [Raising Exceptions in Python - GeeksforGeeks](https://www.geeksforgeeks.org/python-raise-keyword/)  
- [JSON Module Documentation](https://docs.python.org/3/library/json.html)  
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)  

---

> 💬 These codes are written as part of my learning journey. While I’ve done my best (with help from online resources), mistakes or bugs are possible. **Feel free to share corrections, suggestions, or improvements!**

> 💡 Part of my #100DaysOfPython challenge. Follow along here: [Here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong)
