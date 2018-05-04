from evennia import DefaultObject


class Dialog(DefaultObject):
    """
    A dialog spoken by NPCs
    Should be tagged with NPC name, location, and quest (if applicable)
    """

    def at_object_creation(self):
        self.db.nodes = {}
