from typing import Dict, List, Any

def create_task_assignment_module():
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
        print(f"Added task {task_id} to queue")

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

        # Update task data with task_id and robot assignment
        task_data["task_id"] = task_id
        task_data["assigned_robot"] = robot_id
        task_data["status"] = "in_progress"
        tasks[task_id] = task_data

        task_queue.remove(task_id)
        return task_data

    def _sort_task_queue():
        task_queue.sort(
            key=lambda task_id: tasks[task_id].get("priority", 0),
            reverse=True
        )

    def register_robot(robot_id: str, robot_type: str):
        print(f"Registering robot {robot_id} of type {robot_type}")
        robot_status[robot_id] = "idle"
        print(f"Updated robot status: {robot_status}")

    def update_task_status(task_id: str, status: str):
        if task_id in tasks:
            tasks[task_id]["status"] = status
            print(f"Updated task {task_id} status to: {status}")

    def update_robot_status(robot_id: str, status: str):
        robot_status[robot_id] = status
        print(f"Updated robot {robot_id} status to: {status}")

    def get_all_tasks():
        return tasks

    return {
        "add_task": add_task,
        "assign_next_task": assign_next_task,
        "register_robot": register_robot,
        "update_task_status": update_task_status,
        "update_robot_status": update_robot_status,
        "get_all_tasks": get_all_tasks
    }
