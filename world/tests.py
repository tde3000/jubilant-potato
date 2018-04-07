from evennia.commands.default.tests import CommandTest
from evennia.utils import create
from typeclasses.rooms import Room
from utils import search_tags

class TestUtils(CommandTest):

    def test_tags(self):
        room1 = create.create_object(Room, key="room1")
        room2 = create.create_object(Room, key="room2")
        room3 = create.create_object(Room, key="room3")

        room1.tags.add("quest1")
        room1.tags.add("forrest", category="zone")

        room2.tags.add("forrest")

        room3.tags.add("quest1")
        room3.tags.add("forrest", category="zone")
        room3.tags.add("npc")

        expected_rooms=[room1, room3]
        rooms = search_tags([["forrest", "zone"], "quest1"])
        intersection = set(expected_rooms).intersection(set(rooms))
        self.assertEquals(len(intersection), len(expected_rooms), "Rooms returned: {}".format(rooms))





