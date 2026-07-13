from pawpal_system import Owner, Pet, Task, Scheduler

def run_demo():
    print("🐾 --- PawPal+ CLI Demo Setup --- 🐾\n")
    
    # 1. Initialize Owner and Pets
    owner = Owner(name="Hardika")
    pet1 = Pet(name="Max", breed="Golden Retriever", age=3)
    pet2 = Pet(name="Luna", breed="Siamese Cat", age=2)
    
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    print(f"Created owner '{owner.name}' with pets: {pet1.name} ({pet1.breed}) and {pet2.name} ({pet2.breed}).")

    # 2. Add Care Tasks (intentionally out of chronological order to test sorting)
    task1 = Task(description="Evening Walk", duration="30 min", priority="High", time="18:00")
    task2 = Task(description="Morning Feeding", duration="15 min", priority="High", time="08:00")
    task3 = Task(description="Luna Midday Meds", duration="5 min", priority="Medium", time="12:00")
    task4 = Task(description="Afternoon Grooming", duration="20 min", priority="Low", time="12:00")  # Intentional duplicate time

    pet1.add_task(task1)
    pet1.add_task(task2)
    pet2.add_task(task3)
    pet2.add_task(task4)
    print(f"Added {len(owner.get_all_tasks())} total tasks across all pets.\n")

    # 3. Use Scheduler to organize the day
    scheduler = Scheduler()
    all_tasks = owner.get_all_tasks()

    # Test Sorting
    sorted_tasks = scheduler.sort_by_time(all_tasks)
    
    print("📋 Today's Master Chronological Schedule:")
    print("-" * 45)
    for task in sorted_tasks:
        status = "✅" if task.is_completed else "⏳"
        print(f" [{status}] {task.time} — {task.description} ({task.duration}) [Priority: {task.priority}]")
    print("-" * 45 + "\n")

    # Test Conflict Detection
    print("⚠️  Running System Conflict Check...")
    conflicts = scheduler.detect_conflicts(all_tasks)
    if conflicts:
        for conflict in conflicts:
            print(f"  [WARNING] {conflict}")
    else:
        print("  🟢 No scheduling conflicts detected!")

if __name__ == "__main__":
    run_demo()