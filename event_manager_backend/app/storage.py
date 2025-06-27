# In-memory storage for simplicity (replace with DB in production)


class EventStorage:
    def __init__(self):
        self._events = []
        self._counter = 1

    # PUBLIC_INTERFACE
    def list_events(self):
        """Returns a list of all events."""
        return self._events

    # PUBLIC_INTERFACE
    def get_event(self, event_id):
        """Returns an event by its id or None if not found."""
        for ev in self._events:
            if ev.id == event_id:
                return ev
        return None

    # PUBLIC_INTERFACE
    def create_event(self, event):
        """Creates a new event, sets its id, and returns it."""
        event.id = self._counter
        self._counter += 1
        self._events.append(event)
        return event

    # PUBLIC_INTERFACE
    def update_event(self, event_id, event_data):
        """Updates an event by id with provided data, returns updated event or None."""
        ev = self.get_event(event_id)
        if not ev:
            return None
        for key, value in event_data.items():
            setattr(ev, key, value)
        return ev

    # PUBLIC_INTERFACE
    def delete_event(self, event_id):
        """Deletes the event by id, returns True if deleted, False if not found."""
        for idx, ev in enumerate(self._events):
            if ev.id == event_id:
                del self._events[idx]
                return True
        return False


# Singleton instance for storage
event_storage = EventStorage()
