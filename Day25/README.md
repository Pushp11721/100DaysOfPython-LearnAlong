# 📅 Day 25 - Python Learning Log

## 🧠 Topics Covered
- **Working with CSV Files**:
  - Using the `csv` module to read rows and extract values.
  - Transitioning to `pandas` for simpler and more powerful data analysis.
  - Converting data to lists and dictionaries.
  - Calculating statistics with `pandas`:  
    - Mean  
    - Maximum  
    - Filtering rows based on conditions.
  - Creating a new DataFrame from scratch and saving it as a CSV.

- **Squirrel Census Challenge**:
  - Analyzing the **2018 Central Park Squirrel Census** dataset.
  - Counting squirrels by fur color (Gray, Cinnamon, Black).
  - Exporting results to CSV files (`squirrel_count.csv` and `squirrel_count1.csv`).

- **U.S. States Game Project**:
  - Using `turtle` graphics and `pandas`.
  - Interactive quiz: guess the 50 U.S. states.
  - Write guessed states directly on the map.
  - Generate a list of **missed states** (`missed_state.csv`) for practice.

---

## 📂 Files Included

### 🔹 Core Learning Scripts
- `main.py`:  
  - First step: reading weather data with both `csv` and `pandas`.  
  - Prints temperatures from `weather_data.csv`.

- `main2.py`:  
  - Converts DataFrame to dictionary.  
  - Calculates average and maximum temperatures.  
  - Filters rows (e.g., Monday’s weather, hottest day).  
  - Creates a new DataFrame (`scratch_data.csv`).

- `main3.py`:  
  - Counts squirrel fur colors using a simple approach.  
  - Saves counts into `squirrel_count.csv`.

- `main3.1.py`:  
  - Optimized fur color counting with conditions.  
  - Saves results into `squirrel_count1.csv`.

---

### 🔹 Datasets
- `weather_data.csv`: Daily temperature and condition records.  
- `2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250115.csv`: Large dataset (~3000 rows).  
- `scratch_data.csv`: Student scores (generated via pandas).  
- `squirrel_count.csv` & `squirrel_count1.csv`: Processed squirrel fur color counts.

---

### 🎮 U.S. States Game Project
Located in the **`Project/`** folder.

- `main.py`:  
  - Core game script using `turtle` for GUI and `pandas` for data.  
  - Tracks correct guesses and updates the map in real time.  
  - Exiting the game generates `missed_state.csv`.

- `50_states.csv`:  
  - Contains state names with x,y coordinates for map placement.

- `missed_state.csv`:  
  - Auto-generated file of unguessed states for revision.

- `blank_state_img.gif`:  
  - Map background used in the game.

---

## 📝 Summary
On Day 25, I:  
- Learned how to work with **CSV files** using both `csv` and `pandas`.  
- Practiced filtering and analyzing data with simple conditions.  
- Completed the **Squirrel Census Challenge** to analyze real-world data.  
- Built my **first interactive game with data**: the **U.S. States Guessing Game** using `turtle`.  

---

## 🚀 Key Learnings
- `pandas` makes data handling much easier than manual `csv` reading.  
- Mean and max can be calculated directly with built-in DataFrame methods.  
- Conditional filtering is a powerful way to query datasets.  
- Real datasets (like the Squirrel Census) give practical data analysis experience.  
- Combining `pandas` + `turtle` can create fun, educational projects.  

---

## 🔗 Resources Used
- [Pandas Documentation](https://pandas.pydata.org/docs/)  
- [Reading CSVs in Python - GeeksforGeeks](https://www.geeksforgeeks.org/reading-csv-files-in-python/)  
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)  

---

> 💬 These codes are part of my hands-on learning.  
> If you spot bugs or have suggestions, feel free to contribute or share feedback!  

> 💡 Part of my #100DaysOfPython challenge. Follow along here: [Here](https://github.com/Pushp11721/100DaysOfPython-LearnAlong)
