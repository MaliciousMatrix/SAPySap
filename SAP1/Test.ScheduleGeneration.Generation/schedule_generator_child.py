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
from ScheduleGenerator import ScheduleGenerator

class ScheduleGeneratorChild(ScheduleGenerator):
    best_ittr = 0
    best_h = 0

    def shuffle_then_schedule(self, settings, all_tasks, all_staff_members, all_roles):
        self.should_print = False
        num_tries = 100
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

            print('@ ' + str(i) + ' found : ' + str(self.get_avg_happiness(staff)))
            if self.get_avg_happiness(staff) > best_happiness:
                latest_best = i
                print('\t best!')
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

        self.should_print = True
        #self.advanced_schedule(settings, best_tasks, best_staff, all_roles)
        #print('Latest best: ' + str(latest_best))
        #self.best_ittr = latest_best
        self.best_h = best_happiness

    found_3 = -1
    def run_till_3(self, settings, all_tasks, all_staff_members, all_roles):
        found_3 = -1
        self.should_print = False
        num_tries = 100
        staff = all_staff_members
        tasks = all_tasks
        best_tasks = []
        best_staff = []
        best_happiness = -10000000
        latest_best = 0
        for i in range(num_tries):
            for s in staff:
                s.clear_roles()
                s.clear_tasks()

            random.shuffle(staff)
            random.shuffle(tasks)
            self.advanced_schedule(settings, tasks, staff, all_roles)

            print('@ ' + str(i) + ' found : ' + str(self.get_avg_happiness(staff)))
            if self.get_avg_happiness(staff) >= 3:
                self.found_3 = i
                return
                           

        self.best_ittr = latest_best
        self.best_h = best_happiness

    found_277 = -1
    def run_till_277(self, settings, all_tasks, all_staff_members, all_roles):
        found_277 = -1
        self.should_print = False
        num_tries = 100
        staff = all_staff_members
        tasks = all_tasks
        best_tasks = []
        best_staff = []
        best_happiness = -10000000
        latest_best = 0
        for i in range(num_tries):
            for s in staff:
                s.clear_roles()
                s.clear_tasks()

            random.shuffle(staff)
            random.shuffle(tasks)
            self.advanced_schedule(settings, tasks, staff, all_roles)

            print('@ ' + str(i) + ' found : ' + str(self.get_avg_happiness(staff)))
            if self.get_avg_happiness(staff) >= 2.77:
                self.found_277 = i
                return
                           

        self.best_ittr = latest_best
        self.best_h = best_happiness

    found_272 = -1
    def run_till_272(self, settings, all_tasks, all_staff_members, all_roles):
        found_272 = -1
        self.should_print = False
        num_tries = 100
        staff = all_staff_members
        tasks = all_tasks
        best_tasks = []
        best_staff = []
        best_happiness = -10000000
        latest_best = 0
        for i in range(num_tries):
            for s in staff:
                s.clear_roles()
                s.clear_tasks()

            random.shuffle(staff)
            random.shuffle(tasks)
            self.advanced_schedule(settings, tasks, staff, all_roles)

            print('@ ' + str(i) + ' found : ' + str(self.get_avg_happiness(staff)))
            if self.get_avg_happiness(staff) >= 2.72:
                self.found_272 = i
                return
                           

        self.best_ittr = latest_best
        self.best_h = best_happiness

    found_281 = -1
    def run_till_281(self, settings, all_tasks, all_staff_members, all_roles):
        found_281 = -1
        self.should_print = False
        num_tries = 100
        staff = all_staff_members
        tasks = all_tasks
        best_tasks = []
        best_staff = []
        best_happiness = -10000000
        latest_best = 0
        for i in range(num_tries):
            for s in staff:
                s.clear_roles()
                s.clear_tasks()

            random.shuffle(staff)
            random.shuffle(tasks)
            self.advanced_schedule(settings, tasks, staff, all_roles)

            print('@ ' + str(i) + ' found : ' + str(self.get_avg_happiness(staff)))
            if self.get_avg_happiness(staff) >= 2.81:
                self.found_281 = i
                return
                           

        self.best_ittr = latest_best
        self.best_h = best_happiness

    def run(self, settings, all_tasks, all_staff_members, all_roles):
        self.should_print = False
        num_tries = 1
        staff = all_staff_members
        tasks = all_tasks
        best_tasks = []
        best_staff = []
        best_happiness = -10000000
        latest_best = 0

        for s in staff:
            s.clear_roles()
            s.clear_tasks()

        random.shuffle(staff)
        random.shuffle(tasks)
        self.advanced_schedule(settings, tasks, staff, all_roles)
        return self.get_avg_happiness(staff)