from .base_robot import Robot
from typing import Dict, Optional

class PickerRobot(Robot):
    def __init__(self, robot_id: str, position: Dict[str, float]):
        super().__init__(robot_id, position)
        self.carrying_item = None

    def pick_item(self, item_id: str) -> bool:
        if self.carrying_item is None:
            self.carrying_item = item_id
            return True
        return False

    def drop_item(self) -> Optional[str]:
        if self.carrying_item:
            item = self.carrying_item
            self.carrying_item = None
            return item
        return None

    def get_status(self) -> Dict:
        status = super().get_status()
        status["carrying_item"] = self.carrying_item
        return status
