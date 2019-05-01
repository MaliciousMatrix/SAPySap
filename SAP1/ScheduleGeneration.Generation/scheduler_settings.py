class SchedulerSettings:
    def __init__(self, avoid_overtime, overtime_start_at, use_preferences, allow_split_shifts):
        self.avoid_overtime = avoid_overtime
        self.overtime_start_at = overtime_start_at
        self.use_preferences = use_preferences
        self.allow_split_shifts = allow_split_shifts

    def set_avoid_overtime(self, value):
        assert isinstance(value, bool), 'The avoid overtime value must be a boolean.'
        self._avoid_overtime = value

    def get_avoid_overtime(self):
        return self._avoid_overtime

    def set_overtime_start_at(self, value):
        assert isinstance(value, float) or isinstance(value, int)
        self._overtime_start_at = value

    def get_overtime_start_at(self):
        return self._overtime_start_at

    def set_use_preferences(self, value):
        assert isinstance(value, bool)
        self._use_preferences = value

    def get_use_preferences(self):
        return self._use_preferences

    def get_allow_split_shifts(self):
        return self._allow_split_shifts

    def set_allow_split_shifts(self, value):
        assert isinstance(value, bool)
        self._allow_split_shifts = value

    avoid_overtime = property(get_avoid_overtime, set_avoid_overtime)
    overtime_start_at = property(get_overtime_start_at, set_overtime_start_at)
    use_preferences = property(get_use_preferences, set_use_preferences)
    allow_split_shifts = property(get_allow_split_shifts, set_allow_split_shifts)




