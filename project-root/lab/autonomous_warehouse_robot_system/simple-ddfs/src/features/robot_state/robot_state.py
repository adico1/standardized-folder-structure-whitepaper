from typing import Dict, Any

def create_robot_state_module():
    robots: Dict[str, Dict[str, Any]] = {}

    def register_robot(robot_id: str, robot_type: str, initial_position: Dict[str, float]):
        robots[robot_id] = {
            "type": robot_type,
            "position": initial_position,
            "status": "idle",
            "current_task": None,
            "cargo": None
        }
        print(f"Registered robot {robot_id} of type {robot_type}")

    def update_robot_position(robot_id: str, position: Dict[str, float]):
        if robot_id in robots:
            robots[robot_id]["position"] = position
            print(f"Updated robot {robot_id} position to {position}")

    def update_robot_status(robot_id: str, status: str):
        if robot_id in robots:
            robots[robot_id]["status"] = status
            print(f"Updated robot {robot_id} status to {status}")

    def get_robot_state(robot_id: str) -> Dict[str, Any]:
        return robots.get(robot_id, {})

    return {
        "register_robot": register_robot,
        "update_robot_position": update_robot_position,
        "update_robot_status": update_robot_status,
        "get_robot_state": get_robot_state
    }
