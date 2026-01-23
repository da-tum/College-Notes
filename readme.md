# Number Guessing Game

## GitHub Description
A simple and engaging number guessing game implemented in Python. The program picks a random number between 1 and 100, and challenges the player to guess it. With friendly hints, attempt tracking, and replayability, it's a fun little CLI game to enjoy and learn from.

## Installation
Make sure you have Python installed on your system. You can download it here: [python.org](https://www.python.org/downloads/).

Clone this repository or download the `Game.py` file directly to your local machine.

## GitHub Commands and Workflow

Here are common GitHub commands to work with this project repository:

- Clone the repository:
  ```
  git clone https://github.com/your-username/number-guessing-game.git
  ```
- Change directory into the repo:
  ```
  cd number-guessing-game
  ```
- Check the repository status:
  ```
  git status
  ```
- View recent commits and history:
  ```
  git log
  ```
- Fetch updates from remote repository:
  ```
  git fetch
  ```
- Merge fetched updates into current branch:
  ```
  git merge origin/main
  ```
- Check differences between files or commits:
  ```
  git diff
  ```
- Stash any uncommitted changes temporarily:
  ```
  git stash
  ```
- Apply stashed changes back to working directory:
  ```
  git stash apply
  ```
- Reset changes in working directory or specific files:
  ```
  git reset HEAD <file>
  ```
- Add changes for commit:
  ```
  git add .
  ```
- Commit changes with a message:
  ```
  git commit -m "Your descriptive commit message"
  ```
- Push changes to a remote branch:
  ```
  git push origin your-branch-name
  ```
- Create a new branch for development:
  ```
  git checkout -b feature-branch-name
  ```
- Switch between branches:
  ```
  git checkout branch-name
  ```
- Pull latest changes from remote:
  ```
  git pull origin main
  ```
- Manage remote repositories:
  ```
  git remote -v
  git remote add origin <url>
  ```

## Usage
1. Open your terminal or command prompt.
2. Navigate to the directory containing the `Game.py` file.
3. Run the game using the command:
   ```
   python Game.py
   ```
4. Follow the prompts in the console to play the game.
5. Enter your guesses when asked and try to find the random number.
6. After winning, you can choose to play another round or exit.

## Features
- Random number generation between 1 and 100.
- Input validation to ensure valid guesses.
- Friendly hints ("Too high", "Too low").
- Attempt counting.
- Option to play multiple rounds.
- Graceful exit when the player chooses not to play again.

## Future Improvements
- Add difficulty levels with different ranges.
- Add a scoring system based on attempts.
- Implement a graphical user interface (GUI).
- Support multiplayer mode.

## Sample Interaction

![Sample Interaction](/Assets/image.png)

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Make a guess: 50
Too low. Try again!
Make a guess: 75
Too high. Try again!
Make a guess: 62
Congratulations! You guessed the number in 3 attempts.
Would you like to play again? (y/n): n
Thanks for playing! Goodbye!

```

## Git Comamdns Used in this File
![Git1](/Assets/git-cmd01.png)
![Git2](/Assets/git-cmd02.png)
![Git3](/Assets/git-cmd03.png)
![Git4](/Assets/git-cmd04.png)
![Git5](/Assets/git-cmd05.png)
![Git6](/Assets/git-cmd06.png)
![Git7](/Assets/git-cmd07.png)
