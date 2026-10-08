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

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

### Game Purpose

Glitchy Guesser is a number guessing game built with Streamlit. The game picks a secret number in a range set by the difficulty (Easy, Normal or Hard). You guess until you find it or run out of attempts. After each guess the game says "Too High" or "Too Low" and gives a hint in the direction of the secret. Your score goes up or down as you play. The project is an exercise in debugging AI-generated code: the app "worked" when we got it, but it was unplayable.

### Bugs Found

| # | Bug | What I saw |
|---|-----|------------|
| 1 | **Backwards hints** | A guess of 100 said "Too Low", and a guess of 36 (below the secret) said "Go LOWER". The hint messages pointed away from the secret. |
| 2 | **Secret switched between int and string** | On every even attempt, `app.py` turned the secret into a string before comparing. That made Python compare text instead of numbers (`"9" > "50"` is `True`), so the high/low result changed from turn to turn. |
| 3 | **Enter key lagged one turn** | Pressing Enter in the guess box only saved the value. The guess wasn't processed until the next click, so the game always seemed one input behind. |
| 4 | **Status panel showed old values** | The "Attempts left" banner and Developer Debug Info were drawn before the guess was processed, so they showed the previous turn's numbers. |
| 5 | **Logic not testable** | `check_guess` lived inside `app.py`, and `logic_utils.check_guess` only raised `NotImplementedError`, so `pytest` couldn't run. |

### Fixes Applied

- **Hints:** In `logic_utils.check_guess`, "Too High" now goes with "📉 Go LOWER!" and "Too Low" with "📈 Go HIGHER!".
- **Type bug:** `app.py` now always passes `st.session_state.secret` to `check_guess` as an int. I removed the even/odd string conversion and the `TypeError` fallback that covered it up.
- **Enter key:** I put the text input and submit button inside an `st.form` with `clear_on_submit=True`. Pressing Enter now submits the guess on the same rerun and clears the box.
- **Stale status:** The info banner and debug panel are now `st.empty()` placeholders. A `render_status()` function fills them at the end of each run, after the guess is processed.
- **Refactor and tests:** I moved `check_guess` into `logic_utils.py` and `app.py` imports it from there. I rewrote `tests/test_game_logic.py` as a parametrized test that checks the outcome and its hint message together, plus a focused test for the "Too Low" branch.

**Known remaining quirks** (not fixed yet): attempts start at 1 instead of 0, the "Too High" score penalty flips sign on even attempts, and "New Game" and the prompt text always use the 1–100 range whatever the difficulty.

## 📸 Demo Walkthrough

A sample game of the fixed app on **Normal** difficulty (range 1–100, 8 attempts). In this example the secret number, shown under "Developer Debug Info", is **55**.

1. The game starts with a score of 0 and shows "Attempts left: 7".
2. User enters a guess of **40** and presses Enter (or clicks "Submit Guess 🚀").
3. Game returns **"Too Low"** with the hint "📈 Go HIGHER!". Score goes to **-5** and attempts left drops to 6. The input box clears for the next guess.
4. User enters a guess of **70** → game returns **"Too High"** with the hint "📉 Go LOWER!". Score goes to **-10** and attempts left drops to 5.
5. The secret stays at 55 the whole time. The debug panel shows the history `[40, 70]`, and the hints always point toward the secret.
6. User enters a guess of **55** → game returns **"🎉 Correct!"**, balloons appear, and the app shows "You won! The secret was 55. Final score: 40".
7. The game ends after the correct guess. Submitting again shows "You already won. Start a new game to play again." Clicking "New Game 🔁" picks a new secret.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python -m pytest tests/ -v
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0
rootdir: ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collecting ... collected 5 items

tests/test_game_logic.py::test_outcome_and_message_together[50-50-expected0] PASSED [ 20%]
tests/test_game_logic.py::test_outcome_and_message_together[60-50-expected1] PASSED [ 40%]
tests/test_game_logic.py::test_outcome_and_message_together[40-50-expected2] PASSED [ 60%]
tests/test_game_logic.py::test_outcome_and_message_together[9-50-expected3] PASSED [ 80%]
tests/test_game_logic.py::test_else_branch_too_low_says_go_higher PASSED [100%]

============================== 5 passed in 0.03s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
