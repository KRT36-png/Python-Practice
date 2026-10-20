# Terminal Grid Game

A Python-based terminal game built to explore grid-based movement, procedural map generation, and pathfinding.

## About

This project is a grid-based game where the player navigates a map containing obstacles and energy pickups while avoiding an enemy. The map is generated with randomized elements, making each run a little different.

The project was built as a hands-on exercise in Python programming, game logic, and algorithm implementation.

## Features

- **Grid-based movement** — Navigate the map using keyboard controls.
- **Procedural map generation** — Obstacles and energy pickups are placed randomly.
- **Energy system** — Movement consumes energy, adding a resource-management element.
- **Enemy AI** — Uses Breadth-First Search (BFS) to find a shortest path toward its target on the grid.
- **Score tracking** — Keep track of progress during a run.

## Controls

| Key | Action |
|---|---|
| `W` | Move up |
| `A` | Move left |
| `S` | Move down |
| `D` | Move right |

## Technologies

- Python
- Standard Python libraries

## Running the Game

1. Make sure Python is installed.
2. Clone or download this repository.
3. Navigate to the project directory.
4. Run:

   ```bash
   python main.py
   ```

   Depending on your installation, you may need to use `python3 main.py` instead.

## What I Learned

- Representing a game world using a two-dimensional grid.
- Implementing Breadth-First Search for shortest-path navigation.
- Working with randomized map elements and game-state updates.
- Organizing game mechanics into executable Python logic.
- Handling movement, obstacles, and resource constraints.

## Future Improvements

- Refactor the game into smaller, more maintainable modules.
- Improve enemy behaviour and decision-making.
- Expand map generation and gameplay mechanics.
- Add more robust handling of edge cases.

## Project Status

**Work in progress.**

This is a learning project, and its design and mechanics may change as I experiment with new ideas and improve the implementation.
