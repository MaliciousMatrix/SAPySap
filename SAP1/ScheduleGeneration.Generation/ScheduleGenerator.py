from availability import Availability
from category import Category
from duration import Duration
from group import Group
from location import Location 
from preference import Preference
from role import Role
from staff_member import StaffMember
from task import Task 
import sys
from staff_member_list import StaffMemberList
from staff_member_sorter import StaffMemberSorter
from task_sorter import TaskSorter
import random

class ScheduleGenerator():
    def __init__(self, staff_members, roles, tasks, *args, **kwargs):
        self.staff_members = StaffMemberList(staff_members)
        self.roles = roles
        self.tasks = tasks
        return super().__init__(*args, **kwargs)

    def schedule(self, settings):
        self.basic_assign_tasks()

    def basic_assign_tasks(self):
        #hardest_to_assign_tasks = self.get_hardest_to_assign_tasks()
        self._assign_tasks_to_members(self.staff_members, self.tasks)

    def _assign_tasks_to_members(self, members, tasks):
        for task in tasks:
            for member in members:
                if not task.needs_staff(self.staff_members):
                    # as soon as the task has been assigned and needs no more members we can break. 
                    break
                member.try_assign_task(task)

    def get_unassigned_tasks(self):
        unassigned_tasks = []
        for task in self.tasks:
            if task.needs_staff(self.staff_members):
                unassigned_tasks.append(task)

        return unassigned_tasks

    def has_unassigned_tasks(self):
        return len(self.get_unassigned_tasks())

    def get_amount_of_unassigned_tasks(self):
        return len(self.get_unassigned_tasks())

    def assign_roles(self, all_staff_members, all_roles):
        roles_to_assign = list(filter(lambda x: x.needs_staff(all_staff_members), all_roles))
        self.print('Assigning Roles: ')
        for role in roles_to_assign: 
                for s in all_staff_members:
                    if s.try_assign_role(role):
                        if role.get_amount_of_needed_staff(all_staff_members) == 0:
                            self.print('Assigned ' + str(role) + ' to ' + str(s))
                            break

    def schedule(self, settings, all_tasks, all_staff_members, all_roles):
        self.should_print = False
        num_tries = 100
        if not settings.use_preferences:
            # Technicilly it'll still schedule twice but that's not really an issue. 
            num_tries = 1
        staff = all_staff_members
        tasks = all_tasks
        best_tasks = []
        best_staff = []
        best_happiness = -10000000
        latest_best = 0
        for i in range(num_tries):
            random.shuffle(staff)
            random.shuffle(tasks)
            self.advanced_schedule(settings, tasks, staff, all_roles)

            #print('@ ' + str(i) + ' found : ' + str(self.get_avg_happiness(staff)))

            if self.get_avg_happiness(staff) > best_happiness:
                latest_best = i
                #print('\t best!')
                best_tasks = []
                best_staff = StaffMemberList([])
                for t in tasks:
                    best_tasks.append(t)

                for s in staff:
                    best_staff.append(s)

                best_happiness = self.get_avg_happiness(staff)
            
            for s in staff:
                s.clear_roles()
                s.clear_tasks()

        #self.should_print = True
        self.advanced_schedule(settings, best_tasks, best_staff, all_roles)
        print(' found : ' + str(self.get_avg_happiness(staff)))


    def go_to_minimums(self, all_staff_members, all_tasks, avoid_overtime, staff_members, tasks, use_preferences):
        self.print('Going to minimums:')
        while(len(tasks) > 0):
            hardest_to_assign_task = TaskSorter.get_most_difficult_task_to_assign(tasks, staff_members)
            if hardest_to_assign_task == None:
                break
            
            if use_preferences:
                working_staff_list = StaffMemberList(list(filter(lambda x: not x.is_at_minimum_hours_per_week() and x.likes_task(hardest_to_assign_task), staff_members)))
                if len(working_staff_list) == 0:
                    working_staff_list = StaffMemberList(list(filter(lambda x: not x.is_at_minimum_hours_per_week() and x.indifferent_about_task(hardest_to_assign_task), staff_members)))
                    if len(working_staff_list) == 0:
                        working_staff_list = staff_members.where_not_at_minimum_hours_per_week()
            else:
                working_staff_list = staff_members.where_not_at_minimum_hours_per_week()
        
            if avoid_overtime:
                working_staff_list = working_staff_list.where_would_be_over_overtime_hours_if_task_was_assigned(hardest_to_assign_task)
            working_staff_list = StaffMemberSorter.get_least_available_staff_members_for_tasks(tasks, working_staff_list)
                
        
            if len(working_staff_list) == 0:
                break
        
            for s in working_staff_list:
                if s.try_assign_task(hardest_to_assign_task):
                    self.print('\tAssigned Task ' + hardest_to_assign_task.name + ' to ' + s.name + ' @ ' + str(s.get_total_hours_working()) + ' / ' + str(s.get_minimum_hours_per_week()))
                    # Only get here if assignment was successful
                    if not hardest_to_assign_task.needs_staff(all_staff_members):
                        # if we don't need any more staff for this task, break
                        break
        
            tasks.remove(hardest_to_assign_task)
        
        self.print('Going to targets:')
        tasks = list(filter(lambda x: x.needs_staff(all_staff_members), all_tasks))
        return hardest_to_assign_task, tasks

    def go_to_targets(self, all_staff_members, avoid_overtime, staff_members, tasks, use_preferences):
        while(len(tasks) > 0):
            hardest_to_assign_task = TaskSorter.get_most_difficult_task_to_assign(tasks, staff_members)
            if hardest_to_assign_task == None:
                break
            
            if use_preferences:
                working_staff_list = StaffMemberList(list(filter(lambda x: not x.is_at_target_hours_per_week() and x.likes_task(hardest_to_assign_task), staff_members)))
                if len(working_staff_list) == 0:
                    working_staff_list = StaffMemberList(list(filter(lambda x: not x.is_at_target_hours_per_week() and x.indifferent_about_task(hardest_to_assign_task), staff_members)))
                    if len(working_staff_list) == 0:
                        working_staff_list = staff_members.where_not_at_target_hours_per_week()
            else:
                working_staff_list = staff_members.where_not_at_target_hours_per_week()
        
            if avoid_overtime:
                working_staff_list = working_staff_list.where_would_be_over_overtime_hours_if_task_was_assigned(hardest_to_assign_task)
            working_staff_list = StaffMemberSorter.get_least_available_staff_members_for_tasks(tasks, working_staff_list)
        
            if len(working_staff_list) == 0:
                break
        
            for s in working_staff_list:
                if s.try_assign_task(hardest_to_assign_task):
                    self.print('\tAssigned Task ' + hardest_to_assign_task.name + ' to ' + s.name + ' @ ' + str(s.get_total_hours_working()) + ' / ' + str(s.get_target_hours_per_week()))
                    # Only get here if assignment was successful
                    if not hardest_to_assign_task.needs_staff(all_staff_members):
                        # if we don't need any more staff for this task, break
                        break
        
            tasks.remove(hardest_to_assign_task)
        return hardest_to_assign_task

    def go_to_maximums(self, all_staff_members, all_tasks, avoid_overtime, staff_members, use_preferences):
        self.print('Going to maximums:')
        tasks = list(filter(lambda x: x.needs_staff(all_staff_members), all_tasks))
        while(len(tasks) > 0):
            hardest_to_assign_task = TaskSorter.get_most_difficult_task_to_assign(tasks, staff_members)
            if hardest_to_assign_task == None:
                break
        
            if use_preferences:
                working_staff_list = StaffMemberList(list(filter(lambda x: not x.is_at_maximum_hours_per_week() and x.likes_task(hardest_to_assign_task), staff_members)))
                if len(working_staff_list) == 0:
                    working_staff_list = StaffMemberList(list(filter(lambda x: not x.is_at_maximum_hours_per_week() and x.indifferent_about_task(hardest_to_assign_task), staff_members)))
                    if len(working_staff_list) == 0:
                        working_staff_list = staff_members.where_not_at_maximum_hours_per_week()
            else:
                working_staff_list = staff_members.where_not_at_maximum_hours_per_week()
            
            if avoid_overtime:
                working_staff_list = working_staff_list.where_would_be_over_overtime_hours_if_task_was_assigned(hardest_to_assign_task)
            working_staff_list = StaffMemberSorter.get_least_available_staff_members_for_tasks(tasks, working_staff_list)
        
            if len(working_staff_list) == 0:
                break
        
            for s in working_staff_list:
                if s.try_assign_task(hardest_to_assign_task):
                    self.print('\tAssigned Task ' + hardest_to_assign_task.name + ' to ' + s.name + ' @ ' + str(s.get_total_hours_working()) + ' / ' + str(s.get_maximum_hours_per_week()))
                    # Only get here if assignment was successful
                    if not hardest_to_assign_task.needs_staff(all_staff_members):
                        # if we don't need any more staff for this task, break
                        break
        
            tasks.remove(hardest_to_assign_task)

    def advanced_schedule(self, settings, tasks, staff, roles):

        all_tasks = []
        all_staff_members = StaffMemberList([])
        all_roles = []
        for t in tasks:
            all_tasks.append(t)

        for s in staff:
            all_staff_members.append(s)

        for r in roles:
            all_roles.append(r)

        use_preferences = settings.use_preferences
        start_overtime_at = settings.overtime_start_at
        avoid_overtime = settings.avoid_overtime

        self.assign_roles(all_staff_members, all_roles)
        tasks = list(filter(lambda x: x.needs_staff(all_staff_members), all_tasks))

        members = []
        for m in all_staff_members:
            m.overtime_at = start_overtime_at
            members.append(m)
        staff_members = StaffMemberList(members)



        hardest_to_assign_task, tasks = self.go_to_minimums(all_staff_members, all_tasks, avoid_overtime, staff_members, tasks, use_preferences)
        hardest_to_assign_task = self.go_to_targets(all_staff_members, avoid_overtime, staff_members, tasks, use_preferences)
        self.go_to_maximums(all_staff_members, all_tasks, avoid_overtime, staff_members, use_preferences)

        self.try_trade_tasks(all_staff_members, all_tasks)

        self.print('Unassigned: ')
        self.print(len(self.get_unassigned_tasks()))

        self.print_happy(all_staff_members)
        self.print_unhappy(all_staff_members)
        self.get_avg_happiness(all_staff_members)
        if use_preferences:
            self.try_increase_happiness(all_staff_members, all_tasks)
            self.get_avg_happiness(all_staff_members)

    def print_unhappy(self, staff):
        self.print('Unhappy:')
        for s in staff.where_is_unhappy():
            self.print(str(s))

    def print_happy(self, staff):
        self.print('Happy:')
        for s in staff.where_is_happy():
            self.print(str(s))
    
    def get_avg_happiness(self, staff):
        total = len(staff)
        happiness = 0
        for s in staff:
            happiness = happiness + s.get_happiness()

        self.print('H: ' + str(happiness))
        self.print('Avg H: ' + str(happiness / total))
        return (happiness / total)

    def print(self, message):
        if(self.should_print):
            print(message)

    should_print = True

    def try_trade_tasks(self, staff, tasks):
        self.print('Trading')
        un_assigned = self.get_unassigned_tasks()
        for task in un_assigned:
            for i in range(task.get_amount_of_needed_staff(staff)):
                # First try to assign the task to any member:
                assigned = False
                for s in staff:
                    if s.try_assign_task(task):
                        assigned = True
                        break
                if assigned:
                    break

        un_assigned = self.get_unassigned_tasks()
        for task in un_assigned:
            for i in range(task.get_amount_of_needed_staff(staff)):
                for s in staff:
                    conflicting_tasks = s.get_tasks_conflicting_with(task.duration)
                    if len(conflicting_tasks) == 1:
                        conflict = conflicting_tasks[0] # r
                        if s.can_remove_task(conflict):
                            s.remove_task(conflict) # REMOVED THE TASK
                            if s.try_assign_task(task):
                                assigned_conflicting_task = False
                                for m in staff:
                                    if m.try_assign_task(conflict):
                                        self.print('\t' + str(s) + ' got the unassigned task ' + str(task.name))
                                        self.print('\t' + str(m) + ' got the conflicting task ' + str(conflict.name))
                                        assigned_conflicting_task = True
                                        break
                                if not assigned_conflicting_task:
                                    s.remove_task(task)
                                    s.assign_task(conflict)
                            else: # We cannot assign the un-assigned task
                                # Re-assign
                                s.assign_task(conflict)

    def try_increase_happiness(self, staff, tasks):
        self.print('Making Happier.')
        # Sort the members so the unhappiest members go first. 
        unhappy = sorted(staff, key=lambda x: x.get_happiness(), reverse=False)
        for member in unhappy:
            tasks_that_make_member_un_happy = member.get_tasks_that_make_me_unhappy()
            for task_that_makes_member_un_happy in tasks_that_make_member_un_happy:
                assigned = False
                # First try to assign the task to members that like it. 
                staff_who_like_this_task = staff.where_likes_task(task_that_makes_member_un_happy)
                staff_who_could_take_task = []
                for like_task in staff_who_like_this_task:
                    # Next try to find conflicting tasks if any. 
                    conflicting_tasks = like_task.get_tasks_conflicting_with(task_that_makes_member_un_happy.duration)
                    if len(conflicting_tasks) == 0 and like_task.can_assign_task(task_that_makes_member_un_happy):
                        # If there are no conflicting tasks and we can simply assign it then we set those asside for now. 
                        staff_who_could_take_task.append(like_task)

                    if len(conflicting_tasks) == 1 and member.does_not_dislike_task(conflicting_tasks[0]):
                        conflict = conflicting_tasks[0]
                        if like_task.can_remove_task(conflict):
                            like_task.remove_task(conflict) # REMOVED THE TASK
                            if like_task.try_assign_task(task_that_makes_member_un_happy):
                                if member.try_assign_task(conflict):
                                    self.print('Traded two tasks to make members happier!')
                                    assigned = True
                                    break
                                else:
                                    like_task.remove_task(task_that_makes_member_un_happy)
                                    like_task.assign_task(conflict)
                            else:
                                like_task.assign_task(conflict)
                if not assigned:
                    for s in staff_who_could_take_task:
                        if s.try_assign_task(task_that_makes_member_un_happy):
                            member.remove_task(task_that_makes_member_un_happy)
                            self.print('Gave a task away to increase happiness!')
                            assigned = True
                            break

        unhappy = sorted(staff, key=lambda x: x.get_happiness(), reverse=False)
        for member in unhappy:
            tasks_that_make_member_un_happy = member.get_tasks_that_make_me_unhappy()
            for task_that_makes_member_un_happy in tasks_that_make_member_un_happy:
                assigned = False
                # First try to assign the task to members that like it. 
                staff_who_like_this_task = staff.where_indifferent_about_task(task_that_makes_member_un_happy)
                staff_who_could_take_task = []
                for like_task in staff_who_like_this_task:
                    # Next try to find conflicting tasks if any. 
                    conflicting_tasks = like_task.get_tasks_conflicting_with(task_that_makes_member_un_happy.duration)
                    if len(conflicting_tasks) == 0 and like_task.can_assign_task(task_that_makes_member_un_happy):
                        # If there are no conflicting tasks and we can simply assign it then we set those asside for now. 
                        staff_who_could_take_task.append(like_task)

                    if len(conflicting_tasks) == 1 and member.does_not_dislike_task(conflicting_tasks[0]):
                        conflict = conflicting_tasks[0]
                        if like_task.can_remove_task(conflict):
                            like_task.remove_task(conflict) # REMOVED THE TASK
                            if like_task.try_assign_task(task_that_makes_member_un_happy):
                                if member.try_assign_task(conflict):
                                    self.print('Traded two tasks to make members happier! 2')
                                    assigned = True
                                    break
                                else:
                                    like_task.remove_task(task_that_makes_member_un_happy)
                                    like_task.assign_task(conflict)
                            else:
                                like_task.assign_task(conflict)
                if not assigned:
                    for s in staff_who_could_take_task:
                        if s.try_assign_task(task_that_makes_member_un_happy):
                            member.remove_task(task_that_makes_member_un_happy)
                            self.print('Gave a task away to increase happiness! 2')
                            assigned = True
                            break
                        

        



