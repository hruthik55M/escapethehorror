🗝️ Escape Room Game

A Python-based multi-world escape adventure

Welcome to the Escape Room Game, a modular, story-driven puzzle experience built in Python.
The game places the player inside a sequence of themed “worlds,” each with its own logic, clues, and challenges.
Your objective: Solve puzzles, unlock clues, and escape each world to progress to the next.

This project is structured for easy expansion—new worlds, puzzles, and mechanics can be added using the same template.

🚀 Features

Multiple interconnected worlds (world1.py → world5.py)

Centralized game engine to control flow, state, and user input

Clean modular architecture; each world is self-contained


escape-room-game/
│
├── main_game.py
│   └─ Entry point of the game. Initializes the engine, loads worlds, and starts the adventure.
│
├── game_engine.py
│   └─ Core game logic:
│       - Room/world transitions
│       - Puzzle state management
│       - Input/output handling
│       - Game loop functions
│
├── world1.py
│   └─ First escape room:
│       - Introduction to gameplay
│       - Basic puzzle interactions
│
├── world2.py
│   └─ Second escape room:
│       - Increased difficulty
│       - More complex environmental clues
│
├── world3.py
│   └─ Third escape room:
│       - Branching puzzle elements
│       - Multi-step item puzzles
│
├── world4.py
│   └─ Fourth escape room:
│       - Logic-based and code-breaking puzzles
│
├── world5.py
│   └─ Final escape room:
│       - Highest difficulty
│       - Climactic reveal or final challenge
│
└── README.md
    └─ Documentation and game structure overview (this file)






