from evennia.commands.default.tests import CommandTest
from evennia.utils import create
import typeclasses.characters as characters

class TestQuests(CommandTest):

    def test_quests(self):
        pc = create.create_object(characters.Character, key="pc", location=self.room1)

        self.assertIsNotNone(pc.db.quest_log)
