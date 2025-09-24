# 📅 Day 26 - Python Learning Log

## 🧠 Topics Covered
- **List Comprehension**:
  - Shorthand for creating lists: `[new_item for item in list]`.
  - Used with numbers, strings, and ranges.
  - Conditional filtering: `[item for item in list if condition]`.
  - Example: Generate short names or uppercase versions of names.

- **Dictionary Comprehension**:
  - Create dictionaries dynamically: `{key:value for item in list}`.
  - Generate random student scores with `random.randint()`.
  - Conditional filtering inside comprehension:
    - Example: Select only students who scored above passing marks.

- **Iterating Pandas DataFrames**:
  - Using `.iterrows()` to loop through rows in a DataFrame.
  - Access row properties like `row.student` or `row.score`.
  - Filter or transform DataFrame rows inside loops.

---

## 📂 Files Included

- `main1.py`:  
  - Demonstrates **list comprehensions** with numbers, strings, and ranges.  
  - Includes **conditional list comprehensions** to filter short names and create uppercase names.

- `main2.py`:  
  - Creates random student scores using **dictionary comprehension**.  
  - Filters students who passed based on score > 33.

- `main3.py`:  
  - Shows how to iterate through a **pandas DataFrame** with `.iterrows()`.  
  - Prints details for specific students (e.g., Angela).

---

### 📘 Project: NATO Phonetic Alphabet Converter
- `Project/main.py`:  
  - Reads NATO phonetic codes from `nato_phonetic_alphabet.csv`.  
  - Builds a dictionary in the format `{"A": "Alfa", "B": "Bravo"}`.  
  - Takes user input and outputs a list of phonetic words (e.g., `PUSH` → `Papa, Uniform, Sierra, Hotel`).

- `Project/nato_phonetic_alphabet.csv`:  
  - Contains NATO phonetic alphabet mappings (A → Alfa, B → Bravo, … Z → Zulu).

---

## 📝 Summary
On Day 26, I:
- Learned **list and dictionary comprehensions** for faster, cleaner code.  
- Practiced applying conditions in comprehensions to filter data.  
- Explored looping through **pandas DataFrames** using `.iterrows()`.  
- Built a fun **NATO Phonetic Alphabet Converter** project using pandas + dictionary comprehension.

---

## 🚀 Key Learnings
- List comprehensions make code concise and readable.  
- Dictionary comprehensions are powerful for generating dynamic mappings.  
- Conditional logic can be embedded directly into comprehensions.  
- `.iterrows()` is handy for row-wise operations in pandas DataFrames.  
- Combining **comprehensions + pandas** leads to efficient, real-world data handling.

---

## 🔗 Resources Used
- [List Comprehensions - W3Schools](https://www.w3schools.com/python/python_lists_comprehension.asp)  
- [Dictionary Comprehensions - GeeksforGeeks](https://www.geeksforgeeks.org/python-dictionary-comprehension/)  
- [Iterating Pandas DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html)  
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

> 💬 These codes are part of my hands-on learning.  
> If you spot bugs or have suggestions, feel free to contribute or share feedback!  

> 💡 Part of my #100DaysOfPython challenge. Follow along here: [Here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong)
