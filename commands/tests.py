from evennia.commands.default.tests import CommandTest
from commands.command import CmdTalk
from typeclasses.objects import Object
from evennia.utils import create

import typeclasses.characters as characters

class TestTalk(CommandTest):
    """
     Unit tests for CmdTalk
    """

    def test_talk(self):
        obj3 = create.create_object(Object, key="TestObj", location=self.room1)
        other_pc = create.create_object(characters.Character, key="other_pc", location=self.room1)
        npc = create.create_object(characters.CharNPC, key="npc", location=self.room1)

        expected_no_args = "Who are you talking to?"
        expected_too_many_args = "You can only talk to one character at a time."
        expected_npc = "{} says hello."
        expected_pc = "You can just say something out loud or tell {} something privately."
        expected_obj = "You can't talk to objects, silly."
        expected_not_found = "Could not find '{}'."

        self.call(CmdTalk(), "", expected_no_args, caller=self.char1)
        self.call(CmdTalk(), "1 2", expected_too_many_args, caller=self.char1)
        self.call(CmdTalk(), npc.key, expected_npc.format(npc.key), caller=self.char1)
        self.call(CmdTalk(), other_pc.key, expected_pc.format(other_pc.key), caller=self.char1)
        self.call(CmdTalk(), obj3.key, expected_obj, caller=self.char1)
        self.call(CmdTalk(), "nothere", expected_not_found.format("nothere"), caller=self.char1)
