from typing import Dict, List, Any
from ..communication.event_dispatcher import EventDispatcher

def create_task_assignment_module(event_dispatcher: EventDispatcher):
    tasks: Dict[str, Dict[str, Any]] = {}
    robot_status: Dict[str, str] = {}
    task_queue: List[str] = []

    def add_task(task_id: str, task_data: Dict[str, Any]):
        tasks[task_id] = {
            **task_data,
            "status": "pending",
            "assigned_robot": None
        }
        task_queue.append(task_id)
        _sort_task_queue()

        event_dispatcher.dispatch("task_added", {
            "task_id": task_id,
            "task_data": task_data
        })

    def assign_next_task():
        available_robots = [
            robot_id for robot_id, status in robot_status.items()
            if status == "idle"
        ]

        print(f"\nAvailable robots: {available_robots}")
        print(f"Current task queue: {task_queue}")
        print(f"Robot status: {robot_status}")

        if not available_robots or not task_queue:
            print("No compatible robot available")
            return None

        task_id = task_queue[0]
        task_data = tasks[task_id]
        task_type = task_data["type"]

        # Match task type with robot type
        compatible_robot = None
        for robot_id in available_robots:
            if (task_type == "pick" and robot_id == "robot_1") or \
               (task_type == "transport" and robot_id == "robot_2"):
                compatible_robot = robot_id
                break

        if not compatible_robot:
            print(f"No compatible robot available for task type {task_type}")
            return None

        robot_id = compatible_robot
        print(f"Assigning task {task_id} to robot {robot_id}")

        # Get the task data and update it
        task_data = tasks[task_id]
        task_data["assigned_robot"] = robot_id
        task_data["status"] = "in_progress"
        task_data["task_id"] = task_id

        print(f"Updated task status: {task_data}")

        # Send the complete task data in the event
        event_dispatcher.dispatch("task_assigned", {
            "task_id": task_id,
            "robot_id": robot_id,
            "type": task_data["type"],  # Include the type
            "data": task_data["data"],  # Include the data
            "assigned_robot": robot_id,
            "status": "in_progress"
        })

        print(f"Dispatched task_assigned event for task {task_id}")

        # Remove task from queue after assignment
        task_queue.remove(task_id)
        print(f"Removed task {task_id} from queue. Remaining queue: {task_queue}")

    def update_robot_status(robot_id: str, status: str):
        robot_status[robot_id] = status
        if status == "idle":
            assign_next_task()

    def _sort_task_queue():
        task_queue.sort(
            key=lambda task_id: tasks[task_id].get("priority", 0),
            reverse=True
        )

    def update_task_state(event_data: Dict[str, Any]):
        task_id = event_data["task_id"]
        new_state = event_data["new_state"]
        details = event_data.get("details", {})

        if task_id in tasks:
            tasks[task_id]["status"] = new_state
            if details:
                tasks[task_id].update(details)

            print(f"Updated task {task_id} state to: {new_state}")
            if details:
                print(f"With details: {details}")

    def get_all_tasks() -> Dict[str, Dict[str, Any]]:
        return tasks

    def handle_task_completion(event_data: Dict[str, Any]):
        task_id = event_data["task_id"]
        success = event_data["success"]
        robot_id = event_data["robot_id"]

        print(f"\nHandling task completion for task {task_id}")
        print(f"Success: {success}, Robot: {robot_id}")

        if task_id in tasks:
            tasks[task_id]["status"] = "completed" if success else "failed"
            print(f"Updated task status to: {tasks[task_id]['status']}")

        # Update robot status to idle
        robot_status[robot_id] = "idle"
        print(f"Updated robot {robot_id} status to idle")

    def register_robot(robot_id: str, robot_type: str):
        print(f"Registering robot {robot_id} of type {robot_type}")
        robot_status[robot_id] = "idle"
        print(f"Updated robot status: {robot_status}")

    return {
        "add_task": add_task,
        "assign_next_task": assign_next_task,
        "update_robot_status": update_robot_status,
        "update_task_state": update_task_state,
        "get_all_tasks": get_all_tasks,
        "handle_task_completion": handle_task_completion,
        "register_robot": register_robot
    }
