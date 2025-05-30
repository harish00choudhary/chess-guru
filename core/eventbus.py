class EventBus:
    def __init__(self):
        self._events = {}

    def on(self, event_name, callback):
        if event_name not in self._events:
            self._events[event_name] = []
        self._events[event_name].append(callback)

    def emit(self, event_name, *args, **kwargs):
        if event_name in self._events:
            for callback in self._events[event_name]:
                callback(*args, **kwargs)
    
    def emit_with_return(self, event_name, *args, **kwargs):
        results = []
        if event_name in self._events:
            for callback in self._events[event_name]:
                result = callback(*args, **kwargs)
                results.append(result)
        return results

Appbus = EventBus()