from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Task:
    description: str
    duration: str  # e.g., "30 min"
    priority: str  # e.g., "High", "Medium", "Low"
    time: str      # e.g., "08:00"
    is_completed: bool = False

    def mark_complete(self) -> None:
        pass


@dataclass
class Pet:
    name: str
    breed: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass


class Owner:
    def __init__(self, name: str):
        self.name: str = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        pass

    def get_all_tasks(self) -> List[Task]:
        pass


class Scheduler:
    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        pass

    def filter_tasks(self, tasks: List[Task], criteria: str) -> List[Task]:
        pass

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        pass