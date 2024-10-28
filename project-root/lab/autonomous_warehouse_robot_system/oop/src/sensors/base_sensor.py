from abc import ABC, abstractmethod
from typing import Dict, Any

class ObstacleSensor(ABC):
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
        self.status = "active"

    @abstractmethod
    def detect(self) -> bool:
        """Detect obstacles in the environment"""
        pass

    def get_status(self) -> Dict[str, Any]:
        return {
            "sensor_id": self.sensor_id,
            "status": self.status
        }
