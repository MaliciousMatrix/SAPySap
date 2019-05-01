from duration import Duration

class Availability(Duration):
    def __init__(self, datetimespan, *args, **kwargs):
        return super().__init__(datetimespan.start_time, datetimespan.end_time, *args, **kwargs)

    def __str__(self):
        return 'Availability from %s to %s' % (self.start_time, self.end_time)
