from typing import Dict, List, Optional
from ..robots.base_robot import Robot
from ..robots.picker_robot import PickerRobot
from ..robots.transport_robot import TransportRobot
from ..tasks.base_task import Task
from ..tasks.pick_task import PickTask
from ..tasks.transport_task import TransportTask

class TaskManager:
    def __init__(self):
        self.robots: Dict[str, Robot] = {}
        self.tasks: Dict[str, Task] = {}
        self.task_queue: List[str] = []

    def register_robot(self, robot: Robot):
        self.robots[robot.robot_id] = robot

    def add_task(self, task: Task):
        self.tasks[task.task_id] = task
        self.task_queue.append(task.task_id)
        self._sort_task_queue()

    def assign_next_task(self) -> Optional[bool]:
        if not self.task_queue:
            return None

        task_id = self.task_queue[0]
        task = self.tasks[task_id]

        # Print available robots and task queue status
        available_robots = [r for r in self.robots.values() if r.status == "idle"]
        print(f"\nAvailable robots: {[r.robot_id for r in available_robots]}")
        print(f"Current task queue: {self.task_queue}")
        print(f"Robot status: {[(r.robot_id, r.status) for r in self.robots.values()]}")

        # Find appropriate robot for the task type
        available_robot = None
        for robot in self.robots.values():
            if robot.status == "idle":
                # Check task-robot compatibility
                if (isinstance(task, PickTask) and isinstance(robot, PickerRobot)) or \
                   (isinstance(task, TransportTask) and isinstance(robot, TransportRobot)):
                    available_robot = robot
                    break

        if not available_robot:
            print("No compatible robot available")
            return None

        print(f"Assigning task {task_id} to robot {available_robot.robot_id}")

        task.assigned_robot = available_robot
        available_robot.current_task = task_id
        available_robot.update_status("busy")

        print(f"\nExecuting {task.__class__.__name__} (ID: {task_id}) with robot {available_robot.robot_id}")
        if isinstance(task, PickTask):
            print(f"Task details: Location: {task.location}, Item: {task.item_id}")
        elif isinstance(task, TransportTask):
            print(f"Task details: From {task.pickup_location} to {task.dropoff_location}, Item: {task.item_id}")

        success = task.execute(available_robot)
        print(f"Task {task_id} execution {'successful' if success else 'failed'}")

        # Update task status
        task.status = "completed" if success else "failed"
        print(f"Updated task status to: {task.status}")

        # Remove the task from queue after execution
        if task_id in self.task_queue:
            self.task_queue.remove(task_id)
            print(f"Removed task {task_id} from queue. Remaining queue: {self.task_queue}")

        # Update robot status
        available_robot.current_task = None
        available_robot.update_status("idle")
        print(f"Updated robot {available_robot.robot_id} status to idle")

        return success

    def _sort_task_queue(self):
        self.task_queue.sort(
            key=lambda task_id: self.tasks[task_id].priority,
            reverse=True
        )

    def handle_task_completion(self, robot_id: str, task_id: str, success: bool):
        print(f"\nHandling task completion for task {task_id}")
        print(f"Success: {success}, Robot: {robot_id}")

        robot = self.robots[robot_id]
        robot.current_task = None
        robot.update_status("idle")
        print(f"Updated robot {robot_id} status to idle")

        task = self.tasks[task_id]
        task.status = "completed" if success else "failed"
        print(f"Updated task status to: {task.status}")

    def execute_task(self, task_id: str) -> bool:
        if task_id not in self.tasks:
            return False

        task = self.tasks[task_id]
        robot = task.assigned_robot

        if not robot or robot.status != "busy":
            return False

        # Use navigation controller for movement
        if hasattr(self, 'navigation_controller'):
            success = self.navigation_controller.navigate_robot(robot, task.get_target_location())
            if not success:
                self.handle_task_completion(robot.robot_id, task_id, False)
                return False

        return robot.execute_task(task)
