
class Duration:
    def __init__(self, start_date_time, end_date_time, *args, **kwargs):
        self._is_init = True

        self.start_time = start_date_time
        self.end_time = end_date_time

        self._is_init = False

        assert self.start_time < self.end_time, 'start time must be before end time'

        return super().__init__(*args, **kwargs)

    def can_happen_inside_of(self, date_time_span):
        '''
        checks to see if this object can happen inside of the given object. 
        [6 am to 10 am].can_happen_inside_of([6am to 10 am]) => true
        [7 am to 9 am].can_happen_inside_of([6am to 10 am]) => true
        [6 am to 10 am].can_happen_inside_of([7am to 10 am]) => false
        '''
        return self.can_end_inside_of(date_time_span) and self.can_start_inside_of(date_time_span)

    def can_start_inside_of(self, start_time):
        other_start_date = start_time.start_time
        other_end_date = start_time.end_time
        return self.start_time >= other_start_date and self.start_time <= other_end_date

    def can_end_inside_of(self, end_time):
        other_start_date = end_time.start_time
        other_end_date = end_time.end_time

        return self.end_time <= other_end_date and self.end_time >= other_start_date

    def conflicts_with(self, other_time):
        if self.can_end_inside_of(other_time) \
            or self.can_start_inside_of(other_time) \
            or other_time.can_start_inside_of(self) \
            or other_time.can_start_inside_of(self):

            # In this case a DateTimeSpan that ends at 10 does not conflict with one that starts at 10. 
            if self.start_time == other_time.end_time or self.end_time == other_time.start_time:
                return False
            return True

    def __str__(self):
        return '%s to %s' % (self.start_time, self.end_time)

    def set_start_time(self, value):
        assert self._is_init or value < self.end_time, 'start time must be before end time'
        self._start_time = value

    def get_start_time(self):
        return self._start_time

    def set_end_time(self, value):
        assert self._is_init or value > self.start_time, 'start time must be before end time'
        self._end_time = value

    def get_end_time(self):
        return self._end_time

    def get_length_in_hours(self):
        elapsed_time = self.end_time - self.start_time
        return elapsed_time.total_seconds() / 60.0 / 60.0

    def is_on_date(self, date):
        return self.start_time.year == date.year and \
            self.start_time.month == date.month and \
            self.start_time.day == date.day

    start_time = property(get_start_time, set_start_time)
    end_time = property(get_end_time, set_end_time)

    def __eq__(self, value):
        return isinstance(value, Duration) and \
            value.start_time == self.start_time and \
            value.end_time == self.end_time 