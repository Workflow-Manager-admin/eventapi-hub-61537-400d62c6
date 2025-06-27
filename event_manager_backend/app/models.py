from marshmallow import Schema, fields, validate, validates_schema, ValidationError


# PUBLIC_INTERFACE
class Event:
    """
    Represents an event in the event manager.
    """

    def __init__(
        self,
        title,
        description,
        start_time,
        end_time,
        location,
        id=None
    ):
        self.id = id
        self.title = title
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.location = location


# PUBLIC_INTERFACE
class EventSchema(Schema):
    """
    Marshmallow schema for event serialization and deserialization with validation.
    """

    id = fields.Integer(
        dump_only=True,
        description="Unique identifier of the event"
    )
    title = fields.String(
        required=True,
        validate=validate.Length(min=1, max=100),
        description="Title of the event"
    )
    description = fields.String(
        required=True,
        validate=validate.Length(min=1, max=500),
        description="Description of the event"
    )
    start_time = fields.DateTime(
        required=True,
        description="Event start time (RFC3339)"
    )
    end_time = fields.DateTime(
        required=True,
        description="Event end time (RFC3339)"
    )
    location = fields.String(
        required=True,
        validate=validate.Length(min=1, max=200),
        description="Event location"
    )

    @validates_schema
    def validate_dates(self, data, **kwargs):
        if 'start_time' in data and 'end_time' in data:
            if data['end_time'] < data['start_time']:
                raise ValidationError(
                    "end_time must not be before start_time",
                    field_names=["end_time"]
                )
