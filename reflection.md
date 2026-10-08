# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-Enter button pushed------|The game would accept input and run  numerical input in game--|-It is severely deleyaed and only runs when the next input is ran---|This needs to be changed so enter is as responsive as pushing the button|
| guess of 100|too high |too low |would need to be reversed so it reflects the input instead of the opposite |
| guess of 36|go higher |told to go lower |needs to be fixed so it goes the right way |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?Claude/COpilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).The AI made a suggestion for an additional pytest to do with a logic failure involving even numbers
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count. It's test it wanted to run wasnt in the right place and wasnt a pytest

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I tested the bug trigger 
- Describe at least one test you ran (manual or using pytest)  Manual test by playing the game which is how i got the too high too low problem with ai I ran the pytests
  and what it showed you about your code. It showed me a problem in the new logic file I ported over
- Did AI help you design or understand any tests? How? Yes the ai was the one that took my parameters and made a test

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? Its a program that runs codes that doesnt require a gcc powershell window like in some basic C functions

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
The going in and finding hte problem so the ai doesnt waste tokens parsing
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task? I would look throgh the code before I run the program
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It made me think about the requirment to run tests and not trust the ai when it sugggests a change implicty.
