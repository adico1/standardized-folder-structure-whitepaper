from src.system_init import initialize_system
from src.tasks.pick_task import PickTask
from src.tasks.transport_task import TransportTask
import time

def main():
    # Initialize the system
    system = initialize_system()
    task_manager = system["task_manager"]

    print("\nStarting task execution...")

    # Create some example tasks
    pick_task = PickTask(
        task_id="pick_1",
        item_id="item_123",
        location={"x": 10.0, "y": 5.0},
        priority=2
    )

    transport_task = TransportTask(
        task_id="transport_1",
        item_id="item_456",
        weight=50.0,
        pickup_location={"x": 15.0, "y": 8.0},
        dropoff_location={"x": 20.0, "y": 12.0},
        priority=1
    )

    # Add tasks to task manager
    task_manager.add_task(pick_task)
    task_manager.add_task(transport_task)

    # Start task execution
    while task_manager.task_queue:
        print("\nCurrent task status:")
        for task_id, task in task_manager.tasks.items():
            print(f"Task {task_id}: {task.status}")

        success = task_manager.assign_next_task()
        if success is None:
            print("No tasks could be assigned")
        time.sleep(1)  # Simulate time passing

    print("\nAll tasks completed")

if __name__ == "__main__":
    main()
