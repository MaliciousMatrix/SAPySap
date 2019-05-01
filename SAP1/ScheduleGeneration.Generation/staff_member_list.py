from staff_member import StaffMember

class StaffMemberList(list):

    def __init__(self, iterable):
        return super().__init__(iterable)

    #Minimums 
    #region
    def where_not_at_minimum_hours_per_week(self):
        return StaffMemberList(list(filter(lambda x: not x.is_at_minimum_hours_per_week(), self[:])))

    def where_is_at_minimum_hours_per_week(self):
        return StaffMemberList(list(filter(lambda x: x.is_at_minimum_hours_per_week(), self[:])))
    
    def where_is_over_minimum_hours_per_week(self):
        return StaffMemberList(list(filter(lambda x: x.is_over_minimum_hours_per_week(), self[:])))

    def where_would_be_at_minimum_hours_if_task_was_assigned(self, task):
        return StaffMemberList(list(filter(lambda x: x.would_be_at_minimum_hours_if_task_was_assigned(task), self[:])))

    def where_would_be_over_minimum_hours_if_task_was_assigned(self, task):
        return StaffMemberList(list(filter(lambda x: x.would_be_over_minimum_hours_if_task_was_assigned(task), self[:])))
    #endregion

    #Targets
    #region
    def where_not_at_target_hours_per_week(self):
        return StaffMemberList(list(filter(lambda x: not x.is_at_target_hours_per_week(), self[:])))

    def where_is_at_target_hours_per_week(self):
        return StaffMemberList(list(filter(lambda x: x.is_at_target_hours_per_week(), self[:])))
    
    def where_is_over_target_hours_per_week(self):
        return StaffMemberList(list(filter(lambda x: x.is_over_target_hours_per_week(), self[:])))

    def where_would_be_at_target_hours_if_task_was_assigned(self, task):
        return StaffMemberList(list(filter(lambda x: x.would_be_at_target_hours_if_task_was_assigned(task), self[:])))

    def where_would_be_over_target_hours_if_task_was_assigned(self, task):
        return StaffMemberList(list(filter(lambda x: x.would_be_over_target_hours_if_task_was_assigned(task), self[:])))
    #endregion

    #Maximums
    #region
    def where_not_at_maximum_hours_per_week(self):
        return StaffMemberList(list(filter(lambda x: not x.is_at_maximum_hours_per_week(), self[:])))

    def where_is_at_maximum_hours_per_week(self):
        return StaffMemberList(list(filter(lambda x: x.is_at_maximum_hours_per_week(), self[:])))

    def where_would_be_at_maximum_hours_if_task_was_assigned(self, task):
        return StaffMemberList(list(filter(lambda x: x.would_be_at_maximum_hours_if_task_was_assigned(task), self[:])))
    #endregion

    #overtime
    #region
    def where_not_at_overtime_hours_per_week(self):
        return StaffMemberList(list(filter(lambda x: not x.is_at_overtime_per_week(), self[:])))

    def where_is_at_overtime_hours_per_week(self):
        return StaffMemberList(list(filter(lambda x: x.is_at_overtime_hours_per_week(), self[:])))

    def where_would_be_at_overtime_hours_if_task_was_assigned(self, task):
        return StaffMemberList(list(filter(lambda x: x.would_be_at_overtime_hours_if_task_was_assigned(task), self[:])))

    def where_would_be_over_overtime_hours_if_task_was_assigned(self, task):
        return StaffMemberList(list(filter(lambda x: not x.would_be_over_overtime_hours_if_task_was_assigned(task), self[:])))
    #endregion

    def where_can_take_this_task(self, task):
        return StaffMemberList(list(filter(lambda x: x.can_assign_task(task), self[:])))

    def where_can_take_this_role(self, role):
        return StaffMemberList(list(filter(lambda x: x.can_assign_role(role), self[:])))

    def where_can_work_in_category(self, category):
        return StaffMemberList(list(filter(lambda x: x.can_work_in_category(category), self[:])))

    def where_is_in_group(self, group):
        return StaffMemberList(list(filter(lambda x: x.is_in_group(group), self[:])))

    def where_has_task(self, task):
        return StaffMemberList(list(filter(lambda x: x.has_task(task), self[:])))

    def where_can_remove_task(self, task):
        return StaffMemberList(list(filter(lambda x: x.can_remove_task(task), self[:])))

    def where_has_availability_for_duration(self, duration):
        return StaffMemberList(list(filter(lambda x: x.has_availability_for_duration(duration), self[:])))

    def where_has_tasks_conflicting_with(self, duration):
        return StaffMemberList(list(filter(lambda x: x.has_tasks_conflicting_with(duration), self[:])))

    def where_has_preference_for_category(self, category):
        return StaffMemberList(list(filter(lambda x: x.has_preference_for_category(category), self[:])))

    def where_likes_task(self, task):
        return StaffMemberList(list(filter(lambda x: x.likes_task(task), self[:])))

    def where_indifferent_about_task(self, task):
        return StaffMemberList(list(filter(lambda x: x.indifferent_about_task(task), self[:])))

    def where_dislikes_task(self, task):
        return StaffMemberList(list(filter(lambda x: x.dislikes_task(task), self[:])))

    def where_is_happy(self):
        return StaffMemberList(list(filter(lambda x: x.is_happy(), self[:])))

    def where_is_unhappy(self):
        return StaffMemberList(list(filter(lambda x: x.is_unhappy(), self[:])))

    def total_minimum_hours(self):
        minimum_hours = 0
        for s in self[:]:
            minimum_hours = minimum_hours + s.minimum_hours_per_week
        return minimum_hours

    def total_target_hours(self):
        target_hours = 0
        for s in self[:]:
            target_hours = target_hours + s.target_hours_per_week
        return target_hours

    def total_maximum_hours(self):
        maximum_hours = 0
        for s in self[:]:
            maximum_hours = maximum_hours + s.maximum_hours_per_week
        return maximum_hours
