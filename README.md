# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
   # the games purpose is to guess which number the game picked
- [ ] Detail which bugs you found.
   # found several bugs like hints being backwards, negative scores, duplicate that override the check_guess, and difficulty ranges and attempts not adding up/makes no sense.
- [ ] Explain what fixes you applied.
   # applied fixed like removing the duplicate and importing the original function from logic_utils.py to the app.py, this fixed the negative score. fixing some logical errors in the app.py where diffuculty and ranges didnt scale with difficulty.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. enter a guessing number in the box, this is dependent on what difficulty you are in 
2. see if the hint is telling you higher or lower
3. if higher, guess higher. If lower, guess lower
4. if you won or lost, you can click new game to continue
5. <!-- Add more steps as needed -->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.13.15, pytest-9.1.1, pluggy-1.6.0
plugins: anyio-4.15.1
collected 3 items

tests\test_game_logic.py ...                                             [100%]

============================== 3 passed in 0.09s ==============================

```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
