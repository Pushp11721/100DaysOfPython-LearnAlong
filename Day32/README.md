# 📅 Day 32 - Python Learning Log

## 🧠 Topics Covered
- **Email Automation with Python (`smtplib`)**:
  - Sending automated emails using Gmail’s SMTP server.
  - Using `starttls()` to enable secure email transfer.
  - Setting up message structure with subjects and message bodies.

- **Working with Dates (`datetime` module)**:
  - Getting the **current date and time** using `datetime.now()`.
  - Extracting specific parts (year, month, day, hour).
  - Creating custom `datetime` objects.

- **Motivational Quote Emailer**:
  - Reads random motivational quotes from a text file.
  - Sends them automatically every Monday.
  - Demonstrates how to combine file handling, random choice, and scheduling logic.

- **Birthday Wisher Automation** 🎂:
  - Reads **birthdays from a CSV file** using Pandas.
  - Sends personalized birthday wishes via email using pre-written templates.
  - Randomly picks one of multiple templates for variety.
  - Automatically runs daily and checks if today matches any birthday.

- **Hosting with PythonAnywhere** 🌐:
  - You can **host and schedule** this script on [PythonAnywhere](https://www.pythonanywhere.com/).  
  - It can automatically **trigger once daily** at your chosen time (e.g., every morning at 8 AM).  
  - No need to keep your computer running — PythonAnywhere executes your script on its cloud server.

---

## 📂 Files Included

### 📨 Email Automation
- `main.py`:  
  - Demonstrates sending a basic email through **SMTP Gmail** using:
    - `connection = smtplib.SMTP("smtp.gmail.com", port=587)`
    - `connection.starttls()` for secure connection.
    - `connection.sendmail()` for sending formatted messages.

### 🕒 Date and Time
- `main2.py`:  
  - Uses the `datetime` module to:
    - Print current date and time.
    - Extract `year`, `month`, and `day`.
    - Create a custom datetime object (e.g., date of birth).

### 💪 Motivational Email Sender
- `main3.py`:  
  - Sends a **random motivational quote** every Monday.  
  - Reads quotes from `quotes.txt`.  
  - Uses `datetime.weekday()` to check if it’s Monday (`weekday == 6`).  
  - Sends the selected quote to a specified email address.

- `quotes.txt`:  
  - Contains a list of **inspirational quotes** by famous authors.  
  - The script randomly selects one each time it runs.

---

### 🎉 Birthday Wisher Project
📁 **birthday wisher/**
- `main.py`:  
  - Reads birthdays from `birthdays.csv`.  
  - Checks if today’s date matches any entry.  
  - If yes:
    - Selects a random letter from `letter_templates/`.
    - Replaces `[NAME]` placeholder with the actual person’s name.
    - Sends a personalized email with the birthday message.

- `birthdays.csv`:  
  - CSV file containing columns: `name, email, year, month, day`.  
  - Example:
    ```csv
    name,email,year,month,day
    Test,test@yahoo.com,1961,2,15
    ```

📁 **letter_templates/**
- `letter_1.txt`, `letter_2.txt`, `letter_3.txt`:  
  - Pre-written birthday messages with a `[NAME]` placeholder.  
  - Example:
    ```
    Dear [NAME],

    Happy birthday!
    All the best for the year!

    Python
    ```

---

## 📝 Summary
On Day 32, I:  
- Learned to **send emails programmatically** with Python’s `smtplib`.  
- Explored **secure connections** using `starttls()` and SMTP port 587.  
- Understood **date and time handling** using `datetime`.  
- Built two practical automation projects:
  - **Motivational Quote Emailer** → sends positive quotes weekly.
  - **Birthday Wisher** → automatically sends personalized greetings.
- Discovered how to host Python scripts online using **PythonAnywhere** for daily execution.

---

## 🚀 Key Learnings
- `smtplib` enables direct email sending through code — no third-party apps needed.  
- Always secure credentials; avoid hardcoding real passwords in production.  
- The `datetime` module is essential for **date-based automation**.  
- Pandas makes reading and filtering CSV data effortless.  
- **Automation + Scheduling** = Practical real-world Python application.  
- Hosting on **PythonAnywhere** allows fully automated daily tasks.

---

## 🔗 Resources Used
- [Python smtplib Documentation](https://docs.python.org/3/library/smtplib.html)  
- [Python datetime Module](https://docs.python.org/3/library/datetime.html)  
- [PythonAnywhere Scheduler Guide](https://help.pythonanywhere.com/pages/ScheduledTasks/)  
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

> 💬 These codes are written as part of my learning journey. While I’ve done my best (with help from online resources), mistakes or bugs are possible. **Feel free to share corrections, suggestions, or improvements!**

> 💡 Part of my #100DaysOfPython challenge. Follow along here: [Here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong)
