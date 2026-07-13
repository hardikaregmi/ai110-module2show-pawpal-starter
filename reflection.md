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

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
