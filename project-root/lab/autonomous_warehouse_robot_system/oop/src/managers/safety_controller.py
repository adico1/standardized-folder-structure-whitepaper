from typing import Dict, Any, List, Callable
from ..robots.base_robot import Robot

class SafetyController:
    def __init__(self):
        self.error_handlers: Dict[str, List[Callable]] = {}
        self.active_alerts: Dict[str, Dict[str, Any]] = {}

    def register_error_handler(self, error_type: str, handler: Callable):
        if error_type not in self.error_handlers:
            self.error_handlers[error_type] = []
        self.error_handlers[error_type].append(handler)

    def handle_error(self, error_type: str, robot: Robot, details: Dict[str, Any]):
        alert_id = f"{error_type}_{robot.robot_id}_{len(self.active_alerts)}"
        self.active_alerts[alert_id] = {
            "type": error_type,
            "robot": robot,
            "details": details,
            "status": "active"
        }

        if error_type in self.error_handlers:
            for handler in self.error_handlers[error_type]:
                handler(robot, details)

    def resolve_alert(self, alert_id: str):
        if alert_id in self.active_alerts:
            self.active_alerts[alert_id]["status"] = "resolved"

    def get_active_alerts(self) -> Dict[str, Dict[str, Any]]:
        return {k: v for k, v in self.active_alerts.items()
                if v["status"] == "active"}
