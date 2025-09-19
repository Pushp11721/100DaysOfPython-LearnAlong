# 📅 Day 24 - Python Learning Log

## 🧠 Topics Covered
- **Mail Merge Project (Automated Invitations)**:
  - Practiced **file handling** in Python (`open`, `readlines`, `write`).
  - Used **string replacement** with placeholders (`[name]`).
  - Read data from multiple input files (names + template letter).
  - Generated personalized letters for each invitee.
  - Saved ready-to-send invitation files in an output folder.

---

## 📂 Files Included

- `main.py`:  
  - Core script that runs the Mail Merge logic.  
  - Reads names from `invited_names.txt`.  
  - Loads the template letter from `starting_letter.txt`.  
  - Replaces `[name]` with actual invitee names.  
  - Saves each personalized letter in `Output/ReadyToSend/`.  

- `Input/Letters/starting_letter.txt`:  
  - Template letter containing the placeholder `[name]`.  

- `Input/Names/invited_names.txt`:  
  - List of names to be invited (e.g., Aang, Zuko, Katara, etc.).  

- `Output/ReadyToSend/`:  
  - Folder containing generated invitation letters like:  
    - `letter_for_Aang.docs`  
    - `letter_for_Appa.docs`  
    - `letter_for_Katara.docs`  
    - ... and more.  

---

## 📝 Summary
On Day 24, I:  
- Built an **Automated Mail Merge project** that generates invitation letters.  
- Practiced reading data from files and using placeholders for text substitution.  
- Learned how to manage multiple folders (`Input`, `Output`) for cleaner project organization.  
- Created personalized `.docs` letters for each invitee using Python.  

---

## 🚀 Key Learnings
- Using `with open(...) as file:` ensures proper file handling (auto-close).  
- `.strip()` removes unwanted `\n` characters from names.  
- `string.replace()` makes it easy to handle placeholders dynamically.  
- Structuring projects into **Input** and **Output** folders makes the workflow neat.  
- Practicing automation helps understand how mail-merge systems (like MS Word) work under the hood.  

---

## 🔗 Resources Used
- [Python File Handling Docs](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)  
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)  

---

> ✉️ This was my **first automation-style project** using file handling.  
> 💬 This is a **learning project** — I referred to tutorials and resources while building it.  
> 💡 Part of my #100DaysOfPython challenge. Follow along here: [Here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong)  
