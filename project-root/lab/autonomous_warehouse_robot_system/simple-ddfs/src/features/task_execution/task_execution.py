from typing import Dict, Any, Callable

def create_task_execution_module(navigation_module: Dict[str, Callable], robot_state_module: Dict[str, Callable]):
    def execute_pick_task(task_data: Dict[str, Any]) -> bool:
        robot_id = task_data["assigned_robot"]
        item_location = task_data["data"]["location"]

        print(f"\nExecuting pick task to location: {item_location}")

        # Move robot to item location
        success = navigation_module["move_to"](robot_id, item_location)
        if not success:
            return False

        # Update robot state with picked item
        robot_state_module["update_robot_status"](robot_id, "picking")
        return True

    def execute_transport_task(task_data: Dict[str, Any]) -> bool:
        robot_id = task_data["assigned_robot"]
        pickup = task_data["data"]["pickup_location"]
        dropoff = task_data["data"]["dropoff_location"]

        print(f"\nExecuting transport task from {pickup} to {dropoff}")

        # Move to pickup
        if not navigation_module["move_to"](robot_id, pickup):
            return False

        # Move to dropoff
        if not navigation_module["move_to"](robot_id, dropoff):
            return False

        return True

    def execute_task(task_data: Dict[str, Any]) -> bool:
        task_type = task_data["type"]
        task_id = task_data.get("task_id")
        robot_id = task_data["assigned_robot"]

        print(f"\nExecuting {task_type} task (ID: {task_id}) with robot {robot_id}")
        print(f"Task details: {task_data['data']}")

        success = False
        if task_type == "pick":
            success = execute_pick_task(task_data)
        elif task_type == "transport":
            success = execute_transport_task(task_data)

        print(f"Task {task_id} execution {'successful' if success else 'failed'}")
        robot_state_module["update_robot_status"](robot_id, "idle")

        return success

    return {
        "execute_task": execute_task
    }
