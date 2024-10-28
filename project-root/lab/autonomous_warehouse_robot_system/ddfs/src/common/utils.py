from typing import Dict, Any

def calculate_distance(pos1: Dict[str, float], pos2: Dict[str, float]) -> float:
    """Calculate Euclidean distance between two positions"""
    return ((pos1["x"] - pos2["x"]) ** 2 + (pos1["y"] - pos2["y"]) ** 2) ** 0.5

def validate_position(position: Dict[str, float]) -> bool:
    """Validate that a position contains required coordinates"""
    return all(key in position for key in ["x", "y"])

def create_task_data(task_type: str, **kwargs) -> Dict[str, Any]:
    """Create a standardized task data structure"""
    return {
        "type": task_type,
        "priority": kwargs.get("priority", 1),
        "data": kwargs
    }
