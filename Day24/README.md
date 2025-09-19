# 📅 Day 24 - Python Learning Log

## 🧠 Topics Covered
- **File Handling Basics**:
  - Opening, reading, and closing files manually.
  - Using `with open()` for safer file handling (auto-closes file).
  - File modes:  
    - `"r"` → Read existing content.  
    - `"w"` → Write (overwrites existing file).  
    - `"a"` → Append (adds new content without deleting).  
  - Creating new files if they don’t exist (with `"w"`).
  - Using **relative file paths** for accessing files in different directories.

- **Mail Merge Project**:
  - Read names from a file (`invited_names.txt`).
  - Use a template letter (`starting_letter.txt`) with placeholder `[name]`.
  - Generate personalized letters for each name.
  - Save the letters into a dedicated **ReadyToSend** folder.

---

## 📂 Files Included

- `way1.py`:  
  - Opens a file (`my_file.txt`), reads its content, prints it, and closes it manually.

- `way2.py`:  
  - Demonstrates the use of `with open(..., "w")` to write text safely without needing manual `close()`.

- `way3.py`:  
  - Opens a file in **append mode** to add new content without overwriting existing text.

- `way4.py`:  
  - Shows how Python automatically **creates a new file** if it doesn’t exist when opened in `"w"` mode.

- `way5.py`:  
  - Demonstrates **relative file paths** by accessing files located outside the current directory.

- `my_file.txt`:  
  - Text file used for read/write/append practice.

- `new_file.txt`:  
  - File created using `"w"` mode in `way4.py`.

---

### 📬 Mail Merge Project

- `project/main.py`:  
  - Core script for generating personalized letters.  
  - Reads names from `Input/Names/invited_names.txt`.  
  - Loads the template from `Input/Letters/starting_letter.txt`.  
  - Replaces `[name]` with actual names.  
  - Saves each customized letter in the `Output/ReadyToSend/` folder.

- `project/Input/Letters/starting_letter.txt`:  
  - Template letter with placeholder `[name]`.

- `project/Input/Names/invited_names.txt`:  
  - List of invitee names (e.g., Aang, Zuko, Katara).

- `project/Output/ReadyToSend/`:  
  - Contains personalized letters like:  
    - `letter_for_Aang.docs`  
    - `letter_for_Appa.docs`  
    - `letter_for_Katara.docs`  
    - … and more.

---

## 📝 Summary
On Day 24, I:
- Learned **different approaches to file handling** (`open`, `with`, modes like `r`, `w`, `a`).
- Practiced creating and appending files.
- Understood **relative file paths** for organizing project files.
- Built a **Mail Merge automation project**:
  - Read invitee names from a file.
  - Replaced placeholders in a template.
  - Generated multiple personalized letters automatically.

---

## 🚀 Key Learnings
- Always use `with open()` when working with files → ensures proper closing.
- `"w"` overwrites while `"a"` appends → choose wisely to avoid data loss.
- File handling is essential for **persistent storage** and automation tasks.
- Mail merge is a great example of combining file handling with loops and string replacement.
- Organizing files into structured folders (Input/Output) makes projects more maintainable.

---

## 🔗 Resources Used
- [Python File Handling - W3Schools](https://www.w3schools.com/python/python_file_handling.asp)  
- [Python File Modes - GeeksforGeeks](https://www.geeksforgeeks.org/file-handling-python/)  
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

> 💬 These codes are part of my hands-on learning.  
> If you spot bugs or have suggestions, feel free to contribute or share feedback!

> 💡 Part of my #100DaysOfPython challenge. Follow along here: [Here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong)
