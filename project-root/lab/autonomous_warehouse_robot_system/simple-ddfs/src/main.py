from src.system_init import initialize_system
import time

def main():
    # Initialize the system
    system = initialize_system()
    task_assignment = system["task_assignment"]
    robot_state = system["robot_state"]
    task_execution = system["task_execution"]

    # Register robots
    print("\nRegistering robots...")
    robot_state["register_robot"]("robot_1", "picker", {"x": 0, "y": 0})
    robot_state["register_robot"]("robot_2", "transport", {"x": 0, "y": 0})

    # Register robots with task assignment
    task_assignment["register_robot"]("robot_1", "picker")
    task_assignment["register_robot"]("robot_2", "transport")

    # Create example tasks
    pick_task = {
        "type": "pick",
        "priority": 2,
        "data": {
            "item_id": "item_123",
            "location": {"x": 10.0, "y": 5.0}
        }
    }

    transport_task = {
        "type": "transport",
        "priority": 1,
        "data": {
            "item_id": "item_456",
            "weight": 50.0,
            "pickup_location": {"x": 15.0, "y": 8.0},
            "dropoff_location": {"x": 20.0, "y": 12.0}
        }
    }

    # Add tasks
    print("Starting task execution...")
    task_assignment["add_task"]("task_1", pick_task)
    task_assignment["add_task"]("task_2", transport_task)

    # Start task assignment and execution
    while True:
        tasks = task_assignment["get_all_tasks"]()
        print("\nCurrent task status:")
        for task_id, task in tasks.items():
            print(f"Task {task_id}: {task['status']}")

        # Check if all tasks are completed
        all_completed = all(
            task["status"] in ["completed", "failed"]
            for task in tasks.values()
        )

        if all_completed:
            print("\nAll tasks completed")
            break

        # If there are pending tasks, try to assign next task
        task_data = task_assignment["assign_next_task"]()
        if task_data:
            success = task_execution["execute_task"](task_data)
            task_assignment["update_task_status"](task_data["task_id"],
                                                "completed" if success else "failed")
            task_assignment["update_robot_status"](task_data["assigned_robot"], "idle")

        time.sleep(1)  # Simulate processing time

if __name__ == "__main__":
    main()
