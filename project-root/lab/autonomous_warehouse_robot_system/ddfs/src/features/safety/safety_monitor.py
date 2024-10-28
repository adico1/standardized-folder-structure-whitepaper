from typing import Dict, Any, Callable
from ..communication.event_dispatcher import EventDispatcher

def create_safety_monitor(event_dispatcher: EventDispatcher):
    active_alerts: Dict[str, Dict[str, Any]] = {}

    def monitor_robot_status(data: Dict[str, Any]):  # Changed to accept single data argument
        robot_id = data.get("robot_id")
        status = data.get("status")

        if status == "error":
            handle_error(robot_id, "robot_error", data)

    def handle_error(robot_id: str, error_type: str, details: Dict[str, Any]):
        alert_id = f"{error_type}_{robot_id}_{len(active_alerts)}"
        alert_data = {
            "alert_id": alert_id,
            "robot_id": robot_id,
            "type": error_type,
            "details": details,
            "status": "active"
        }
        active_alerts[alert_id] = alert_data

        event_dispatcher.dispatch("safety_alert", alert_data)

        if error_type in ["collision_risk", "system_failure"]:
            event_dispatcher.dispatch("emergency_stop", {
                "robot_id": robot_id,
                "reason": error_type
            })

    def resolve_alert(alert_id: str):
        if alert_id in active_alerts:
            active_alerts[alert_id]["status"] = "resolved"
            event_dispatcher.dispatch("alert_resolved", {
                "alert_id": alert_id
            })

    return {
        "monitor_robot_status": monitor_robot_status,
        "handle_error": handle_error,
        "resolve_alert": resolve_alert
    }
