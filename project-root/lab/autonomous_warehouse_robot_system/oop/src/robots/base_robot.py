from typing import Dict, Any, Optional
from ..sensors.base_sensor import ObstacleSensor

class Robot:
    def __init__(self, robot_id: str, position: Dict[str, float]):
        self.robot_id = robot_id
        self.position = position
        self.status = "idle"
        self.current_task = None
        self.sensors: Dict[str, ObstacleSensor] = {}

    def move(self, target_position: Dict[str, float]) -> bool:
        # Basic movement logic
        self.position = target_position
        return True

    def add_sensor(self, sensor_type: str, sensor: ObstacleSensor):
        self.sensors[sensor_type] = sensor

    def check_obstacles(self) -> bool:
        for sensor in self.sensors.values():
            if sensor.detect():
                return True
        return False

    def update_status(self, new_status: str):
        self.status = new_status

    def get_status(self) -> Dict[str, Any]:
        return {
            "robot_id": self.robot_id,
            "position": self.position,
            "status": self.status,
            "current_task": self.current_task
        }

    def handle_error(self, error_type: str, details: Dict[str, Any]):
        self.update_status("error")
        if hasattr(self, 'task_manager'):
            self.task_manager.safety_controller.handle_error(error_type, self, details)

    def execute_task(self, task: 'Task') -> bool:
        try:
            success = task.execute(self)
            if success:
                self.task_manager.handle_task_completion(self.robot_id, task.task_id, True)
            return success
        except Exception as e:
            self.handle_error("task_execution_error", {"error": str(e)})
            self.task_manager.handle_task_completion(self.robot_id, task.task_id, False)
            return False
