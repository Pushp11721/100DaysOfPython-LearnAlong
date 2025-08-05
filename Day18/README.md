# 📅 Day 18 - Python Learning Log

## 🧠 Topics Covered
- Drawing with the **Turtle graphics** module
- Using **loops, pen control**, and **color changes** to draw shapes
- Drawing:
  - Squares
  - Dashed lines
  - Polygons (3 to 9 sides)
  - Random walks
  - Spirographs
- Using **RGB color tuples** with randomization
- **Hirst Painting Project**:
  - Extracting colors from an image using `colorgram` (commented out)
  - Using `dot()` function to create a grid of colored dots
  - Setting turtle position using `setposition()` and movement logic

## 📂 Files Included

### 🔸 Turtle Drawing Practice
- `main.py`:  
  - Basic turtle object setup.
  - Draws a square using a loop.

- `Lec2.py`:  
  - Draws dashed lines using `penup()` and `pendown()` for controlled strokes.

- `Lec3.py` & `Lec3.1.py`:  
  - Defines functions to draw polygons with increasing sides and random colors.

- `Lec4.py`:  
  - Simulates a **random walk** with varying turtle heading and colors.
  - Uses `pensize()` and `speed()` for visual styling.

- `Lec5.py`:  
  - Creates a **Spirograph** by repeatedly drawing circles while changing heading by 5 degrees.
  - Uses RGB values with `pencolor()`.

### 📁 Hirst Painting Project
- `main.py`:  
  - (Commented out) Color extraction from `image.jpg` using `colorgram`.
  - Contains a predefined `color_list` of RGB tuples extracted from image for dot painting.

- `hirst_painting.py`:  
  - Uses the `color_list` to draw a 10x10 grid of dots with `turtle.dot()`.
  - Implements precise turtle movement using `penup()`, `setposition()`, and looped navigation.

- `image.jpg`:  
  - Image file used for extracting dominant colors (optional asset for running colorgram extraction).

## 📝 Summary
On Day 18, I explored the **Turtle graphics** module in-depth to build interactive and colorful visualizations:
- Practiced drawing basic shapes with loops.
- Learned to control the pen (on/off), stroke thickness, turtle movement and speed.
- Built patterns like dashed lines, spirographs, and random walks using mathematical angles.
- Implemented a small project based on **Hirst dot painting**, using color data from an image to build a grid of colored dots.

## 🚀 Key Learnings
- Turtle graphics is a great way to visually understand **loops**, **functions**, and **modular drawing**.
- Random color generation can be done using RGB values scaled to 0–1 range.
- Drawing complex visuals like spirographs or Hirst paintings involves **coordination between loops and position handling**.
- `turtle.dot()` is useful for dot painting, and precise movement is controlled via `penup()`, `goto()`, and `setposition()`.

## 🔗 Resources Used
- [Turtle Graphics Documentation – Python](https://docs.python.org/3/library/turtle.html)
- [Colorgram.py for Color Extraction](https://pypi.org/project/colorgram.py/)
- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

> 💬 These codes are written as part of my hands-on learning. Bugs, suggestions, or contributions are always welcome!

> 💡 This is part of my #100DaysOfPython challenge. Follow the journey on GitHub: [Pushp11721/100DaysOfPython-LearnAlong](https://github.com/Pushp11721/100DaysOfPython-LearnAlong)
