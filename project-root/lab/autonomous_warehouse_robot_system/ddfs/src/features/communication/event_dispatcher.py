from typing import Dict, List, Callable, Any

class EventDispatcher:
    def __init__(self):
        self.listeners: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, callback: Callable):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(callback)

    def dispatch(self, event_type: str, data: Any):
        if event_type in self.listeners:
            for callback in self.listeners[event_type]:
                callback(data)
