from .base_sensor import ObstacleSensor
import random  # For simulation purposes

class InfraredSensor(ObstacleSensor):
    def __init__(self, sensor_id: str, detection_range: float = 2.0):
        super().__init__(sensor_id)
        self.detection_range = detection_range
        self.last_reading = None

    def detect(self) -> bool:
        # Simulate obstacle detection
        self.last_reading = random.random() * self.detection_range
        return self.last_reading < (self.detection_range / 2)

    def get_status(self) -> dict:
        status = super().get_status()
        status.update({
            "detection_range": self.detection_range,
            "last_reading": self.last_reading
        })
        return status
