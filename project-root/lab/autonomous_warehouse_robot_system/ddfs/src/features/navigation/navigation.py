from typing import Dict, Callable
from ..communication.event_dispatcher import EventDispatcher

def create_navigation_module(event_dispatcher: EventDispatcher, obstacle_detector: Callable):
    def move_to(robot_id: str, target_position: Dict[str, float]):
        if obstacle_detector(robot_id, target_position):
            event_dispatcher.dispatch("obstacle_detected", {
                "robot_id": robot_id,
                "position": target_position
            })
            return False

        event_dispatcher.dispatch("robot_moved", {
            "robot_id": robot_id,
            "position": target_position
        })
        return True

    def calculate_path(start_position: Dict[str, float], end_position: Dict[str, float]):
        # Simple direct path calculation
        return [start_position, end_position]

    def update_robot_position(robot_id: str, new_position: Dict[str, float]):
        event_dispatcher.dispatch("robot_position_updated", {
            "robot_id": robot_id,
            "position": new_position
        })
        return True

    return {
        "move_to": move_to,
        "calculate_path": calculate_path,
        "update_robot_position": update_robot_position
    }
