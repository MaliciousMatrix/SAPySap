import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Generation')
sys.path.append(os.getcwd() + '\\..\\TestCommon')
from availability import Availability
from category import Category
from duration import Duration
from group import Group
from location import Location 
from preference import Preference
from role import Role
from staff_member import StaffMember
from task import Task
from TestCommon import CommonTestFunctions
from camp_staff_common import CampStaffCommon
from CampTaskCommon import CampTaskCommon
from bad_task_assignment_exception import BadTaskAssignmentException
from availability_getter import AvailabilityGetter
from duration_getter import DurationGetter
from staff_member_list import StaffMemberList
from ScheduleGenerator import ScheduleGenerator
from schedule_generator_child import ScheduleGeneratorChild
from scheduler_settings import SchedulerSettings

class TestLiquorStoreSchedule(unittest.TestCase):
    
    def test_scheduling(self):
        generic = CommonTestFunctions()
        location = generic.location(1, 'Sarrack\'s Wine and Spirits')
        
        cashier_group = generic.group(1, 'Cashier')
        manager_group = generic.group(2, 'Manager')
        employee_group = generic.group(3, 'Employee')

        cashier_category = generic.category(1, 'Cashiering')
        beer_mover_category = generic.category(2, 'Moving Beer')
        floor_stocking_category = generic.category(3, 'Floor Stocking')
        wine_work_category = generic.category(4, 'Wine Work')
        shipment_receiving_category = generic.category(5, 'Receive Shipment')
        management_category = generic.category(6, 'Manage Plebs')

        #Preferences 
        #region 
        like_cashier = generic.preference(cashier_category, 1)
        dislike_cashier = generic.preference(cashier_category, -1)

        like_beer_mover = generic.preference(beer_mover_category, 1)
        dislike_beer_mover = generic.preference(beer_mover_category, -1)
        cannot_work_beer_mover = generic.preference(beer_mover_category, 0, False)

        like_floor_stocking = generic.preference(floor_stocking_category, 1)
        dislike_floor_stocking = generic.preference(floor_stocking_category, -1)

        like_wine_work = generic.preference(wine_work_category, 1)
        dislike_wine_work = generic.preference(wine_work_category, -1)

        like_shipment_receiving = generic.preference(shipment_receiving_category, 1)
        dislike_shipment_receiving = generic.preference(shipment_receiving_category, -1)
        #endregion

        #Sunday - 21 hours
        manager_sunday = generic.atask(manager_group, location, management_category, DurationGetter.sunday(11, 18), 'Manage Employees', 1)                      # 
        stock_sunday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.sunday(11, 18), 'FLoor Help', 2)                         # 2
                                                                                                                                                                
        # Monday - 40 hours                                                                                                                                     
        morning_manager_monday = generic.atask(manager_group, location, management_category, DurationGetter.monday(8, 15), 'Manage Employees', 1)               # 
        afternoon_manager_monday = generic.atask(manager_group, location, management_category, DurationGetter.monday(15, 22), 'Manage Employees', 1)            # 
        cashier_monday = generic.atask(cashier_group, location, cashier_category, DurationGetter.monday(15, 22), 'Cashier', 1)                                  # 1
        afternoon_help_monday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.monday(15, 20), 'Floor Help', 1)                # 1
        closer_monday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.monday(15, 22), 'Floor Help', 1)                        # 1
        beer_mover_monday = generic.atask(employee_group, location, beer_mover_category, DurationGetter.monday(15, 22), 'Move beer / Floor Help', 1)            # 1
                                                                                                                                                                
        #Tuesday - 40 hours                                                                                                                                     
        morning_manager_tuesday = generic.atask(manager_group, location, management_category, DurationGetter.tuesday(8, 15), 'Manage Employees', 1)             # 
        afternoon_manager_tuesday = generic.atask(manager_group, location, management_category, DurationGetter.tuesday(15, 22), 'Manage Employees', 1)          # 
        cashier_tuesday = generic.atask(cashier_group, location, cashier_category, DurationGetter.tuesday(15, 22), 'Cashier', 1)                                # 1
        afternoon_help_tuesday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.tuesday(15, 20), 'Floor Help', 1)              # 1
        closer_tuesday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.tuesday(15, 22), 'Floor Help', 1)                      # 1
        beer_mover_tuesday = generic.atask(employee_group, location, beer_mover_category, DurationGetter.tuesday(15, 22), 'Move beer / Floor Help', 1)          # 1
                                                                                                                                                                
        #Wednesday - 40 hours                                                                                                                                   
        morning_manager_wednesday = generic.atask(manager_group, location, management_category, DurationGetter.wednesday(8, 15), 'Manage Employees', 1)         # 
        afternoon_manager_wednesday = generic.atask(manager_group, location, management_category, DurationGetter.wednesday(15, 22), 'Manage Employees', 1)      # 
        cashier_wednesday = generic.atask(cashier_group, location, cashier_category, DurationGetter.wednesday(15, 22), 'Cashier', 1)                            # 1
        afternoon_help_wednesday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.wednesday(15, 20), 'Floor Help', 1)          # 1
        closer_wednesday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.wednesday(15, 22), 'Floor Help', 1)                  # 1
        beer_mover_wednesday = generic.atask(employee_group, location, beer_mover_category, DurationGetter.wednesday(15, 22), 'Move beer / Floor Help', 1)      # 1

        #Thursday - 49 hours
        morning_manager_thursday = generic.atask(manager_group, location, management_category, DurationGetter.thursday(6, 15), 'Manage Employees', 1)           # 
        receive_shipment_thursday = generic.atask(employee_group, location, shipment_receiving_category, DurationGetter.thursday(6, 9), 'Receive Shipment', 1)  # 1
        afternoon_manager_thursday = generic.atask(manager_group, location, management_category, DurationGetter.thursday(15, 22), 'Manage Employees', 1)        # 
        cashier_thursday = generic.atask(cashier_group, location, cashier_category, DurationGetter.thursday(15, 22), 'Cashier', 1)                              # 1
        afternoon_help_thursday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.thursday(15, 20), 'Floor Help', 1)            # 1
        closer_thursday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.thursday(15, 22), 'Floor Help', 1)                    # 1
        beer_mover_thursday = generic.atask(employee_group, location, beer_mover_category, DurationGetter.thursday(15, 22), 'Move beer / Floor Help', 1)        # 1
        wine_work_thursday = generic.atask(employee_group, location, wine_work_category, DurationGetter.thursday(15, 20), 'Stock Wine', 1)                      # 1

        #Friday - 68 hours
        morning_manager_friday = generic.atask(manager_group, location, management_category, DurationGetter.friday(8, 15), 'Manage Employees', 1)               # 
        afternoon_manager_friday = generic.atask(manager_group, location, management_category, DurationGetter.friday(15, 22), 'Manage Employees', 1)            # 
        cashier_friday = generic.atask(cashier_group, location, cashier_category, DurationGetter.friday(15, 22), 'Cashier', 2)                                  # 1
        afternoon_help_friday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.friday(15, 20), 'Floor Help', 1)                # 1
        midday_friday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.friday(10, 17), 'Floor Help', 1)                        # 1
        closer_friday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.friday(15, 22), 'Floor Help', 3)                        # 3
        beer_mover_friday = generic.atask(employee_group, location, beer_mover_category, DurationGetter.friday(15, 22), 'Move beer / Floor Help', 1)            # 1

        #Saturday - 61 hours
        morning_manager_saturday = generic.atask(manager_group, location, management_category, DurationGetter.saturday(8, 15), 'Manage Employees', 1)           # 
        afternoon_manager_saturday = generic.atask(manager_group, location, management_category, DurationGetter.saturday(15, 22), 'Manage Employees', 1)        # 
        cashier_saturday = generic.atask(cashier_group, location, cashier_category, DurationGetter.saturday(15, 22), 'Cashier', 2)                              # 1
        afternoon_help_saturday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.saturday(15, 20), 'Floor Help', 1)            # 1
        midday_saturday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.saturday(10, 17), 'Floor Help', 1)                    # 1
        closer_saturday = generic.atask(employee_group, location, floor_stocking_category, DurationGetter.saturday(15, 22), 'Floor Help', 2)                    # 2
        beer_mover_saturday = generic.atask(employee_group, location, beer_mover_category, DurationGetter.saturday(15, 22), 'Move beer / Floor Help', 1)        # 1

        # Total hours - 320

        morning_manager_tasks = [
            morning_manager_monday,
            morning_manager_tuesday,
            morning_manager_thursday,
            morning_manager_friday,
            morning_manager_saturday,
            ]

        afternoon_manager_tasks = [
            manager_sunday,
            afternoon_manager_monday,
            afternoon_manager_tuesday, 
            afternoon_manager_wednesday,
            afternoon_manager_thursday,
            ]

        misc_manager_tasks = [
            morning_manager_wednesday,
            afternoon_manager_friday, 
            afternoon_manager_saturday,
            ]

        preferences = []
        groups = [manager_group, employee_group, cashier_group]
        availability = [
            AvailabilityGetter.sunday(6,22),
            AvailabilityGetter.monday(6, 22),
            AvailabilityGetter.tuesday(6,22),
            AvailabilityGetter.wednesday(6,22),
            AvailabilityGetter.thursday(6,22),
            AvailabilityGetter.friday(6,22),
            AvailabilityGetter.saturday(6,22),
            ]

        staff_dan = generic.astaff_member('Dan', 30, 40, 50, 10, availability, preferences, groups)

        preferences = []
        groups = [manager_group, employee_group, cashier_group]
        availability = [
            AvailabilityGetter.sunday(6,22),
            AvailabilityGetter.monday(6, 22),
            AvailabilityGetter.tuesday(6,22),
            AvailabilityGetter.wednesday(6,22),
            AvailabilityGetter.thursday(6,22),
            AvailabilityGetter.friday(6,22),
            AvailabilityGetter.saturday(6,22),
            ]

        staff_chris = generic.astaff_member('Chris', 30, 35, 44, 10, availability, preferences, groups)

        preferences = []
        groups = [manager_group, employee_group, cashier_group]
        availability = [
            AvailabilityGetter.sunday(6, 22),
            AvailabilityGetter.monday(6, 22),
            AvailabilityGetter.tuesday(6, 22),
            AvailabilityGetter.wednesday(6, 22),
            AvailabilityGetter.thursday(6, 22),
            AvailabilityGetter.friday(6, 22),
            AvailabilityGetter.saturday(6, 22),
            ]

        staff_brian = generic.astaff_member('Brian', 30, 35, 44, 10, availability, preferences, groups)

        preferences = [like_shipment_receiving, like_wine_work, dislike_beer_mover, like_floor_stocking, dislike_cashier]
        groups = [employee_group, cashier_group]
        availability = [
            AvailabilityGetter.sunday(6, 22),
            AvailabilityGetter.monday(15, 22),
            AvailabilityGetter.tuesday(15, 22),
            AvailabilityGetter.thursday(6, 9),
            AvailabilityGetter.thursday(15, 22),
            AvailabilityGetter.friday(15, 22),
            AvailabilityGetter.saturday(6, 22),
            ]

        staff_wencel = generic.astaff_member('Wencel', 20, 24, 36, 10, availability, preferences, groups)

        preferences = [dislike_beer_mover, like_floor_stocking, dislike_cashier]
        groups = [employee_group, cashier_group]
        availability = [
            AvailabilityGetter.sunday(6, 22),
            AvailabilityGetter.saturday(6, 22),
            ]

        staff_shawn = generic.astaff_member('Shawn', 20, 20, 24, 10, availability, preferences, groups)

        preferences = [like_floor_stocking, dislike_wine_work, dislike_shipment_receiving, like_beer_mover]
        groups = [employee_group]
        availability = [
            AvailabilityGetter.sunday(6, 22),
            AvailabilityGetter.monday(15, 22),
            AvailabilityGetter.tuesday(15, 22),
            AvailabilityGetter.wednesday(15, 22),
            AvailabilityGetter.thursday(15, 22),
            AvailabilityGetter.friday(15, 22),
            AvailabilityGetter.saturday(6, 22),
            ]

        staff_adam = generic.astaff_member('Adam', 20, 24, 36, 10, availability, preferences, groups)

        preferences = [like_beer_mover, dislike_cashier, like_floor_stocking, dislike_wine_work, dislike_shipment_receiving]
        groups = [employee_group, cashier_group, manager_group]
        availability = [
            AvailabilityGetter.sunday(6, 22),
            AvailabilityGetter.monday(6, 22),
            AvailabilityGetter.tuesday(6, 22),
            AvailabilityGetter.wednesday(6, 22),
            AvailabilityGetter.thursday(6, 22),
            AvailabilityGetter.friday(6, 22),
            AvailabilityGetter.saturday(6, 22),
            ]

        staff_keith = generic.astaff_member('Keith', 20, 36, 44, 10, availability, preferences, groups)

        preferences = [cannot_work_beer_mover, like_cashier]
        groups = [cashier_group]
        availability = [
            AvailabilityGetter.monday(15, 22),
            AvailabilityGetter.tuesday(15, 22),
            AvailabilityGetter.wednesday(15, 22),
            AvailabilityGetter.thursday(15, 22),
            AvailabilityGetter.friday(15, 22),
            AvailabilityGetter.saturday(15, 22),
            ]

        staff_lenny = generic.astaff_member('Lenny', 20, 40, 44, 10, availability, preferences, groups)

        preferences = [cannot_work_beer_mover, like_cashier]
        groups = [cashier_group]
        availability = [
            AvailabilityGetter.monday(15, 22),
            AvailabilityGetter.tuesday(15, 22),
            AvailabilityGetter.wednesday(15, 22),
            AvailabilityGetter.thursday(15, 22),
            AvailabilityGetter.friday(15, 22),
            AvailabilityGetter.saturday(15, 22),
            ]

        staff_ = generic.astaff_member('Venus', 20, 30, 40, 10, availability, preferences, groups)

        preferences = [dislike_cashier, like_beer_mover, like_floor_stocking, dislike_wine_work, dislike_shipment_receiving]
        groups = [employee_group]
        availability = [
            AvailabilityGetter.sunday(6, 22),
            AvailabilityGetter.monday(6, 22),
            AvailabilityGetter.tuesday(6, 22),
            AvailabilityGetter.wednesday(6, 22),
            AvailabilityGetter.thursday(6, 22),
            AvailabilityGetter.friday(6, 22),
            AvailabilityGetter.saturday(6, 22),
            ]

        staff_ab = generic.astaff_member('AB', 30, 36, 44, 10, availability, preferences, groups)

        preferences = [like_cashier, dislike_wine_work, dislike_shipment_receiving, ]
        groups = [employee_group, cashier_group]
        availability = [
            AvailabilityGetter.sunday(6, 22),
            AvailabilityGetter.monday(6, 22),
            AvailabilityGetter.tuesday(6, 22),
            AvailabilityGetter.wednesday(6, 22),
            AvailabilityGetter.thursday(6, 22),
            AvailabilityGetter.friday(6, 22),
            AvailabilityGetter.saturday(6, 22),
            ]

        staff_jimbo = generic.astaff_member('Jimbo', 30, 36, 44, 10, availability, preferences, groups)

        all_staff = StaffMemberList(generic.created_staff_members)
        print(all_staff.total_minimum_hours())
        print(all_staff.total_target_hours())
        print(all_staff.total_maximum_hours())

        task_hours = 0
        for task in generic.created_tasks:
            addition = task.required_number_of_employees * task.get_length_in_hours()
            task_hours = task_hours + addition

        print(task_hours)

        morning_manager_role = generic.role(morning_manager_tasks, 1, 'Manage Employees - Morning')
        staff_dan.assign_role(morning_manager_role, True)

        afternoon_manager_role = generic.role(afternoon_manager_tasks, 1, 'Manage Employees - Afternon')
        staff_chris.assign_role(afternoon_manager_role, True)

        misc_manager_role = generic.role(misc_manager_tasks, 1, 'Manage Employees - Misc')

        self.assertFalse(morning_manager_role.needs_staff(all_staff))
        self.assertFalse(afternoon_manager_role.needs_staff(all_staff))

        all_roles = [
            morning_manager_role,
            afternoon_manager_role,
            misc_manager_role,
            ]

        scheduler = ScheduleGenerator(all_staff, all_roles, generic.created_tasks)
        scheduler_settings1 = SchedulerSettings(True, 40, True, False)
        scheduler.schedule(scheduler_settings1, generic.created_tasks, all_staff, all_roles)



    # Further test methods used to generate the graphs in the report
    def run_find_how_long_it_takes_to_find_best(self, all_roles, all_staff, generic, scheduler, scheduler_settings):
        for i in range(1000):
            scheduler.shuffle_then_schedule(scheduler_settings, generic.created_tasks, all_staff, all_roles)
            f = open('text_output.txt', 'a+')
            f.write(str(scheduler.best_ittr) + ',' + str(scheduler.best_h) + ',\n')
            f.close()

    def run_find_3(self, all_roles, all_staff, generic, scheduler, scheduler_settings):
        for i in range(1000):
            scheduler.run_till_3(scheduler_settings, generic.created_tasks, all_staff, all_roles)
            f = open('text_3.txt', 'a+')
            if scheduler.found_3 != -1:
                f.write(str(i) + ',' + str(scheduler.found_3) + ',\n')
            f.close()

    def run_find_277(self, all_roles, all_staff, generic, scheduler, scheduler_settings):
        for i in range(1000):
            scheduler.run_till_277(scheduler_settings, generic.created_tasks, all_staff, all_roles)
            f = open('text_277.txt', 'a+')
            if scheduler.found_277 != -1:
                f.write(str(i) + ',' + str(scheduler.found_277) + ',\n')
            f.close()

    def run_find_272(self, all_roles, all_staff, generic, scheduler, scheduler_settings):
        for i in range(1000):
            scheduler.run_till_272(scheduler_settings, generic.created_tasks, all_staff, all_roles)
            f = open('text_272.txt', 'a+')
            if scheduler.found_272 != -1:
                f.write(str(i) + ',' + str(scheduler.found_272) + ',\n')
            f.close()

    def run_find_281(self, all_roles, all_staff, generic, scheduler, scheduler_settings):
        for i in range(1000):
            scheduler.run_till_281(scheduler_settings, generic.created_tasks, all_staff, all_roles)
            f = open('text_281.txt', 'a+')
            if scheduler.found_281 != -1:
                f.write(str(i) + ',' + str(scheduler.found_281) + ',\n')
            f.close()

    def run_print_h(self, all_roles, all_staff, generic, scheduler, scheduler_settings):
        for i in range(1000):
            h = scheduler.run(scheduler_settings, generic.created_tasks, all_staff, all_roles)
            f = open('general_h.txt', 'a+')
            f.write(str(i) + ',' + str(h) + ',\n')
            f.close()

    def output_schedule_as_csvs(self, all_staff, path):
        for s in all_staff:
            f = open(path + s.name + '.csv', 'a+')
            f.write('Like:,\n')
            for p in s.get_preferences_of(1):
                f.write(p.category.name + ', ')
            f.write('\nDisike:,\n')
            for p in s.get_preferences_of(-1):
                f.write(p.category.name + ', ')
        
            f.write('\n\n')
            f.write('Happiness,' + str(s.get_happiness()))
            f.write('\nHours This Cycle,' + str(s.get_total_hours_working()))
            f.write('\nMin Hours, ' + str(s.minimum_hours_per_week))
            f.write('\nTarget Hours, ' + str(s.target_hours_per_week))
            f.write('\nMax Hours, ' + str(s.maximum_hours_per_week))
            f.write('\nMax Hours (day), ' + str(s.maximum_hours_per_day))
            
        
            f.write('\n\nTasks:,\n')
            f.write('Name, Time, Category,\n')
            for t in s.get_tasks():
                f.write(t.name + ', ' + str(t.duration) + ', ' + str(t.category.name) + ',\n')
        
        
            f.close()
if __name__ == '__main__':
    unittest.main()
