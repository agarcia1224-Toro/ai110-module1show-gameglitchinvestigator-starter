# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  the game seemed to run fine when I input my guess for the numbers, however the logic didnt make sense for when I was trying to further make my guesses.
- List at least two concrete bugs you noticed at the start  
  One major bug I found was the game not allowing the player to make a new game once the game was over. The score would give a negative score, and the difficulty setting would not apply the proper difficulty level.
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| input for new game | make new game while keeping score| nothing happened | failed to make new game |
| hints | hints tell correct hint | hints were backwards | none |
| score input | score input possitive| score was negative| score is not adding up|
| difficulty | difficulty change | no changed happened | failed to change difficulty along with guesses and number range|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  # I used the built in chat for vscode, so most likely chat.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  # when I asked about the hints being backwards, it it found a duplicate check_guess function, so it suggested removing the duplicate because it was overiding the correct version
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  # one example was when I asked about the difficulty and attempts, it gave new values instead of tweaking the already existing values. like swapping the ranges for difficulty (normal was 1-100) (hard was 1-50) but it suggested (normal 1-100) and (hard 1-200)

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  # tested it by running the code and also verifying with the chat
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  # one thing I tested was the difficulty range not matching up with the hints
- Did AI help you design or understand any tests? How?
  # yes, because when I asked about the suggested fixes and saw what it changed, if the manual test made sense to me, I kept the changes
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  # a bit confusing at first when starting out, but when you run the code, it makes the "game" in the browser and you can see what changes the code made to that user interface

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  # constantly keeping track of changes and what certain things changed
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
  # be more specific in promts, also to ask what the changes are doing
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  # AI generated code helped me see bugs when I describe the bug to the AI, if I had a problem with hints lying to me, then the AI would take a look and show me where the hint logic and explain what the change would do