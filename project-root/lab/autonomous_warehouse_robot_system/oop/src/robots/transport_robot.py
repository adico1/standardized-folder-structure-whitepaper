from .base_robot import Robot
from typing import Dict, Optional

class TransportRobot(Robot):
    def __init__(self, robot_id: str, position: Dict[str, float], max_load: float = 100.0):
        super().__init__(robot_id, position)
        self.max_load = max_load
        self.current_load = 0.0
        self.cargo = []

    def load_cargo(self, item_id: str, weight: float) -> bool:
        if self.current_load + weight <= self.max_load:
            self.cargo.append(item_id)
            self.current_load += weight
            return True
        return False

    def unload_cargo(self) -> list:
        cargo = self.cargo.copy()
        self.cargo = []
        self.current_load = 0.0
        return cargo

    def get_status(self) -> Dict:
        status = super().get_status()
        status.update({
            "current_load": self.current_load,
            "max_load": self.max_load,
            "cargo": self.cargo
        })
        return status
