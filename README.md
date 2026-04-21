```markdown
# ⚔️ RPG‑Python – A Console‑Based Role‑Playing Game

> A simple RPG built with Python to practice Object‑Oriented Programming (OOP).  
> This project is meant to be fun, collaborative, and a great first step into team development on GitHub.

---

## 📖 Description

The game lets you create a **Player** character, fight **Enemies**, collect **Items** (weapons, potions), and manage an **Inventory**.  
Combat uses a 20‑sided dice roll with critical hits, standard attacks, and occasional fumbles.

It is currently a **turn‑based console prototype** – perfect for learning OOP concepts like classes, inheritance, dataclasses, and static methods.

---

## 🛠️ How to Install (for absolute beginners)

Follow these steps exactly. They work on Windows, macOS, and Linux.

### 1. Clone the repository
Open a terminal (Command Prompt, PowerShell, or Terminal) and run:
```bash
git clone https://github.com/felix3224/rpg-python.git
cd rpg-python
```

### 2. Create a virtual environment (venv)
This keeps dependencies isolated.
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
Currently the project uses **only the Python standard library** – no external packages.  
But we include the `pip install` step so you’re ready for future needs:
```bash
pip install --upgrade pip
# (No extra packages yet)
```
> If you later add a `requirements.txt` file, run `pip install -r requirements.txt`.

---

## 📁 Project Structure (what each file does)

```
rpg-python/
├── README.md          # You are here
├── main.py            # Game entry point – creates player, enemy, items, starts combat
├── character.py       # Defines Character (base), Player, and Enemy (HP, attack, defense)
├── combat.py          # Dice rolling logic and the battle system (attacker vs defender)
├── inventory.py       # Inventory class – add/remove/show items
├── items.py           # Item (abstract), Weapon, Consumable – use() method for each
```

- **`character.py`** – Contains the `Character` dataclass (HP, attack, defense) and the `Player`/`Enemy` subclasses.  
- **`combat.py`**    – Handles dice rolls and the turn‑based attack logic (critical hits, misses).  
- **`inventory.py`** – Manages a list of `Item` objects (add, remove, display).  
- **`items.py`**     – Defines items: `Weapon` (damage) and `Consumable` (heal).  
- **`main.py`**      – The script you run. It creates a sample player, an enemy, some items, and demonstrates combat.

---

## 🎮 How to Play (Usage)

Currently the game is **demonstration‑only** – it runs a fixed scenario to show how classes work together.

To run it:
```bash
python main.py
```

You will see:
- Player and enemy stats printed
- Items being added/removed from the inventory
- Two combat rounds: player attacks enemy, then enemy attacks player

> **No user input yet** – the roadmap below includes plans to make it interactive!

---

## 🧭 Roadmap (where we want to go)

- [ ] **XP & Level Up System**         – Gain experience from defeated enemies, level up to increase stats (HP, attack, defense).  
- [ ] **Equipment System**             – Equip weapons and armor to modify attack/damage and defense.  
- [ ] **Graphical Interface (future)** – Move from the console to a GUI (e.g., Pygame or Tkinter).  

### Stretch goals (ideas for later)
- [ ] Turn‑based menu with choices (attack / use item / run)  
- [ ] Multiple enemy types and a small world map  
- [ ] Save / load game  

---

## 👥 Working as a Team (GitHub basics)

Since this is your first team project, remember this is matter:

1. **Always pull before you push**  
   `git checkout main`
   `git pull origin main`

2. **Create a new branch for each feature**  
   `git checkout -b feature/add-xp-system`

3. **Commit often with clear messages**  
   `git commit -m "Add XP reward when enemy dies"`

4. **Push your branch and open a Pull Request**  
   `git push origin feature/add-xp-system`

5. **Resolve conflicts together** – don’t panic, ask for help.

---

## 📝 License

This project is for learning purposes – feel free to use, modify, and share.

---

**Happy coding & have fun!** 🎲  
If you get stuck, open an **Issue** on GitHub or ask in the team chat.
```
