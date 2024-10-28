from typing import Dict, Any, Optional
from ..features.communication.event_dispatcher import EventDispatcher

def create_error_handler(event_dispatcher: EventDispatcher):
    def handle_error(error_type: str, details: Dict[str, Any], severity: str = "warning"):
        error_data = {
            "type": error_type,
            "details": details,
            "severity": severity,
            "timestamp": __import__('time').time()
        }

        event_dispatcher.dispatch("error_occurred", error_data)

        if severity == "critical":
            event_dispatcher.dispatch("system_halt_required", error_data)

        return error_data

    def log_error(error_data: Dict[str, Any]):
        # In a real implementation, this would write to a log file or database
        print(f"ERROR: {error_data['type']} - {error_data['details']}")

    return {
        "handle_error": handle_error,
        "log_error": log_error
    }
