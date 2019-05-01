from task import Task
from named_with_id import NamedWithId

class Role(NamedWithId):
    def __init__(self, id, name, tasks, required_number_of_employees, *args, **kwargs):
        self._check_tasks_dont_conflict(tasks)
        self._tasks = tasks
        self.required_number_of_employees = required_number_of_employees

        return super().__init__(id, name, *args, **kwargs)

    def __str__(self):
        return 'Role %s with %s tasks for %s employees' % (self.name, str(len(self.tasks)), str(self.required_number_of_employees))

    def get_tasks(self):
        return self._tasks

    def set_required_number_of_employees(self, value):
        assert value > 0, "The number of employees required for this role must be greater than zero. Not: " + str(value)
        assert isinstance(value, int), "The number of employees required for this role must be an integer. Not: " + str(value)
        for task in self._tasks:
            assert value <= task.required_number_of_employees, 'The number of required employees cannot excede the needed amount of any task.'
        self._required_number_of_employees = value

    def get_required_number_of_employees(self):
        return self._required_number_of_employees

    tasks = property(get_tasks)
    required_number_of_employees = property(get_required_number_of_employees, set_required_number_of_employees)

    def _check_tasks_dont_conflict(self, tasks):
        task_count = len(tasks)
        for i in range(task_count):
            for j in range(i + 1, task_count):
                assert not tasks[i].conflicts_with(tasks[j])

    def needs_staff(self, staff_members):
        return self.required_number_of_employees > self.get_amount_of_assigned_staff(staff_members)

    def get_assigned_staff(self, staff_members):
        members_assigned = []
        for member in staff_members:
            if member.has_role(self):
                members_assigned.append(member)
        return members_assigned

    def get_amount_of_assigned_staff(self, staff_members):
        return len(self.get_assigned_staff(staff_members))

    def get_amount_of_needed_staff(self, staff_members):
        return self.required_number_of_employees - self.get_amount_of_assigned_staff(staff_members)

    def has_too_many_staff(self, staff_members):
        return self.get_amount_of_needed_staff(staff_members) < 0

    def staff_who_can_take_this_role(self, staff_members):
        staff = []
        for member in staff_members:
            if member.can_assign_role(self):
                staff.append(member)
        return staff

    def amount_of_staff_who_can_take_this_role(self, staff_members):
        return len(self.staff_who_can_take_this_role(staff_members))

    def __eq__(self, value):
        return super().__eq__(value)