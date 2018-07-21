from evennia import DefaultObject
from tracker import Tracker


class Dialog(DefaultObject):
    """
    A dialog spoken by NPCs
    Should be tagged with NPC name, location, initial, and quest (if applicable)
    """

    def at_object_creation(self):
        self.db.text = ""
        self.db.pre_reqs = []
        self.db.upon_completion = []
        self.db.nodes = {}

    @property
    def text(self):
        return self.db.text

    @text.setter
    def text(self, text):
        self.db.text = text

    @property
    def pre_reqs(self):
        return self.db.pre_reqs

    def add_pre_req(self, tracker, state):
        """

        :param tracker:
            typeclasses.tracker.Tracker

        :param state:
            one of these:
            "=="
            "<"
            ">="
            None
        :return:
        """

        allowed_states = ["==", "<", ">", "<=", ">=", "!=", None]

        if type(tracker) is not Tracker:
            raise ValueError("tracker type is {}, should be typeclasses.tracker.Tracker")

        if state not in allowed_states:
            raise ValueError("{} is not one of the allowed states: {}".format(state, allowed_states))

        pre_req = (tracker, state)

        self.db.pre_reqs.append(pre_req)

    @property
    def upon_completion(self):
        return self.db.upon_completion

    def add_upon_complition(self, upon_complition):
        allowed_types = ["quest", "tracker", "reward"]
        upon_completion_type = upon_complition[0]

        if upon_completion_type not in allowed_types:
            raise ValueError("{} is not in {}".format(upon_completion_type, allowed_types))

        self.db.upon_completion.append(upon_complition)
