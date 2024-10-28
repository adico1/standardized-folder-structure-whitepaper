from typing import Dict, Any, Callable
from ..communication.event_dispatcher import EventDispatcher

def create_task_execution_module(
    event_dispatcher: EventDispatcher,
    navigation_module: Dict[str, Callable],
    robot_state_module: Dict[str, Callable]
):
    def execute_pick_task(task_data: Dict[str, Any]):
        robot_id = task_data["assigned_robot"]
        item_location = task_data["data"]["location"]

        # Move robot to item location
        success = navigation_module["move_to"](robot_id, item_location)
        if not success:
            return False

        # Update robot state with picked item
        robot_state_module["update_robot_status"](robot_id, "picking")
        event_dispatcher.dispatch("item_picked", {
            "robot_id": robot_id,
            "item_id": task_data["data"]["item_id"]
        })
        return True

    def execute_transport_task(task_data: Dict[str, Any]):
        robot_id = task_data["assigned_robot"]
        pickup = task_data["data"]["pickup_location"]
        dropoff = task_data["data"]["dropoff_location"]

        # Move to pickup
        if not navigation_module["move_to"](robot_id, pickup):
            return False

        # Move to dropoff
        if not navigation_module["move_to"](robot_id, dropoff):
            return False

        event_dispatcher.dispatch("cargo_delivered", {
            "robot_id": robot_id,
            "task_id": task_data["task_id"]
        })
        return True

    def handle_task_completion(task_data: Dict[str, Any], success: bool):
        robot_id = task_data["assigned_robot"]

        event_dispatcher.dispatch("task_completed", {
            "task_id": task_data["task_id"],
            "robot_id": robot_id,
            "success": success
        })

        robot_state_module["update_robot_status"](robot_id, "idle")

    def execute_task(task_data: Dict[str, Any]):
        task_type = task_data["type"]
        task_id = task_data.get("task_id")
        robot_id = task_data["assigned_robot"]
        success = False

        print(f"\nExecuting {task_type} task (ID: {task_id}) with robot {robot_id}")
        print(f"Task details: {task_data['data']}")

        if task_type == "pick":
            print(f"Executing pick task to location: {task_data['data']['location']}")
            success = execute_pick_task(task_data)
        elif task_type == "transport":
            print(f"Executing transport task from {task_data['data']['pickup_location']} to {task_data['data']['dropoff_location']}")
            success = execute_transport_task(task_data)

        print(f"Task {task_id} execution {'successful' if success else 'failed'}")

        # Update task status and robot status
        event_dispatcher.dispatch("task_completed", {
            "task_id": task_id,
            "success": success,
            "robot_id": robot_id
        })

        print(f"Dispatched task_completed event for task {task_id}")

        # Update task state with the correct argument structure
        event_dispatcher.dispatch("task_state_updated", {
            "task_id": task_id,
            "new_state": "completed" if success else "failed",
            "details": {"success": success}
        })

        print(f"Dispatched task_state_updated event for task {task_id}")
        return success

    # Add to the returned dictionary
    return {
        "execute_pick_task": execute_pick_task,
        "execute_transport_task": execute_transport_task,
        "handle_task_completion": handle_task_completion,
        "execute_task": execute_task  # Add this new function
    }
