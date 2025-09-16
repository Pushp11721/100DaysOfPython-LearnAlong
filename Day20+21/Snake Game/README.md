# 🐍 Snake Game (Python + Turtle)

A simple and fun Snake Game built using Python's **Turtle graphics library**.  
The game keeps track of the **current score** and saves the **high score** in a text file.

---

## 🎮 Features
- Classic Snake gameplay with arrow key controls
- Food appears at random locations 🍎
- Scoreboard with **persistent High Score**
- Collision detection with:
  - Walls 🧱
  - Snake’s own body 🐍
- Fun, addictive, and beginner-friendly!

---

## 📂 Project Structure
Snake-Game/
- 'main.py': # Main game loop
- 'snake.py': # Snake class (movement, growth, reset)
- 'food.py': # Food class (random placement)
- 'scoreboard.py': # Scoreboard (score + high score)
- 'data.txt': # Stores high score

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/snake-game.git
   cd snake-game
2. Run the game:
   ```bash
   python main.py
3. Control the snake using your WASD Keys:
   ⬆️ W
   ⬇️ S
   ⬅️ A
   ➡️ D
   
## 📌 Requirements
- Python 3.x
- turtle module (comes pre-installed with Python)

## 🏆 High Score System
- The game saves the highest score in data.txt.
- If you beat the high score, it automatically updates the file.
- Your record is safe even after exiting the game.

## 🤝 Contributing
- Pull requests are welcome!
- For major changes, please open an issue first to discuss what you would like to improve.

## ⚠️ Disclaimer
- This is a learning project created while practicing Python.
- I referred to multiple resources, tutorials, and guides to build this game.
- It is not an entirely original project and should be considered part of my learning journey in programming.
