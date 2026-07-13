import pytest
from pawpal_system import Owner, Pet, Task, Scheduler

def test_task_completion():
    """Verify that calling mark_complete() changes the task's status."""
    task = Task(description="Give Vitamins", duration="5 min", priority="Medium", time="09:00")
    assert task.is_completed is False
    
    task.mark_complete()
    assert task.is_completed is True

def test_task_addition():
    """Verify that adding a task to a Pet increases that pet's task count."""
    pet = Pet(name="Max", breed="Golden Retriever", age=3)
    task = Task(description="Morning Feeding", duration="15 min", priority="High", time="08:00")
    
    assert len(pet.tasks) == 0
    pet.add_task(task)
    assert len(pet.tasks) == 1
    assert pet.tasks[0].description == "Morning Feeding"

def test_scheduler_sorting():
    """Verify tasks are returned in strict chronological order regardless of addition sequence."""
    scheduler = Scheduler()
    task_late = Task(description="Evening Walk", duration="30 min", priority="High", time="18:00")
    task_early = Task(description="Morning Feeding", duration="15 min", priority="High", time="08:00")
    task_midday = Task(description="Luna Midday Meds", duration="5 min", priority="Medium", time="12:00")
    
    sorted_result = scheduler.sort_by_time([task_late, task_early, task_midday])
    assert sorted_result[0].time == "08:00"
    assert sorted_result[1].time == "12:00"
    assert sorted_result[2].time == "18:00"

def test_conflict_detection():
    """Verify that the Scheduler flags duplicate times with a warning string."""
    scheduler = Scheduler()
    task1 = Task(description="Luna Midday Meds", duration="5 min", priority="Medium", time="12:00")
    task2 = Task(description="Afternoon Grooming", duration="20 min", priority="Low", time="12:00")
    
    conflicts = scheduler.detect_conflicts([task1, task2])
    assert len(conflicts) == 1
    assert "Conflict at 12:00" in conflicts[0]

def test_status_filtering():
    """Verify that filtering by completion state correctly groups items."""
    scheduler = Scheduler()
    t1 = Task(description="Task 1", duration="10m", priority="Low", time="09:00", is_completed=True)
    t2 = Task(description="Task 2", duration="10m", priority="Low", time="10:00", is_completed=False)
    tasks = [t1, t2]
    
    completed_tasks = scheduler.filter_tasks(tasks, "completed")
    pending_tasks = scheduler.filter_tasks(tasks, "pending")
    
    assert len(completed_tasks) == 1
    assert completed_tasks[0].description == "Task 1"
    assert len(pending_tasks) == 1
    assert pending_tasks[0].description == "Task 2"