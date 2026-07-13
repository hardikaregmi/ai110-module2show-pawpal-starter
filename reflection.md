# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
My initial design centers around four primary classes, separating data storage from scheduling execution.
- What classes did you include, and what responsibilities did you assign to each?
Owner: Tracks user information and acts as a container managing multiple pets.
Pet: Holds individual pet profiles (name, breed, age) and maintains their specific list of daily tasks.
Task: A simple data object representing a care activity, storing critical tracking properties like description, duration, and priority level.
Scheduler: The operational engine of the app. It retrieves tasks across all pets, resolves scheduling logic, sorts items by priority, and ensures everything fits within given time limits.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
N/A - Currently in the initial design phase. No structural changes made to the skeleton yet.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
The scheduler primarily considers two core constraints: Time (the specific `HH:MM` timestamp assigned to a care task) and Priority (`High`, `Medium`, or `Low`). It uses the time constraint to strictly sort the daily itinerary chronologically and flag exact scheduling conflicts, while the priority level helps the owner visually assess which tasks take precedence during a busy day.

- How did you decide which constraints mattered most?
Time was designated as the absolute primary constraint because a pet schedule is fundamentally a timeline. Without chronological structure, an owner cannot easily plan their day or ensure time-sensitive tasks (like medication or feeding routines) happen when they are supposed to. Priority was chosen as the secondary constraint to give the owner immediate visibility into non-negotiable tasks if their schedule becomes overcrowded.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
While designing the Scheduler engine, a deliberate tradeoff was made to keep the conflict detection logic lightweight. The system currently flags collisions based on exact time matches (e.g., two tasks sharing the same starting hour and minute string). 

- Why is that tradeoff reasonable for this scenario?
The Benefit: This approach is computationally efficient ($O(N)$ runtime lookup via dictionary keys) and provides clear, non-blocking warning strings to the user without crashing the application state or locking the UI thread.
The Limitation: It does not account for overlapping durations (e.g., a 45-minute walk starting at 08:00 would not mathematically block a second task scheduled for 08:15). In a future production iteration, parsing the times into true datetime objects to check interval overlaps ($[\text{start}, \text{start} + \text{duration}]$) would provide more robust coverage.
---

## 3. AI Collaboration

**a. How you used AI**
* **How did you use AI tools during this project?**
  I used AI across the entire lifecycle: generating the initial Mermaid.js UML layout from natural language constraints, scaffolding structural dataclass stubs in Python, refactoring nested loop logic into efficient lookup dictionaries, and constructing a comprehensive automated test suite.
* **What kinds of prompts or questions were most helpful?**
  Granular, context-focused prompts were the most effective. For instance, asking *"How can I use Python's built-in sorted() with a lambda key to parse HH:MM strings chronologically?"* provided actionable, highly tailored code blocks without unnecessary bloat.

**b. Judgment and verification**
* **Describe one moment where you did not accept an AI suggestion as-is.**
  When initially generating the Streamlit UI configuration, the AI suggested structural logic that re-instantiated the primary data structures on every thread execution loop. 
* **How did you evaluate or verify what the AI suggested?**
  Knowing that Streamlit runs scripts from top to bottom on user interaction, I caught that this would wipe user inputs. I modified the suggestion to wrap our data classes properly within the persistent `st.session_state` cache engine to maintain database integrity.

---

## 4. Testing and Verification

**a. What you tested**
* **What behaviors did you test?**
  I explicitly tested underlying model tracking states (`add_task`, `mark_complete`), strict chronological ordering functionality (`sort_by_time`), isolated time-slot duplication tracking (`detect_conflicts`), and future date generation copy routines (`process_recurrence`).
* **Why were these tests important?**
  They validate our algorithmic backend independent of the presentation layout. Ensuring our logic is resilient under the hood guarantees the application won't break if we overhaul the front-end design later.

**b. Confidence**
* **How confident are you that your scheduler works correctly?**
  ⭐⭐⭐⭐⭐ (5/5 Stars). The test suite passes perfectly, confirming all core application logic functions reliably.
* **What edge cases would you test next if you had more time?**
  I would test boundary and input validation limits—such as evaluating how the time engine handles broken or invalid time string formats (e.g., `25:00` or `8:0am`) and testing sorting constraints on empty arrays.

---

## 5. Reflection

**a. What went well**
* **What part of this project are you most satisfied with?**
  I am incredibly satisfied with how cleanly the backend logic binds to the interactive Streamlit UI. Seeing exact warnings pop up dynamically on the dashboard screen when task times collide is incredibly rewarding.

**b. What you would improve**
* **If you had another iteration, what would you improve or redesign?**
  I would upgrade the scheduling engine to support continuous interval processing rather than exact match tracking. This would let the app parse durations to ensure overlapping windows are caught dynamically.

**c. Key takeaway**
* **What is one important thing you learned about designing systems or working with AI on this project?**
  I learned that AI is a powerful accelerator, but human architectural oversight remains critical. The developer must act as a precise director—defining relationships, managing execution state lifecycles, and carefully auditing code to ensure optimal performance.