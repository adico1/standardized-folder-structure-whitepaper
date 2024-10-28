from .features.communication.event_dispatcher import EventDispatcher
from .features.navigation.navigation import create_navigation_module
from .features.task_assignment.task_assignment import create_task_assignment_module
from .features.obstacle_detection.obstacle_detection import create_obstacle_detection_module
from .features.robot_state.robot_state import create_robot_state_module
from .features.task_execution.task_execution import create_task_execution_module
from .features.safety.safety_monitor import create_safety_monitor

def initialize_system():
    # Create event dispatcher
    event_dispatcher = EventDispatcher()

    # Initialize all modules
    obstacle_detection = create_obstacle_detection_module(event_dispatcher)
    navigation = create_navigation_module(event_dispatcher, obstacle_detection["check_for_obstacles"])
    robot_state = create_robot_state_module(event_dispatcher)
    task_assignment = create_task_assignment_module(event_dispatcher)
    task_execution = create_task_execution_module(event_dispatcher, navigation, robot_state)
    safety_monitor = create_safety_monitor(event_dispatcher)

    # Update event subscriptions
    event_dispatcher.subscribe("robot_status_updated", safety_monitor["monitor_robot_status"])
    event_dispatcher.subscribe("task_assigned", task_execution["execute_task"])
    event_dispatcher.subscribe("task_completed", task_assignment["handle_task_completion"])
    event_dispatcher.subscribe("task_state_updated", task_assignment["update_task_state"])
    event_dispatcher.subscribe("obstacle_detected", safety_monitor["handle_error"])

    return {
        "event_dispatcher": event_dispatcher,
        "navigation": navigation,
        "task_assignment": task_assignment,
        "obstacle_detection": obstacle_detection,
        "robot_state": robot_state,
        "task_execution": task_execution,
        "safety_monitor": safety_monitor
    }
