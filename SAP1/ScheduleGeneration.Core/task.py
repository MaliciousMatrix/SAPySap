import datetime
from named_with_id import NamedWithId
from duration import Duration

class Task(NamedWithId):
    def __init__(self, id, name, duration, required_number_of_employees, group, location, category, *args, **kwargs):
        self.duration = duration 
        self.required_number_of_employees = required_number_of_employees
        self.group = group
        self.location = location
        self.category = category
        return super().__init__(id, name, *args, **kwargs)

    def set_duration(self, value):
        self._duration = value

    def get_duration(self):
        return self._duration

    def set_required_number_of_employees(self, value):
        assert value > 0, "The number of employees required for this task must be greater than zero. Not: " + str(value)
        assert isinstance(value, int), "The number of employees required for this task must be an integer. Not: " + str(value)

        self._required_number_of_employees = value;

    def get_required_number_of_employees(self):
        return self._required_number_of_employees

    def set_group(self, value):
        self._group = value

    def get_group(self):
        return self._group

    def set_location(self, value):
        self._location = value

    def get_location(self):
        return self._location

    def set_category(self, value):
        self._category = value

    def get_category(self):
        return self._category

    def needs_staff(self, staff_members):
        return self.required_number_of_employees > self.get_amount_of_assigned_staff(staff_members)

    def get_assigned_staff(self, staff_members):
        members_assigned = []
        for member in staff_members:
            if member.has_task(self):
                members_assigned.append(member)

        return members_assigned

    def get_amount_of_assigned_staff(self, staff_members):
        return len(self.get_assigned_staff(staff_members))

    def get_amount_of_needed_staff(self, staff_members):
        return self.required_number_of_employees - self.get_amount_of_assigned_staff(staff_members)

    def has_too_many_staff(self, staff_members):
        return self.get_amount_of_needed_staff(staff_members) < 0

    def staff_who_can_take_this_task(self, staff_members):
        staff = []
        for member in staff_members:
            if member.can_assign_task(self):
                staff.append(member)
        return staff

    def amount_of_staff_who_can_take_this_task(self, staff_members):
        return len(self.staff_who_can_take_this_task(staff_members))

    duration = property(get_duration, set_duration)
    required_number_of_employees = property(get_required_number_of_employees, set_required_number_of_employees)
    group = property(get_group, set_group)
    location = property(get_location, set_location)
    category = property(get_category, set_category)

    def get_length_in_hours(self):
        return self.duration.get_length_in_hours()

    def get_is_on_date(self, date):
        return self.duration.is_on_date(date)

    def conflicts_with(self, task):
        return self.duration.conflicts_with(task.duration)

    def __eq__(self, value):
        return isinstance(value, Task) and \
            self.required_number_of_employees == value.required_number_of_employees and \
            self.duration == value.duration and \
            self.category == value.category and \
            self.location == value.location and \
            self.group == value.group and \
            super().__eq__(value)

    def __str__(self):
        return 'Task %s for %s poeple on %s @ %s' % (self.name, str(self.required_number_of_employees), self.duration, self.location)