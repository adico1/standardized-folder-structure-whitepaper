from .base_task import Task
from ..robots.transport_robot import TransportRobot
from typing import Dict

class TransportTask(Task):
    def __init__(self, task_id: str, item_id: str, weight: float,
                 pickup_location: Dict[str, float],
                 dropoff_location: Dict[str, float],
                 priority: int = 1):
        super().__init__(task_id, priority)
        self.item_id = item_id
        self.weight = weight
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location

    def execute(self, robot) -> bool:
        if not isinstance(robot, TransportRobot):
            return False

        # Move to pickup location
        if not robot.move(self.pickup_location):
            return False

        # Load cargo
        if not robot.load_cargo(self.item_id, self.weight):
            return False

        # Move to dropoff location
        if not robot.move(self.dropoff_location):
            return False

        # Unload cargo
        robot.unload_cargo()
        return True

    def get_target_location(self) -> Dict[str, float]:
        # Return pickup location if cargo not loaded, otherwise return dropoff location
        if not self.assigned_robot or not isinstance(self.assigned_robot, TransportRobot):
            return self.pickup_location
        return self.dropoff_location if self.assigned_robot.cargo else self.pickup_location
