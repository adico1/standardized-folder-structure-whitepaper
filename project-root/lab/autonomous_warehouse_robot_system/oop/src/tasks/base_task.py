from abc import ABC, abstractmethod
from typing import Dict, Any
from ..robots.base_robot import Robot

class Task(ABC):
    def __init__(self, task_id: str, priority: int = 1):
        self.task_id = task_id
        self.priority = priority
        self.status = "pending"
        self.assigned_robot = None

    @abstractmethod
    def execute(self, robot: Robot) -> bool:
        pass

    def get_status(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "priority": self.priority,
            "status": self.status,  # This will now show "completed" or "failed"
            "assigned_robot": self.assigned_robot.robot_id if self.assigned_robot else None
        }

    def get_target_location(self) -> Dict[str, float]:
        """Return the target location for this task. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement get_target_location")
