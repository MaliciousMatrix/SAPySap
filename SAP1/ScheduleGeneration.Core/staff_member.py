from named_with_id import NamedWithId
from bad_task_assignment_exception import BadTaskAssignmentException
from availability import Availability
from category import Category
from group import Group
from duration import Duration
from role import Role
from preference import Preference
from task import Task
from bad_role_assignment_exception import BadRoleAssignmentException

class StaffMember(NamedWithId):
    def __init__(self, id, name, minimum_hours_per_week, target_hours_per_week, maximum_hours_per_week, maximum_hours_per_day, availability, preferences, groups, *args, **kwargs):
        self._is_init = True
        self.minimum_hours_per_week = minimum_hours_per_week
        self.target_hours_per_week = target_hours_per_week
        self.maximum_hours_per_week = maximum_hours_per_week
        self.maximum_hours_per_day = maximum_hours_per_day
        self.availability = availability
        self.preferences = preferences
        self.groups = groups

        self._tasks = [];
        self._unremovable_tasks = []
        self._roles = []
        self._unremovable_roles = []
        self._is_init = False

        return super().__init__(id, name, *args, **kwargs)

    #Hours per week 
    #region
    def set_minimum_hours_per_week(self, value):
        assert value >= 0 and value <= self._hours_in_a_week, 'Minimum hours per week must be >= 0 and < 168. Not: ' + str(value)
        self._minimum_hours_per_week = value

    def get_minimum_hours_per_week(self):
        return self._minimum_hours_per_week
    
    def set_target_hours_per_week(self, value):
        assert value >= self.minimum_hours_per_week and (self._is_init or value <= self.maximum_hours_per_week), 'Target hours per week must be greater than or equal to minimum hours per week.'
        self._target_hours_per_week = value

    def get_target_hours_per_week(self):
        return self._target_hours_per_week

    def set_maximum_hours_per_week(self, value):
        assert value >= self.target_hours_per_week and value <= self._hours_in_a_week, 'Maximum hours per week must be greater than or equal to target hours per week.'
        self._maximum_hours_per_week = value

    def get_maximum_hours_per_week(self):
        return self._maximum_hours_per_week
    #endregion 

    def set_maximum_hours_per_day(self, value):
        assert value >= 0 and value <= 24, 'Maximum hours per day must be >= 0 and <= 24.'
        self._maximum_hours_per_day = value

    def get_maximum_hours_per_day(self):
        return self._maximum_hours_per_day

    # init values
    # region 
    def set_availability(self, value):
        self._availability = value

    def get_availability(self):
        return self._availability

    def set_preferences(self, value):
        self._preferences = value
        self._check_preferences_are_different()

    def get_preferences(self):
        return self._preferences

    def set_groups(self, value):
        self._groups = value

    def get_groups(self):
        return self._groups

    def clear_member(self):
        self._tasks = [];
        self._unremovable_tasks = []
        self._roles = []
        self._unremovable_roles = []
    #endregion

    # Tasks
    #region 

    def can_work_in_category(self, category):
        for preference in self.preferences:
            if preference.category == category:
                return preference.can_work
        # If they have no preference for the category then return true. 
        return True

    def is_in_group(self, group):
        return group in self.groups

    def assign_task(self, task, un_removable = False):
        self._check_if_can_be_assigned(task)
        self._tasks.append(task)
        if un_removable:
            self._unremovable_tasks.append(task)

    def has_task(self, task):
        return task in self._tasks

    def has_unremovable_task(self, task):
        return task in self._unremovable_tasks

    def _remove_unremovable_task(self, task):
        assert self.has_task(task), 'Tried to remove task %s from %s but had no such task.' % (str(task), str(self))
        assert task in self._unremovable_tasks, 'Task must be in the unremovable task list if you want it removed.'
        self._tasks.remove(task)
        self._unremovable_tasks.remove(task)

    def try_remove_task(self, task):
        try:
            self.remove_task(task)
        except:
            return False
        else:
            return True

    def remove_task(self, task):
        assert self.has_task(task), 'Tried to remove task %s from %s but had no such task.' % (str(task), str(self))
        assert task not in self._unremovable_tasks, 'Task cannot be in the unremovable task list.'
        self._tasks.remove(task)

    def can_remove_task(self, task):
        return self.has_task(task) and \
            task not in self._unremovable_tasks

    def try_assign_task(self, task):
        try:
            self.assign_task(task)
        except:
            return False
        else:
            return True

    def can_assign_task(self, task):
        try:
            self._check_if_can_be_assigned(task)
        except:
            return False
        else:
            return True

    # Internally the only place that this should ever be called true from is the would_be_over_maximum_hours_if_task_was_assigned() method
    def _check_if_can_be_assigned(self, task):
        # Cannot assign a task that a member already has. 
        if self.has_task(task):
            raise BadTaskAssignmentException('%s already has task %s.' % (str(self), str(task)))

        # Cannot assign a task to a member that is not in the group the task requires. 
        if not self.is_in_group(task.group):
            raise BadTaskAssignmentException('%s must be a part of group %s.' % (str(self), str(task.group)))

        if not self.can_work_in_category(task.category):
            raise BadTaskAssignmentException('%s  must be able to work in category %s.' % (str(self), str(task.category)))

        if not self.is_available_for_task(task):
            raise BadTaskAssignmentException('Cannot assign %s to %s because it conflicts with another task.' % (str(task), str(self)))

        if self.task_would_put_staff_over_max_hours_per_day(task):
            raise BadTaskAssignmentException('Connot work %s more than %d hours on %s.' % (str(self), self.maximum_hours_per_day, str(task.duration.start_time)))

        if self._would_be_over_maximum_hours_if_task_was_assigned(task):
            raise BadTaskAssignmentException('Connot work %s more than %d hours this cycle.' % (str(self), self.maximum_hours_per_day))

    def clear_tasks(self):
        self._tasks = []
        for task in self._unremovable_tasks:
            self._tasks.append(task)

    def clear_force_assigned_tasks(self):
        self._unremovable_tasks = []

    def is_available_for_task(self, task):
        # First check and see if the staff member is able to take the task in their availability
        if not self.has_availability_for_duration(task.duration):
            return False

        if self.has_task_conflicting_with(task.duration):
            return False
        return True

    def has_availability_for_duration(self, duration):
        '''
        This only checks against the availability. It does not check against the assigned tasks. 
        '''
        for a in self.availability:
            if duration.can_happen_inside_of(a):
                return True

    def has_task_conflicting_with(self, duration):
        return len(self.get_tasks_conflicting_with(duration)) > 0

    def get_tasks_conflicting_with(self, duration):
        conflicting = []
        for t in self._tasks:
            if t.duration.conflicts_with(duration):
                conflicting.append(t)
        return conflicting

    def get_tasks(self):
        return self._tasks

    def tasks_this_can_take(self, tasks):
        a_tasks = []
        for task in tasks:
            if self.can_assign_task(task):
                a_tasks.append(task)
        return a_tasks

    def get_amount_of_tasks_this_can_take(self, tasks):
        return len(self.tasks_this_can_take(tasks))

    #endregion

    # Roles
    #region

    def assign_role(self, role, unremovable = False):
        self._check_assign_role(role)
        self._roles.append(role)
        for task in role.tasks:
            self.assign_task(task, True)

        if unremovable:
            self._unremovable_roles.append(role)

    def can_assign_role(self, role):
        try:
            self._check_assign_role(role)
        except:
            return False
        else:
            return True
            
    def try_assign_role(self, role, unremovable = False):
        try:
            self.assign_role(role, unremovable)
        except:
            return False
        else:
            return True
    
    def can_remove_role(self, role):
        return_value = role in self._roles and \
            role not in self._unremovable_roles

        for task in role.tasks:
            if task not in self._tasks:
                return False

        return return_value

    def remove_role(self, role):
        assert self.can_remove_role(role)
        self._roles.remove(role)

        for task in role.tasks:
            self._remove_unremovable_task(task)

    def try_remove_role(self, role):
        try:
            self.remove_role(role)
        except:
            return False
        else:
            return True

    def has_role(self, role):
        return role in self._roles

    def _check_assign_role(self, role):
        if self.has_role(role):
           raise BadRoleAssignmentException('Tried to assign %s %s but it already has that role' % (str(self), str(role)))

        for task in role.tasks:
           if not self.can_assign_task(task):
               raise BadRoleAssignmentException('Cannot assign a task from this role to this user.')

    def roles_this_can_take(self, roles):
        a_roles = []
        for role in roles:
            if self.can_assign_role(role):
                a_roles.append(role)
        return a_roles

    def get_amount_of_roles_this_can_take(self, roles):
        return len(self.roles_this_can_take(roles))

    def clear_roles(self):
        for r in self._roles:
            self.try_remove_role(r)

    #endregion

    # Minimum hour check
    #region

    def is_at_minimum_hours_per_week(self):
        return self.get_total_hours_working() >= self.minimum_hours_per_week

    def is_over_minimum_hours_per_week(self):
        return self.get_total_hours_working() > self.minimum_hours_per_week

    def would_be_at_minimum_hours_if_task_was_assigned(self, task):
        assert self.can_assign_task(task)
        potential_hours = self.get_total_hours_working() + task.get_length_in_hours()
        return potential_hours >= self.minimum_hours_per_week

    def would_be_over_minimum_hours_if_task_was_assigned(self, task):
        assert self.can_assign_task(task)
        potential_hours = self.get_total_hours_working() + task.get_length_in_hours()
        return potential_hours > self.minimum_hours_per_week

    #endregion

    # target hour check
    #region
    def is_at_target_hours_per_week(self):
        return self.get_total_hours_working() >= self.target_hours_per_week

    def is_over_target_hours_per_week(self):
        return self.get_total_hours_working() > self.target_hours_per_week

    def would_be_at_target_hours_if_task_was_assigned(self, task):
        assert self.can_assign_task(task)
        potential_hours = self.get_total_hours_working() + task.get_length_in_hours()
        return potential_hours >= self.target_hours_per_week

    def would_be_over_target_hours_if_task_was_assigned(self, task):
        assert self.can_assign_task(task)
        potential_hours = self.get_total_hours_working() + task.get_length_in_hours()
        return potential_hours > self.target_hours_per_week

    #endregion

    # Maximum hour check
    #region
    def is_at_maximum_hours_per_week(self):
        return self.get_total_hours_working() >= self.maximum_hours_per_week

    def is_over_maximum_hours_per_week(self):
        return self.get_total_hours_working() > self.maximum_hours_per_week

    def would_be_at_maximum_hours_if_task_was_assigned(self, task):
        assert self.can_assign_task(task)
        potential_hours = self.get_total_hours_working() + task.get_length_in_hours()
        # Equals here because any assignment over the maximum hours per week results in a BadTaskAssignmentException.
        return potential_hours == self.maximum_hours_per_week

    # Private because there is no reason that an outside caller would ever call it. If a task will put a user over the amount of hours allocated 
    # in a cycle then the can_assign_task() will return false. 
    def _would_be_over_maximum_hours_if_task_was_assigned(self, task):
        potential_hours = self.get_total_hours_working() + task.get_length_in_hours()
        return potential_hours > self.maximum_hours_per_week

    #endregion

    # Overtime hour check
    over_time_at = 40
    def is_at_overtime_per_week(self):
        return self.get_total_hours_working() >= self.overtime_at

    def is_over_overtime_hours_per_week(self):
        return self.get_total_hours_working() > self.over_time_at

    def would_be_at_overtime_hours_per_week_if_task_was_assigned(self, task):
        assert self.can_assign_task(task)
        potential_hours = self.get_total_hours_working() + task.get_length_in_hours()
        return potential_hours >= self.overtime_at

    def would_be_over_overtime_hours_if_task_was_assigned(self, task):
        potential_hours = self.get_total_hours_working() + task.get_length_in_hours()
        return potential_hours > self.overtime_at
    
    #endregion

    # Data about hours worked per day / week.  
    #region

    def get_total_hours_working(self):
        hours = 0
        for task in self._tasks:
            hours += task.get_length_in_hours()

        return hours;
    

    def get_hours_worked_on_date(self, date):
        hours = 0
        for task in self._tasks:
            if task.get_is_on_date(date):
                hours += task.get_length_in_hours()

        return hours

    def task_would_put_staff_over_max_hours_per_day(self, task):
        current_hours_on_day = self.get_hours_worked_on_date(task.duration.start_time)
        return current_hours_on_day + task.get_length_in_hours() > self.maximum_hours_per_day

    #endregion

    # Preferences and happiness
    #region 

    def get_preferences_of(self, likness):
        assert Preference.get_min_likness() <= likness <= Preference.get_max_likness(), 'likness must be between [%d, %d]. Not: %s' % (Preference.get_min_likness(), Preference.get_max_likness(), str(likness))
        assert isinstance(likness, int), 'likness must be an integer.'
        return list(filter(lambda x: x.likness == likness, self.preferences))

    def _check_preferences_are_different(self):
        found_category = []
        for pref in self.preferences:
            if pref.category not in found_category:
                found_category.append(pref.category)
            else: #pref.category in found_category
                raise ValueError("preference for category %s was in %s more than once. " % (str(pref.category), str(self)))

    def get_preference_for_category(self, category):
        for pref in self._preferences:
            if pref.category == category:
                return pref.likness
        # By default no one has preferences for each task. Therefore, return preference default. 
        return Preference.get_avg_likness()

    def has_preference_for_category(self, category):
        for pref in self._preferences:
            if pref.category == category:
                return True
        return False

    def get_preference_for_task(self, task):
        return self.get_preference_for_category(task.category)

    def likes_task(self, task):
        return self.get_preference_for_task(task) > 0

    def indifferent_about_task(self, task):
        return self.get_preference_for_task(task) == 0

    def dislikes_task(self, task):
        return self.get_preference_for_task(task) < 0

    def does_not_dislike_task(self, task):
        return self.get_preference_for_task(task) >= 0

    def get_happiness(self):
        happiness = 0
        for task in self._tasks:
            if self.dislikes_task(task):
                happiness -= 1
            elif self.likes_task(task):
                happiness += 1
        return happiness

    def get_tasks_that_make_me_unhappy(self):
        un_happy_tasks = []
        for task in self._tasks:
            if self.dislikes_task(task):
                un_happy_tasks.append(task)
        return un_happy_tasks

    def get_tasks_that_make_me_happy(self):
        happy_tasks = []
        for task in self._tasks:
            if self.likes_task(task):
                happy_tasks.append(task)
        return happy_tasks

    def is_happy(self):
        return self.get_happiness() > 0

    def is_unhappy(self):
        return self.get_happiness() < 0

    #endregion 
    
    minimum_hours_per_week = property(get_minimum_hours_per_week, set_minimum_hours_per_week)
    target_hours_per_week = property(get_target_hours_per_week, set_target_hours_per_week)
    maximum_hours_per_week = property(get_maximum_hours_per_week, set_maximum_hours_per_week)
    maximum_hours_per_day = property(get_maximum_hours_per_day, set_maximum_hours_per_day)
    availability = property(get_availability, set_availability)
    preferences = property(get_preferences, set_preferences)
    groups = property(get_groups, set_groups)

    _hours_in_a_week = 168

    def __str__(self):
        return 'Staff Member ' + self.name
