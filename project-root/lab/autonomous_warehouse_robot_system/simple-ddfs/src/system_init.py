from .features.navigation.navigation import create_navigation_module
from .features.task_assignment.task_assignment import create_task_assignment_module
from .features.obstacle_detection.obstacle_detection import create_obstacle_detection_module
from .features.robot_state.robot_state import create_robot_state_module
from .features.task_execution.task_execution import create_task_execution_module

def initialize_system():
    # Initialize all modules
    obstacle_detection = create_obstacle_detection_module()
    navigation = create_navigation_module(obstacle_detection["check_for_obstacles"])
    robot_state = create_robot_state_module()
    task_assignment = create_task_assignment_module()
    task_execution = create_task_execution_module(navigation, robot_state)

    return {
        "navigation": navigation,
        "task_assignment": task_assignment,
        "obstacle_detection": obstacle_detection,
        "robot_state": robot_state,
        "task_execution": task_execution
    }
