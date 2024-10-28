from typing import Dict, Callable, Any
from ..communication.event_dispatcher import EventDispatcher

def create_obstacle_detection_module(event_dispatcher: EventDispatcher):
    sensors: Dict[str, Callable] = {}

    def add_sensor(sensor_id: str, detect_fn: Callable):
        sensors[sensor_id] = detect_fn

    def check_for_obstacles(robot_id: str, position: Dict[str, float]) -> bool:
        for sensor_id, detect_fn in sensors.items():
            if detect_fn(position):
                event_dispatcher.dispatch("obstacle_detected", {
                    "robot_id": robot_id,
                    "sensor_id": sensor_id,
                    "position": position
                })
                return True
        return False

    def process_sensor_reading(data: Dict[str, Any]):
        sensor_id = data["sensor_id"]
        reading = data["reading"]
        sensor_type = data["type"]

        # Process reading based on sensor type
        threshold = {
            "infrared": 1.0,
            "ultrasonic": 0.5
        }.get(sensor_type, 1.0)

        if reading < threshold:
            event_dispatcher.dispatch("obstacle_detected", {
                "sensor_id": sensor_id,
                "reading": reading,
                "type": sensor_type
            })

    return {
        "add_sensor": add_sensor,
        "check_for_obstacles": check_for_obstacles,
        "process_sensor_reading": process_sensor_reading
    }
