In this example:

* The `read_data` method simulates a new distance reading each time it’s called.
* The `simulate_stream` method mimics a continuous data stream by printing sensor data at regular intervals.

### **Testing Scenarios with Simulated Sensors**

Simulated sensors enable you to define diverse testing scenarios, such as:

* **Normal Operation**: Test the system under stable, expected sensor data to benchmark standard performance.
* **Edge Cases**: Simulate high and low extremes in data (e.g., max distance readings) to ensure the system can handle boundary conditions.
* **Failure Simulation**: Emulate sensor failure or unexpected values (e.g., null readings) to evaluate how the system handles errors.
* **High-Frequency Data**: Increase the data generation rate to test the system's ability to handle high-throughput conditions.

By using simulated sensors, you can effectively test the architecture, real-time interactions, error handling, and adaptability, providing robust insights without needing physical sensor hardware.

```python
import random
import time

class ProximitySensor:
    def __init__(self, min_distance=0.5, max_distance=5.0):
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.current_distance = max_distance

    def read_data(self):
        # Simulate distance readings with some randomness
        self.current_distance = random.uniform(self.min_distance, self.max_distance)
        return self.current_distance

    def simulate_stream(self, delay=1):
        while True:
            distance = self.read_data()
            print(f"ProximitySensor reading: {distance:.2f} meters")
            time.sleep(delay)  # Delay to simulate real-time sensor data intervals

# Usage example
sensor = ProximitySensor()
sensor.simulate_stream(delay=2)  # Generate data every 2 seconds
```