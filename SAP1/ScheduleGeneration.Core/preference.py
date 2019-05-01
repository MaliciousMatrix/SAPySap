class Preference:
    def __init__(self, category, likness, can_work, *args, **kwargs):
        self.category = category
        if not can_work:
            likness = 0
        self.likness = likness
        self.can_work = can_work
        return super().__init__(*args, **kwargs)    

    def __str__(self):
        return 'Preference %s for %s' % (self.likeness, self.category)

    def __eq__(self, value):
        return self.category == value.category and \
            self.likness == value.likness and \
            self.can_work == value.can_work

    def set_category(self, value):
        assert value is not None, 'category cannot be none.'
        self._category = value

    def get_category(self):
        return self._category

    def set_likness(self, value):
        assert isinstance(value, int), 'likness must be an integer. Not: ' + str(value)
        assert Preference.get_min_likness() <= value <= Preference.get_max_likness(), 'likness must be between [%d, %d]. Not: %s' % (Preference.get_min_likness(), Preference.get_max_likness(), str(value))
        self._likness = value
        
    def get_likness(self):
        return self._likness

    def set_can_work(self, value):
        assert isinstance(value, bool), 'can_work must be a boolean value.'
        self._can_work = value

    def get_can_work(self):
        return self._can_work

    category = property(get_category, set_category)
    likness = property(get_likness, set_likness)
    can_work = property(get_can_work, set_can_work)
    
    def get_max_likness():
        return 2

    def get_min_likness():
        return -2

    def get_avg_likness():
        return 0