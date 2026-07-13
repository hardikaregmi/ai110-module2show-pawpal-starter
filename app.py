import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

# Initialize Application Memory
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Hardika")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+ Smart Dashboard")

# 1. Profiles Management Section
st.subheader("👤 Manage Profiles")
col_owner, col_pet, col_breed, col_age = st.columns(4)

with col_owner:
    owner_name = st.text_input("Owner Name", value=st.session_state.owner.name)
    st.session_state.owner.name = owner_name  

with col_pet:
    pet_name = st.text_input("Pet Name", value="Max")
with col_breed:
    pet_breed = st.text_input("Breed/Species", value="Golden Retriever")
with col_age:
    pet_age = st.number_input("Age", min_value=0, max_value=30, value=3)

if st.button("➕ Add Pet Profile"):
    if pet_name and not any(p.name == pet_name for p in st.session_state.owner.pets):
        new_pet = Pet(name=pet_name, breed=pet_breed, age=int(pet_age))
        st.session_state.owner.add_pet(new_pet)
        st.success(f"Registered {pet_name} successfully!")
    elif any(p.name == pet_name for p in st.session_state.owner.pets):
        st.warning(f"'{pet_name}' is already registered.")

if st.session_state.owner.pets:
    st.markdown("**Registered Pets:** " + ", ".join([f"{p.name} ({p.breed})" for p in st.session_state.owner.pets]))
else:
    st.info("No pet profiles added yet.")

st.divider()

# 2. Task Management Section with Frequency Selection
st.subheader("📅 Schedule Care Tasks")

if not st.session_state.owner.pets:
    st.warning("Please add at least one pet profile above before adding tasks.")
else:
    target_pet_name = st.selectbox("Assign Task To", [p.name for p in st.session_state.owner.pets])
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        task_desc = st.text_input("Task Description", value="Morning Feeding")
    with col2:
        task_dur = st.text_input("Duration", value="15 min")
    with col3:
        task_pri = st.selectbox("Priority Level", ["High", "Medium", "Low"])
    with col4:
        task_time = st.text_input("Time (HH:MM)", value="08:00")
    with col5:
        task_freq = st.selectbox("Frequency", ["Once", "Daily"])

    if st.button("📥 Add Task to System"):
        selected_pet = next((p for p in st.session_state.owner.pets if p.name == target_pet_name), None)
        if selected_pet:
            new_task = Task(
                description=task_desc, 
                duration=task_dur, 
                priority=task_pri, 
                time=task_time,
                frequency=task_freq
            )
            selected_pet.add_task(new_task)
            st.success(f"Added {task_freq} task '{task_desc}' for {target_pet_name}!")

st.divider()

# 3. Dynamic Engine & Advanced Controls
st.subheader("📋 Build Master Schedule")

# Filter controls
filter_status = st.radio("Filter Schedule By Status:", ["All", "Pending", "Completed"], horizontal=True)

if st.button("🚀 Generate and Process Plan"):
    all_tasks = st.session_state.owner.get_all_tasks()
    
    if not all_tasks:
        st.info("No tasks found in the database. Schedule tasks above first!")
    else:
        # Run algorithmic conflict check
        conflicts = st.session_state.scheduler.detect_conflicts(all_tasks)
        if conflicts:
            for conflict in conflicts:
                st.warning(f"⚠️ {conflict}")
        else:
            st.success("🟢 Complete system check clean! No scheduling overlaps detected.")

        # Filter implementation
        filtered_tasks = all_tasks
        if filter_status != "All":
            filtered_tasks = st.session_state.scheduler.filter_tasks(all_tasks, filter_status)

        # Chronological sorting algorithmic key
        sorted_tasks = st.session_state.scheduler.sort_by_time(filtered_tasks)
        
        # Display Engine Timetable Layout
        st.markdown(f"### Daily Agenda for {st.session_state.owner.name}'s Household")
        
        display_data = []
        for task in sorted_tasks:
            display_data.append({
                "Time": task.time,
                "Task Details": task.description,
                "Duration": task.duration,
                "Priority": task.priority,
                "Frequency": task.frequency,
                "Status": "Completed ✅" if task.is_completed else "Pending ⏳"
            })
        st.table(display_data)