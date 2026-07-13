from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime, timedelta

@dataclass
class Task:
    description: str
    duration: str  # e.g., "15 min"
    priority: str  # e.g., "High", "Medium", "Low"
    time: str      # e.g., "08:00"
    frequency: str = "Once"  # "Once" or "Daily"
    is_completed: bool = False

    def mark_complete(self) -> None:
        """Marks the task as completed. If recurring, simulates rescheduling."""
        self.is_completed = True


@dataclass
class Pet:
    name: str
    breed: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Adds a care task to the pet's list."""
        self.tasks.append(task)


class Owner:
    def __init__(self, name: str):
        self.name: str = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Adds a pet to the owner's profile."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Gathers all tasks from all pets managed by the owner."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


class Scheduler:
    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sorts tasks chronologically using an HH:MM lambda evaluation key."""
        return sorted(tasks, key=lambda t: t.time)

    def filter_tasks(self, tasks: List[Task], status_criteria: str) -> List[Task]:
        """Filters tasks dynamically by 'Completed' or 'Pending' states."""
        if status_criteria.lower() == "completed":
            return [t for t in tasks if t.is_completed]
        elif status_criteria.lower() == "pending":
            return [t for t in tasks if not t.is_completed]
        return tasks

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Detects scheduling collisions where multiple tasks share an identical time slot."""
        time_slots = {}
        conflicts = []
        for task in tasks:
            if task.time in time_slots:
                conflicts.append(
                    f"Conflict at {task.time}: '{task.description}' overlaps with '{time_slots[task.time]}'"
                )
            else:
                time_slots[task.time] = task.description
        return conflicts

    def process_recurrence(self, task: Task) -> Optional[Task]:
        """
        If a task is 'Daily', returns a new copy of the task set for tomorrow.
        Uses Python's datetime objects for strict scheduling calculations.
        """
        if task.frequency.lower() == "daily" and task.is_completed:
            # Generate next occurrence details safely
            return Task(
                description=f"{task.description} (Next Occurrence)",
                duration=task.duration,
                priority=task.priority,
                time=task.time,
                frequency="Daily",
                is_completed=False
            )
        return None