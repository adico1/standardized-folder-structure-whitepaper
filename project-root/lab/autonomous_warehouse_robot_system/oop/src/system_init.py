from src.managers.task_manager import TaskManager
from src.managers.safety_controller import SafetyController
from src.robots.picker_robot import PickerRobot
from src.robots.transport_robot import TransportRobot
from src.sensors.infrared_sensor import InfraredSensor
from src.sensors.ultrasonic_sensor import UltrasonicSensor
from src.managers.navigation_controller import NavigationController
from src.robots.base_robot import Robot
from typing import Dict, Any

def initialize_system():
    # Initialize controllers
    task_manager = TaskManager()
    safety_controller = SafetyController()

    # Create and register robots
    picker = PickerRobot("picker_1", {"x": 0, "y": 0})
    transport = TransportRobot("transport_1", {"x": 0, "y": 0})

    # Add sensors to robots
    picker.add_sensor("infrared", InfraredSensor("ir_1"))
    transport.add_sensor("ultrasonic", UltrasonicSensor("us_1"))

    # Register robots with task manager
    task_manager.register_robot(picker)
    task_manager.register_robot(transport)

    # Add error handler registration
    def robot_error_handler(robot: Robot, details: Dict[str, Any]):
        print(f"Error handling for robot {robot.robot_id}: {details}")
        robot.update_status("error")

    safety_controller.register_error_handler("task_execution_error", robot_error_handler)

    # Add to initialization
    navigation_controller = NavigationController()

    return {
        "task_manager": task_manager,
        "safety_controller": safety_controller,
        "navigation_controller": navigation_controller
    }
