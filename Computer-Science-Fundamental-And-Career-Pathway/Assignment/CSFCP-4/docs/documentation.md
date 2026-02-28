# Project Documentation

## Project overview

A simple and engaging number guessing game implemented in Python. The program picks a random number between 1 and 100, and challenges the player to guess it. With friendly hints, attempt tracking, and replayability, it's a fun little CLI game to enjoy and learn from.

## Development process (how we built it)

This section describes how we built the number guessing game from scratch.

The project was developed as a command-line interface (CLI) game in Python. The development process involved:

- Designing the core game logic to generate a random number between 1 and 100.
- Implementing user input handling with validation to ensure only valid guesses are accepted.
- Providing feedback hints to the player such as "Too high" or "Too low" based on the guesses.
- Tracking the number of attempts to offer a measure of performance.
- Enabling the player to replay the game after each round or exit gracefully.
- Testing the game through multiple rounds to ensure stability and correct behavior.

The code was written in a single Python file (`Game.py`) for simplicity and ease of use and was tested in a terminal environment.

## Future improvements section

- Add difficulty levels with different ranges.
- Add a scoring system based on attempts.
- Implement a graphical user interface (GUI).
- Support multiplayer mode.
