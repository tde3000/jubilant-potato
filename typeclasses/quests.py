from evennia import DefaultObject


class Quest(DefaultObject):
    def __init__(self,
                 pre_text = None,
                 mid_text = None,
                 end_text = None):
        self.pre_text = pre_text
        self.mid_text = mid_text
        self.end_text = end_text