from evennia import DefaultObject


class Tracker(DefaultObject):

    def at_object_creation(self):
        self.db.name = ""
        self.db.objective = []
        self.db.starting_value = None
        self.db.target_value = []


