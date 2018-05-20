import json

class Member:
    def __init__(self, name, meetup_id, slack_id, sverok_id, group_id):
        self.name = name
        self.group_id = group_id
        self.sverok_id = sverok_id
        self.slack_id = slack_id
        self.meetup_id = meetup_id

    def __repr__(self):
        return "Member(meetup_id={self.meetup_id}, slack_id={self.slack_id}, sverok_id={self.sverok_id}, group_id={" \
               "self.group_id}) "


class Event:
    def __init__(self, id: int, name: str, time: int, status: str, rsvp_limit: int, waitlist_count: int,
                 yes_rsvp_count: int, announced: bool, event_url: str, venue: dict, participants: list = None,
                 **kwargs: dict) -> None:
        self.participants = participants or []
        self.venue = venue
        self.event_url = event_url
        self.announced = announced
        self.yes_rsvp_count = yes_rsvp_count
        self.waitlist_count = waitlist_count
        self.rsvp_limit = rsvp_limit
        self.status = status
        self.time = time
        self.name = name
        self.event_id = id
        _ = kwargs

    def json(self):
        d = {"event_id": self.event_id,
             "name": self.name,
             "time": self.time,
             "status": self.status,
             "rsvp_limit": self.rsvp_limit,
             "waitlist_count": self.waitlist_count,
             "yes_rsvp_count": self.yes_rsvp_count,
             "announced": self.announced,
             "event_url" : self.event_url,
             "venue": self.venue,
             "participants": self.participants}
        return json.dumps(d)

    def __repr__(self):
        return "Event(event_id={self.event_id}, name='{self.name}', time={self.time}, status='{self.status}', " \
               "rsvp_limit={self.rsvp_limit}, waitlist_count={self.waitlist_count}, yes_rsvp_count={" \
               "self.yes_rsvp_count}, announced={self.announced}, event_url='{self.event_url}', " \
               "venue={self.venue}, participants={self.participants})".format_map(vars())


class Rsvp:
    def __init__(self, venue, response, answers, member, **kwargs):
        self.member = member
        self.answers = answers
        self.response = response
        self.venue = venue
        _ = kwargs


class GameTable:
    def __init__(self, number, title, blurb=None, max_players=None, players=None, gm=None, system=None):
        self.number = number
        self._players = []
        self.system = system
        self.gm = gm
        self.max_players = max_players
        self.players = players
        self.blurb = blurb
        self.title = title

    def add_player(self, player):
        self.players.append(player)

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        if value is None:
            value = []
        self._players = value
