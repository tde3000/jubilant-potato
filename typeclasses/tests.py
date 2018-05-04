from evennia.commands.default.tests import CommandTest
from evennia.utils import create
import typeclasses.characters as characters
from typeclasses.quests import Quest


class TestTypeclasses(CommandTest):

    def test_quests(self):
        pc = create.create_object(characters.Character, key="pc", location=self.room1)

        self.assertIsNotNone(pc.db.quest_log, "A new character was created without a quest log")

    def test_NPC(self):
        npc = create.create_object(characters.CharNPC, key="npc", location=self.room1)

        default_greeting = characters.CharNPC.DEFAULT_GREETING
        self.assertEquals(npc.greeting, default_greeting, "NPCs aren't created with default greeting '{}'".format(default_greeting))

        new_greeting = "Hello, my name is Inigo Montoya. You killed my father, prepare to die!"
        npc.greeting = new_greeting
        self.assertEquals(npc.greeting, new_greeting, "Couldn't set NPC greeting to '{}'".format(new_greeting))

    def test_generate_menu_data(self):
        pc = create.create_object(characters.Character, key="pc", location=self.room1)
        npc = create.create_object(characters.CharNPC, key="npc2", location=self.room1)

        default_greeting = characters.CharNPC.DEFAULT_GREETING
        dialog = npc.generate_menu_data(npc)
        greeting = dialog["start"](npc)[0]

        self.assertEquals(greeting, default_greeting, "Start node doesn't contain the default greeting, instaed contains '{}'".format(greeting))

