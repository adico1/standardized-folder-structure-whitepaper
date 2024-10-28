from typing import Dict, List
from ..robots.base_robot import Robot

class NavigationController:
    def __init__(self):
        self.active_routes: Dict[str, List[Dict[str, float]]] = {}

    def calculate_path(self, start: Dict[str, float], end: Dict[str, float]) -> List[Dict[str, float]]:
        # Simple direct path for now
        return [start, end]

    def navigate_robot(self, robot: Robot, target: Dict[str, float]) -> bool:
        if robot.check_obstacles():
            return False

        path = self.calculate_path(robot.position, target)
        self.active_routes[robot.robot_id] = path

        return robot.move(target)

    def get_active_route(self, robot_id: str) -> List[Dict[str, float]]:
        return self.active_routes.get(robot_id, [])
