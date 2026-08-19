
**Owner**:
The user whose time is being booked and who configures the meeting types, availability and
settings. Every tenant row belongs to exactly one.
_Avoid_: user (a login), admin (site-wide privilege), account (a connected Google account)

**Invitee**:
The person who books an Owner's time. Has no login and no calit row of their own beyond the
booking.
_Avoid_: guest (an extra attendee added to a booking), booker, attendee, customer

**Host**:
An Owner who participates in a meeting type and whose calendar a booking must fit — the Creator
or an accepted Co-host. The unit availability and buffers are resolved per.
_Avoid_: participant, organizer (that is the one host whose Google account the event is created on)
