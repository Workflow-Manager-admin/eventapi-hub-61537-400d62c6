from flask.views import MethodView
from flask_smorest import Blueprint, abort

from ..models import Event, EventSchema
from ..storage import event_storage

blp = Blueprint(
    "Events",
    "events",
    url_prefix="/events",
    description="Operations on events"
)

event_schema = EventSchema()
event_list_schema = EventSchema(many=True)


# PUBLIC_INTERFACE
@blp.route("/")
class EventsList(MethodView):
    """List all events or create a new event."""

    @blp.response(200, EventSchema(many=True), description="List of all events.")
    def get(self):
        """Get a list of all events."""
        return event_storage.list_events()

    @blp.arguments(EventSchema, location="json")
    @blp.response(201, EventSchema, description="Created event")
    def post(self, event_data):
        """Create a new event."""
        try:
            event_obj = Event(**event_data)
        except TypeError as e:
            abort(400, str(e))
        event = event_storage.create_event(event_obj)
        return event


# PUBLIC_INTERFACE
@blp.route("/<int:event_id>")
class EventDetail(MethodView):
    """Retrieve, update, or delete a specific event."""

    @blp.response(200, EventSchema, description="Event details")
    def get(self, event_id):
        """Get event details by ID."""
        event = event_storage.get_event(event_id)
        if not event:
            abort(404, message="Event not found.")
        return event

    @blp.arguments(EventSchema, location="json")
    @blp.response(200, EventSchema, description="Updated event")
    def put(self, event_data, event_id):
        """Update an existing event."""
        event = event_storage.update_event(event_id, event_data)
        if not event:
            abort(404, message="Event not found.")
        return event

    @blp.response(204, description="Event deleted")
    def delete(self, event_id):
        """Delete an event by ID."""
        deleted = event_storage.delete_event(event_id)
        if not deleted:
            abort(404, message="Event not found.")
        return ""
