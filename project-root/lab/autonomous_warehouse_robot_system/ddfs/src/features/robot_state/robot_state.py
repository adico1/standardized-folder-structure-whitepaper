from typing import Dict, Any
from ..communication.event_dispatcher import EventDispatcher

def create_robot_state_module(event_dispatcher: EventDispatcher):
    robots: Dict[str, Dict[str, Any]] = {}

    def register_robot(robot_id: str, robot_type: str, initial_position: Dict[str, float]):
        robots[robot_id] = {
            "type": robot_type,
            "position": initial_position,
            "status": "idle",
            "current_task": None,
            "cargo": None
        }

    def update_robot_position(robot_id: str, position: Dict[str, float]):
        if robot_id in robots:
            robots[robot_id]["position"] = position
            event_dispatcher.dispatch("robot_position_updated", {
                "robot_id": robot_id,
                "position": position
            })

    def update_robot_status(robot_id: str, status: str):
        if robot_id in robots:
            robots[robot_id]["status"] = status
            event_dispatcher.dispatch("robot_status_updated", {
                "robot_id": robot_id,
                "status": status,
                "position": robots[robot_id]["position"]  # Include position in status update
            })

    def get_robot_state(robot_id: str) -> Dict[str, Any]:
        return robots.get(robot_id, {})

    return {
        "register_robot": register_robot,
        "update_robot_position": update_robot_position,
        "update_robot_status": update_robot_status,
        "get_robot_state": get_robot_state
    }
