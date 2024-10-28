from typing import Dict, Any, Callable
from ..communication.event_dispatcher import EventDispatcher
import random

def create_sensor_simulation(event_dispatcher: EventDispatcher):
    sensors: Dict[str, Dict[str, Any]] = {}

    def create_sensor(sensor_id: str, sensor_type: str, config: Dict[str, Any]):
        sensors[sensor_id] = {
            "type": sensor_type,
            "config": config,
            "status": "active"
        }

    def simulate_reading(sensor_id: str) -> Dict[str, Any]:
        if sensor_id not in sensors:
            return None

        sensor = sensors[sensor_id]
        if sensor["type"] == "infrared":
            reading = random.uniform(0, sensor["config"]["max_range"])
        elif sensor["type"] == "ultrasonic":
            reading = random.uniform(0, sensor["config"]["max_distance"])

        event_dispatcher.dispatch("sensor_reading", {
            "sensor_id": sensor_id,
            "reading": reading,
            "type": sensor["type"]
        })

        return {"reading": reading}

    return {
        "create_sensor": create_sensor,
        "simulate_reading": simulate_reading
    }
