from .base_task import Task
from ..robots.picker_robot import PickerRobot
from typing import Dict

class PickTask(Task):
    def __init__(self, task_id: str, item_id: str, location: Dict[str, float], priority: int = 1):
        super().__init__(task_id, priority)
        self.item_id = item_id
        self.location = location

    def execute(self, robot) -> bool:
        if not isinstance(robot, PickerRobot):
            return False

        # Move to item location
        if not robot.move(self.location):
            return False

        # Attempt to pick the item
        return robot.pick_item(self.item_id)

    def get_target_location(self) -> Dict[str, float]:
        return self.location
