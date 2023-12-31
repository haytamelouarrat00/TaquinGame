# Taquin Puzzle Game with AI Solver

## Overview
This project implements a classic Taquin (also known as the sliding puzzle) game in Python, enhanced with an AI solver. The game is played on a 3x3 grid where eight numbered tiles and one blank space are arranged randomly. The player can slide tiles into the blank space to reorder them. The goal is to arrange the tiles in ascending order with the blank space at the end.

## Features
- Interactive text-based user interface to play the game.
- An AI solver using the A* search algorithm to automatically solve the puzzle.
- Heuristic-based solution finding with the Manhattan distance metric.
- Solvability check to ensure puzzles are solvable before the game starts.

## Requirements
- Python 3.x

## Setup and Installation
1. Clone or download this repository to your local machine.
2. Ensure Python 3.x is installed on your system.

## Usage
To play the game, run the script from the command line:

```bash
python taquin_game.py
    