import datetime
from duration import Duration

class DateConverter:

    def create_duration_on_next_day(self, start_day, end_day, start_time, end_time, current_date=datetime.datetime.now()):
        # TODO: This will need to be redone if we ever change the ability to have start and end dates other than sunday / saturady
        next_start_day = self.__next_weekday(current_date, 6)
        start_day_integer = self.get_week_day_as_python_int(start_day)
        end_day_integer = self.get_week_day_as_python_int(end_day)

        start_date = self.__next_weekday(next_start_day, start_day_integer)
        end_date = self.__next_weekday(next_start_day, end_day_integer)
        
        start_hour = start_time.hour
        start_minute = start_time.minute
        end_hour = end_time.hour
        end_minute = end_time.minute

        start_date = datetime.datetime(start_date.year, start_date.month, start_date.day, start_hour, start_minute)
        end_date = datetime.datetime(end_date.year, end_date.month, end_date.day, end_hour, end_minute)
        return Duration(start_date, end_date)

    def get_week_day_as_python_int(self, day):

        if day == 'Monday':
            return 0
        elif day == 'Tuesday':
            return 1
        elif day == 'Wednesday':
            return 2
        elif day == 'Thursday':
            return 3
        elif day == 'Friday':
            return 4
        elif day == 'Saturday':
            return 5
        elif day == 'Sunday':
            return 6
        else:
            raise ValueError("Could not calculate integer for date " + day)


    def __next_weekday(self, d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0: # Target day already happened this week
            days_ahead += 7
        return d + datetime.timedelta(days_ahead)
