from typing import Dict, Callable

def create_obstacle_detection_module():
    sensors: Dict[str, Callable] = {}

    def add_sensor(sensor_id: str, detect_fn: Callable):
        sensors[sensor_id] = detect_fn
        print(f"Added sensor {sensor_id}")

    def check_for_obstacles(robot_id: str, position: Dict[str, float]) -> bool:
        for sensor_id, detect_fn in sensors.items():
            if detect_fn(position):
                print(f"Obstacle detected by sensor {sensor_id} for robot {robot_id}")
                return True
        return False

    return {
        "add_sensor": add_sensor,
        "check_for_obstacles": check_for_obstacles
    }
