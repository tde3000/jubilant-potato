"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter
from world.questlog import QuestLog
from world.utils import search_tags
from evennia.utils.evmenu import EvMenu


class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """

    def at_object_creation(self):
        self.db.quest_log = QuestLog()
        self.db.trackers = {}


class CharNPC(Character):
    """
    An NPC typeclass which extends character.
    Able to reply to talk command
    """
    DEFAULT_GREETING = "Hello, stranger"

    def at_object_creation(self):
        self.greeting = self.DEFAULT_GREETING

    def generate_menu_data(self, caller):
        menu_data = {"start":
                         lambda caller:(
                             self.greeting,
                             {}
                         )
                     }
        # add other eligilble dialogs
        return menu_data

    def talk(self, caller):
        menu_data = self.generate_menu_data(caller)
        EvMenu(caller, menu_data)

    @property
    def greeting(self):
        return self.db.greeting

    @greeting.setter
    def greeting(self, greeting):
        self.db.greeting = greeting



