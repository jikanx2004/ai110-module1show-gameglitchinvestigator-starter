# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The first time I ran it, the game looked normal: it had a title, a guess box, buttons and a debug panel. It fell apart once I started playing. The hints sent me the wrong way, so I couldn't zero in on the secret even with the debug panel open. Pressing Enter didn't seem to do anything until I made my next input, so the game always felt one step behind. Together these made the game basically unwinnable without cheating off the debug panel.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Type a guess and press **Enter** | The guess is submitted right away, just like clicking "Submit Guess" | Nothing happens until the next input; then the previous guess is processed | No error. Enter only stored the value, and the guess wasn't processed until the next rerun |
| Guess of **100** (secret below 100) | "Too High" | "Too Low" | No error. The outcome and hint text were swapped in `check_guess` |
| Guess of **36** (secret above 36) | "📈 Go HIGHER!" | Told to "Go LOWER" | No error. The hint pointed away from the secret |
| Same kind of guess on an **even-numbered attempt** | Same high/low result as any other attempt | Result could flip, because the secret was turned into a string on even attempts | No error. A `TypeError` fallback hid it by comparing strings (`"9" > "50"` is `True`) |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude and GitHub Copilot in VS Code.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

The AI suggested adding a pytest for a logic failure involving even numbers, the case where the secret was turned into a string on even attempts. That pointed me to the real bug: comparing an int to a string gave the wrong high/low answer. I verified the fix by running `pytest` (all tests passed) and by playing several rounds and checking that the hints stayed consistent from one attempt to the next.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

The AI suggested a test that wasn't written as a pytest and wasn't in the right place: it wasn't in `tests/test_game_logic.py`, where `pytest` would find it. I didn't use it as written. Instead I had the test rewritten as a proper pytest function in the tests file, checking the outcome and the hint message together. I verified it by running `pytest` and seeing the new test collected and passing alongside the others.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I treated a bug as fixed only once I could repeat the exact input that triggered it and get the right behavior. For example, I re-entered a guess of 100 and a guess of 36 and checked that the hints now pointed toward the secret. I also pressed Enter instead of clicking the button to make sure the guess went through right away.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

My first test was manual: I played the game with the debug panel open, which is how I found the too high / too low problem. After moving `check_guess` into `logic_utils.py`, I ran `pytest`, and it exposed a problem in the newly moved logic: the outcome and hint message weren't paired correctly. After the fix, all 5 tests pass, including the cases for a win, too high, too low, and a guess far below the secret.

- Did AI help you design or understand any tests? How?

Yes. I described the cases I wanted to check (the guess, the secret and the expected result), and the AI turned them into a parametrized pytest. This let me add new cases as one line each instead of writing a new function every time. It also suggested checking the outcome and the message together, which is exactly what caught the backwards hints.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit runs your whole Python script from top to bottom every time the user does anything, like clicking a button or submitting a form. That's a "rerun." Normal variables get reset on every rerun, so if you stored the secret number in a regular variable, it would be re-randomized on every click. `st.session_state` is like a backpack that survives reruns, so the secret, attempts, score and history are kept there. Order matters too: if the page shows "Attempts left" before the code that processes the guess, it shows last turn's number. That's why I moved the status display to the end of the script.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

I want to keep finding the problem area myself before asking the AI. When I pointed it at the specific function or lines, like the column layout and submit button, it gave faster and more accurate answers and didn't waste tokens reading the whole project.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time I would read through the code before running the program. Some of these bugs, like the even-attempt string conversion, were visible right in the source, and I would have spotted them sooner by reading than by playing.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

AI-generated code can look finished and still be badly broken, so I shouldn't trust a change just because the AI suggests it confidently. Now I see running tests and checking the behavior myself as a required step, not an optional one.
