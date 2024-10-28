from .base_sensor import ObstacleSensor
import random

class UltrasonicSensor(ObstacleSensor):
    def __init__(self, sensor_id: str, max_range: float = 4.0):
        super().__init__(sensor_id)
        self.max_range = max_range
        self.last_distance = None

    def detect(self) -> bool:
        # Simulate ultrasonic distance measurement
        self.last_distance = random.uniform(0, self.max_range)
        return self.last_distance < 1.0  # Obstacle detected if distance < 1m

    def get_status(self) -> dict:
        status = super().get_status()
        status.update({
            "max_range": self.max_range,
            "last_distance": self.last_distance
        })
        return status
