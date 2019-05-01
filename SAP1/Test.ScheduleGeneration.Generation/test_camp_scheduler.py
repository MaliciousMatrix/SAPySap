import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration')
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
from ScheduleGenerator import ScheduleGenerator
from scheduler_settings import SchedulerSettings
from staff_member_list import StaffMemberList

class TestCampScheduler(unittest.TestCase):

    def test_scheduling(self):

        generic = CommonTestFunctions()
        
        # Locations
        #region 

        # program areas 
        craftshop_location = generic.location(2, 'Craftshop')
        corral_location = generic.location(3, 'Corral')
        boat_house_location = generic.location(4, 'Boat House')
        fishing_location = generic.location(5, 'Fishing')
        bikes_location = generic.location(6, 'Bikes')
        beach_location = generic.location(7, 'Beach')
        target_sports_location = generic.location(8, 'Target Sports')
        nature_location = generic.location(9, 'Nature')
        kannacks_location = generic.location(10, 'Kannacks')
        maintenance_location = generic.location(11, 'Maintenance')
        kitchen_location = generic.location(12, 'Kitchen')
        cit_location = generic.location(13, 'With CITS')
        lit_location = generic.location(14, 'With LITS')
        homestead_location = generic.location(15, 'Homestead')
        athletic_field_location = generic.location(16, 'Athletic Field')
        day_camper_location = generic.location(17, 'With Day Campers')
        pathfinder_location = generic.location(18, 'With Pathfinders')
        trading_post_location = generic.location(19, 'Trading Post')
        floater_location = generic.location(20, 'Floating')
        outpost_location = generic.location(21, 'Outpost')

        # cabins
        duluth_location = generic.location(101, 'Duluth')
        frontenac_location = generic.location(102, 'Fontenac')
        jolliet_location = generic.location(103, 'Jolliet')
        hennepin_location = generic.location(104, 'Hennepin')
        groseilliers_location = generic.location(105, 'Groseilliers')
        le_sueur_location = generic.location(206, 'Le Sueur')
        la_verendrye_location = generic.location(207, 'La Verendrye')
        marquette_location = generic.location(208, 'Marquette')
        nicollet_location = generic.location(209, 'Nicollet')
        ramsey_location = generic.location(210, 'Ramsey')
        ripley_location = generic.location(211, 'Ripley')
        radisson_location = generic.location(212, 'Radisson')
        schoolcraft_location = generic.location(213, 'Schoolcraft')
        lower_cabin_location = generic.location(214, 'Lower Cabin')
        willy_location = generic.location(215, 'Willy')
        yaqua_location = generic.location(216, 'Yaqua')

        #misc
        flag_pole = generic.location(217, 'Flag Pole')
        dining_hall = generic.location(218, 'Dining Hall')
        around_camp = generic.location(219, 'Around Camp')
        store = generic.location(220, 'Store')
        #endregion 

        #Groups
        #region

        # Counselors 
        duluth_counselor = generic.group(1, 'Duluth Counselor')
        frontenac_counselor = generic.group(2, 'Frontenac Counselor')
        jolliet_counselor = generic.group(3, 'Jolliet Counselor')
        hennepin_counselor = generic.group(4, 'Hennepin Counselor')
        grossielliers_counselor = generic.group(5, 'Grossielliers Counselor')
        le_sueur_counselor = generic.group(6, 'Le Sueur Counselor')
        la_verendrye_counselor = generic.group(7, 'La Verendrye Counselor')
        marquette_counselor = generic.group(8, 'Marquette Counselor')
        nicollet_counselor = generic.group(9, 'Nicollet Counselor')
        ramsey_counselor = generic.group(10, 'Ramsey Counselor')
        ripley_counselor = generic.group(11, 'Ripley Counselor')
        radisson_counselor = generic.group(12, 'Radisson Counselor')
        schoolcraft_counselor = generic.group(13, 'Schoolcraft Counselor')
        lower_cabin_counselor = generic.group(14, 'Lower Cabin Counselor')
        willy_counselor = generic.group(15, 'Willy Counselor')
        yaqua_counselor = generic.group(16, 'Yaqua Counselor')
        erie_counselor = generic.group(17, 'Erie Counselor')

        # Program area directors
        corral_director = generic.group(103, 'Corral Director')
        boat_house_director = generic.group(104, 'Boat House Director')
        fishing_director = generic.group(105, 'Fishing Director')
        bikes_director = generic.group(106, 'Bikes Director')
        beach_director = generic.group(107, 'Beach Director')
        target_sports_director = generic.group(108, 'Target Sports Director')
        nature_director = generic.group(109, 'Nature Director')
        kannacks_director = generic.group(110, 'Kannacks Director')
        maintenance_worker = generic.group(111, 'Maintenace Worker')
        kitchen_worker = generic.group(112, 'Kitchen Worker')
        craftshop_director = generic.group(113, 'Craftshop Director')

        #other 
        cit_leader = generic.group(201, 'CIT Leader')
        lit_leader = generic.group(202, 'LIT Leader')
        day_camp_counselor = generic.group(203, 'Day Camp Counselor')
        path_finder_counselor = generic.group(203, 'Path Finder Counselor')

        #Major
        pstaff = generic.group(301, 'P Staff')
        counselor = generic.group(302, 'Counselor')

        # Certified 
        lifegaurd = generic.group(401, 'Lifegaurd')
        wrangler = generic.group(402, 'Wrangler')
        skipper = generic.group(403, 'Skipper')

        #endregion

        #Categories
        #region

        corral_category = generic.category(3, 'Corral')
        boat_house_category = generic.category(4, 'Boat House')
        fishing_category = generic.category(5, 'Fishing')
        bikes_category = generic.category(6, 'Bikes')
        beach_category = generic.category(7, 'Beach')
        target_sports_category = generic.category(8, 'Target Sports')
        nature_category = generic.category(9, 'Nature')
        kannacks_category = generic.category(10, 'Kannacks')
        maintenance_category = generic.category(11, 'Maintenance')
        kitchen_category = generic.category(12, 'Kitchen')
        floater_category = generic.category(20, 'Floater')
        morning_activity = generic.category(100, 'Morning Activity')
        clean_cabin = generic.category(101, 'Clean Cabin')
        afternoon_activity = generic.category(102, 'Afternoon Activity')
        craftshop_category = generic.category(103, 'Craftshop')

        campfire_category = generic.category(201, 'Campfire')
        flag_raising_category = generic.category(202, 'Flag Raising')
        breakfast_grace_category = generic.category(203, 'Breakfast Grace')
        lunch_grace_category = generic.category(204, 'Lunch Grace')
        dinner_grace_category = generic.category(205, 'Dinner Grace')
        flag_lowering_category = generic.category(206, 'Flag Lowering')
        password_category = generic.category(207, 'Password')
        power_up_category = generic.category(208, 'Power Up')
        quiet_cabin_category = generic.category(209, 'Quiet Cabin')
        trading_post_category = generic.category(210, 'Trading Post')

        #endregion 

        # Preferences
        #region 
        like_corral = generic.preference(corral_category, 1)
        dislike_corral = generic.preference(corral_category, -1)
        cannot_work_corral = generic.preference(corral_category, 0, False)

        like_boat_house = generic.preference(boat_house_category, 1)
        dislike_boat_house = generic.preference(boat_house_category, -1)
        cannot_work_boat_house = generic.preference(boat_house_category, 0, False)

        like_craftshop = generic.preference(craftshop_category, 1)
        dislike_craftshop = generic.preference(craftshop_category, -1)
        cannot_work_shop = generic.preference(craftshop_category, 0, False)

        like_fishing = generic.preference(fishing_category, 1)
        dislike_fishing = generic.preference(fishing_category, -1)
        cannot_work_fishing = generic.preference(fishing_category, 0, False)

        like_bikes = generic.preference(bikes_category, 1)
        dislike_bikes = generic.preference(bikes_category, -1)
        cannot_work_bikes = generic.preference(bikes_category, 0, False)

        like_beach = generic.preference(beach_category, 1)
        dislike_beach = generic.preference(beach_category, -1)
        cannot_work_beach = generic.preference(beach_category, 0, False)

        like_target_sports = generic.preference(target_sports_category, 1)
        dislike_target_sports = generic.preference(target_sports_category, -1)
        cannot_work_target_sports = generic.preference(target_sports_category, 0, False)

        like_nature = generic.preference(nature_category, 1)
        dislike_nature = generic.preference(nature_category, -1)
        cannot_work_nature = generic.preference(nature_category, 0, False)

        like_kannacks = generic.preference(kannacks_category, 1)
        dislike_kannacks = generic.preference(kannacks_category, -1)
        cannot_work_kannacks = generic.preference(kannacks_category, 0, False)

        like_maintenance = generic.preference(maintenance_category, 1)
        dislike_maintenance = generic.preference(maintenance_category, -1)
        cannot_work_maintenance = generic.preference(maintenance_category, 0, False)

        like_kitchen = generic.preference(kitchen_category, 1)
        dislike_kitchen = generic.preference(kitchen_category, -1)
        cannot_work_kitchen = generic.preference(kitchen_category, 0, False)

        like_floater = generic.preference(floater_category, 1)
        dislike_floater = generic.preference(floater_category, -1)
        cannot_work_floater = generic.preference(floater_category, 0, False)

        like_campfire = generic.preference(campfire_category, 1)
        dislike_campfire = generic.preference(campfire_category, -1)

        like_trading_post = generic.preference(trading_post_category, 1)
        dislike_trading_post = generic.preference(trading_post_category, -1)

        like_power_up = generic.preference(power_up_category, 1)
        dislike_power_up = generic.preference(power_up_category, -1)

        like_quiet_cabin = generic.preference(quiet_cabin_category, 1)
        dislike_quiet_cabin = generic.preference(quiet_cabin_category, -1)

        #endregion

        # Availabilities
        #region
        sunday_availability = generic.camp_availability(1, 12, 23, 45, 0)
        monday_availability = generic.camp_availability(2, 7, 23, 45, 0)
        tuesday_availability = generic.camp_availability(3, 7, 23, 45, 0)
        wednesday_availability = generic.camp_availability(4, 7, 23, 45, 0)
        thursday_availability = generic.camp_availability(5, 7, 23, 45, 0)
        friday_availability = generic.camp_availability(6, 7, 23, 45, 0)
        saturday_availability = generic.camp_availability(7, 7, 12, 0, 0)

        availability = [
            sunday_availability,
            monday_availability,
            tuesday_availability,
            wednesday_availability,
            thursday_availability,
            friday_availability,
            saturday_availability,
            ]

        #endregion

        #Durations
        #region 

        #Cabin Activities
        cabin_activity_duration_monday_nine_ten = generic.camp_duration(9, 10, 2)
        cabin_activity_duration_monday_ten_eleven = generic.camp_duration(10, 11, 2)
        cabin_activity_duration_monday_eleven_twelve = generic.camp_duration(11, 12, 2)

        cabin_activity_duration_tuesday_nine_ten = generic.camp_duration(9, 10, 3)
        cabin_activity_duration_tuesday_ten_eleven = generic.camp_duration(10, 11, 3)
        cabin_activity_duration_tuesday_eleven_twelve = generic.camp_duration(11, 12, 3)

        cabin_activity_duration_wednesday_nine_ten = generic.camp_duration(9, 10, 4)
        cabin_activity_duration_wednesday_ten_eleven = generic.camp_duration(10, 11, 4)
        cabin_activity_duration_wednesday_eleven_twelve = generic.camp_duration(11, 12, 4)

        cabin_activity_duration_thursday_nine_ten = generic.camp_duration(9, 10, 5)
        cabin_activity_duration_thursday_ten_eleven = generic.camp_duration(10, 11, 5)
        cabin_activity_duration_thursday_eleven_twelve = generic.camp_duration(11, 12, 5)

        cabin_activity_duration_friday_nine_ten = generic.camp_duration(9, 10, 6)
        cabin_activity_duration_friday_ten_eleven = generic.camp_duration(10, 11, 6)
        cabin_activity_duration_friday_eleven_twelve = generic.camp_duration(11, 12, 6)

        monday_overnight_1_duration = generic.camp_duration(12, 23, 2)
        monday_overnight_2_duration = generic.camp_duration(7, 12, 3, 45)

        tuesday_overnight_1_duration = generic.camp_duration(12, 23, 3)
        tuesday_overnight_2_duration = generic.camp_duration(7, 12, 4, 45)

        wednesday_overnight_1_duration = generic.camp_duration(12, 23, 3)
        wednesday_overnight_2_duration = generic.camp_duration(7, 12, 4, 45)

        thursday_overnight_1_duration = generic.camp_duration(12, 23, 4)
        thursday_overnight_2_duration = generic.camp_duration(7, 12, 5, 45)

        cabin_activity_duration_monday_nine_twelve = generic.camp_duration(9, 12, 2)
        cabin_activity_duration_tuesday_nine_twelve = generic.camp_duration(9, 12, 3)
        cabin_activity_duration_wednesday_nine_twelve = generic.camp_duration(9, 12, 4)
        cabin_activity_duration_thursday_nine_twelve = generic.camp_duration(9, 12, 5)
        cabin_activity_duration_friday_nine_twelve = generic.camp_duration(9, 12, 6)

        #Afternoon activities
        duration_monday_first = generic.camp_duration(14, 15, 2, 0, 30)
        duration_tuesday_first = generic.camp_duration(14, 15, 3, 0, 30)
        duration_wednesday_first = generic.camp_duration(14, 15, 4, 30, 30)
        duration_thursday_first = generic.camp_duration(14, 15, 5, 0, 30)
        duration_friday_first = generic.camp_duration(14, 15, 6, 0, 30)

        duration_monday_second = generic.camp_duration(16, 17, 2, 0, 30)
        duration_tuesday_second = generic.camp_duration(16, 17, 3, 0, 30)
        duration_wednesday_second = generic.camp_duration(16, 17, 4, 0, 30)
        duration_thursday_second = generic.camp_duration(16, 17, 5, 0, 30)
        duration_friday_second = generic.camp_duration(16, 17, 6, 0, 30)

        duration_monday_mid = generic.camp_duration(15, 16, 2, 30)
        duration_tuesday_mid = generic.camp_duration(15, 16, 3, 30)
        duration_wednesday_mid = generic.camp_duration(15, 16, 4, 30)
        duration_thursday_mid = generic.camp_duration(15, 16, 5, 30)

        duration_sunday_night = generic.camp_duration(20, 21, 1)
        duration_monday_night = generic.camp_duration(20, 21, 2)
        duration_tuesday_night = generic.camp_duration(20, 21, 3)
        duration_wednesday_night = generic.camp_duration(20, 21, 4)
        duration_thursday_night = generic.camp_duration(20, 21, 5)
        duration_friday_night = generic.camp_duration(20, 21, 6)

        duration_monday_morning = generic.camp_duration(7, 8, 2, 45)
        duration_tuesday_morning = generic.camp_duration(7, 8, 3, 45)
        duration_wednesday_morning = generic.camp_duration(7, 8, 4, 45)
        duration_thursday_morning = generic.camp_duration(7, 8, 5, 45)
        duration_friday_morning = generic.camp_duration(7, 8, 6, 45)
        duration_saturday_morning = generic.camp_duration(7, 8, 7, 45)

        duration_sunday_evening = generic.camp_duration(18, 18, 1, 0, 15)
        duration_monday_evening = generic.camp_duration(18, 18, 2, 0, 15)
        duration_tuesday_evening = generic.camp_duration(18, 18, 3, 0, 15)
        duration_wednesday_evening = generic.camp_duration(18, 18, 4, 0, 15)
        duration_thursday_evening = generic.camp_duration(18, 18, 5, 0, 15)
        duration_friday_evening = generic.camp_duration(18, 18, 6, 0, 15)

        duration_monday_lunch = generic.camp_duration(12, 13, 2)
        duration_tuesday_lunch = generic.camp_duration(12, 13, 3)
        duration_wednesday_lunch = generic.camp_duration(12, 13, 4)
        duration_thursday_lunch = generic.camp_duration(12, 13, 5)
        duration_friday_lunch = generic.camp_duration(12, 13, 6)

        #endregion

        #Tasks
        #region

        #Cabin Morning Tasks
        all_tasks = []
        grossielliers_cabin_tasks = [
            generic.task(grossielliers_counselor, kannacks_location, morning_activity, cabin_activity_duration_monday_nine_ten, 1, 'Kannacks', 2),
            generic.task(grossielliers_counselor, homestead_location, morning_activity, cabin_activity_duration_monday_ten_eleven, 2, 'Homestead Hike', 2),
            generic.task(grossielliers_counselor, athletic_field_location, morning_activity, cabin_activity_duration_monday_eleven_twelve, 3, 'AF', 2),
        
            generic.task(grossielliers_counselor, outpost_location, morning_activity, monday_overnight_1_duration, 4, 'Overnight', 2),
            generic.task(grossielliers_counselor, outpost_location, morning_activity, monday_overnight_2_duration, 5, 'Overnight', 2),

            generic.task(grossielliers_counselor, boat_house_location, morning_activity, cabin_activity_duration_wednesday_nine_ten, 6, 'Boat House', 2),
            generic.task(grossielliers_counselor, target_sports_location, morning_activity, cabin_activity_duration_wednesday_ten_eleven, 7, 'Rifles', 2),
            generic.task(grossielliers_counselor, groseilliers_location, morning_activity, cabin_activity_duration_wednesday_eleven_twelve, 8, 'Skit', 2),

            generic.task(grossielliers_counselor, fishing_location, morning_activity, cabin_activity_duration_thursday_nine_ten, 9, 'Fishing', 2),
            generic.task(grossielliers_counselor, corral_location, morning_activity, cabin_activity_duration_thursday_ten_eleven, 10, 'Corral', 2),
            generic.task(grossielliers_counselor, craftshop_location, morning_activity, cabin_activity_duration_thursday_eleven_twelve, 11, 'Craftshop', 2),

            generic.task(grossielliers_counselor, beach_location, morning_activity, cabin_activity_duration_friday_nine_ten, 12, 'Beach', 2),
            generic.task(grossielliers_counselor, target_sports_location, morning_activity, cabin_activity_duration_friday_ten_eleven, 13, 'Archery', 2),
            generic.task(grossielliers_counselor, nature_location, morning_activity, cabin_activity_duration_friday_eleven_twelve, 14, 'Nature', 2),

            generic.task(grossielliers_counselor, groseilliers_location, clean_cabin, duration_friday_second, 194, 'Clean Cabin', 2),
        ]

        all_tasks.extend(grossielliers_cabin_tasks)

        frontenac_cabin_tasks = [
            generic.task(frontenac_counselor, beach_location, morning_activity, cabin_activity_duration_monday_nine_ten, 15, 'Beach', 2),
            generic.task(frontenac_counselor, target_sports_location, morning_activity, cabin_activity_duration_monday_ten_eleven, 16, 'Archery', 2),
            generic.task(frontenac_counselor, nature_location, morning_activity, cabin_activity_duration_monday_eleven_twelve, 17, 'Nature', 2),
            
            generic.task(frontenac_counselor, kannacks_location, morning_activity, cabin_activity_duration_tuesday_nine_ten, 18, 'Kannacks', 2),
            generic.task(frontenac_counselor, homestead_location, morning_activity, cabin_activity_duration_tuesday_ten_eleven, 19, 'Homestead Hike', 2),
            generic.task(frontenac_counselor, athletic_field_location, morning_activity, cabin_activity_duration_tuesday_eleven_twelve, 20, 'AF', 2),
            
            generic.task(frontenac_counselor, outpost_location, morning_activity, tuesday_overnight_1_duration, 21, 'Overnight', 2),
            generic.task(frontenac_counselor, outpost_location, morning_activity, tuesday_overnight_2_duration, 22, 'Overnight', 2),

            generic.task(frontenac_counselor, boat_house_location, morning_activity, cabin_activity_duration_thursday_nine_ten, 23, 'Boat House', 2),
            generic.task(frontenac_counselor, target_sports_location, morning_activity, cabin_activity_duration_thursday_ten_eleven, 24, 'Rifles', 2),
            generic.task(frontenac_counselor, frontenac_location, morning_activity, cabin_activity_duration_thursday_eleven_twelve, 25, 'Skit', 2),
            
            generic.task(frontenac_counselor, fishing_location, morning_activity, cabin_activity_duration_friday_nine_ten, 26, 'Fishing', 2),
            generic.task(frontenac_counselor, corral_location, morning_activity, cabin_activity_duration_friday_ten_eleven, 27, 'Corral', 2),
            generic.task(frontenac_counselor, craftshop_location, morning_activity, cabin_activity_duration_friday_eleven_twelve, 28, 'Craftshop', 2),

            generic.task(frontenac_counselor, frontenac_location, clean_cabin, duration_friday_second, 195, 'Clean Cabin', 2),
            ]
        all_tasks.extend(frontenac_cabin_tasks)

        duluth_cabin_tasks = [
            generic.task(duluth_counselor, fishing_location, morning_activity, cabin_activity_duration_monday_nine_ten, 29, 'Fishing', 2),
            generic.task(duluth_counselor, corral_location, morning_activity, cabin_activity_duration_monday_ten_eleven, 30, 'Corral', 2),
            generic.task(duluth_counselor, craftshop_location, morning_activity, cabin_activity_duration_monday_eleven_twelve, 31, 'Craftshop', 2),
            
            generic.task(duluth_counselor, beach_location, morning_activity, cabin_activity_duration_tuesday_nine_ten, 32, 'Beach', 2),
            generic.task(duluth_counselor, target_sports_location, morning_activity, cabin_activity_duration_tuesday_ten_eleven, 33, 'Archery', 2),
            generic.task(duluth_counselor, nature_location, morning_activity, cabin_activity_duration_tuesday_eleven_twelve, 34, 'Nature', 2),
            
            generic.task(duluth_counselor, kannacks_location, morning_activity, cabin_activity_duration_wednesday_nine_ten, 35, 'Kannacks', 2),
            generic.task(duluth_counselor, homestead_location, morning_activity, cabin_activity_duration_wednesday_ten_eleven, 36, 'HH', 2),
            generic.task(duluth_counselor, athletic_field_location, morning_activity, cabin_activity_duration_thursday_eleven_twelve, 37, 'AF', 2),
            
            generic.task(duluth_counselor, outpost_location, morning_activity, wednesday_overnight_1_duration, 38, 'Overnight', 2),
            generic.task(duluth_counselor, outpost_location, morning_activity, wednesday_overnight_2_duration, 39, 'Overnight', 2),
            
            generic.task(duluth_counselor, boat_house_location, morning_activity, cabin_activity_duration_friday_nine_ten, 40, 'Boat House', 2),
            generic.task(duluth_counselor, target_sports_location, morning_activity, cabin_activity_duration_friday_ten_eleven, 41, 'Rifles', 2),
            generic.task(duluth_counselor, duluth_location, morning_activity, cabin_activity_duration_friday_eleven_twelve, 42, 'Skit', 2),

            generic.task(duluth_counselor, duluth_location, clean_cabin, duration_friday_second, 196, 'Clean Cabin', 2),
            ]

        all_tasks.extend(duluth_cabin_tasks)

        jolliet_cabin_tasks = [
            generic.task(jolliet_counselor, boat_house_location, morning_activity, cabin_activity_duration_monday_nine_ten, 43, 'Boat House', 2),
            generic.task(jolliet_counselor, target_sports_location, morning_activity, cabin_activity_duration_monday_ten_eleven, 44, 'Rifles', 2),
            generic.task(jolliet_counselor, jolliet_location, morning_activity, cabin_activity_duration_monday_eleven_twelve, 45, 'Skit', 2),
            
            generic.task(jolliet_counselor, fishing_location, morning_activity, cabin_activity_duration_tuesday_nine_ten, 46, 'Fishing', 2),
            generic.task(jolliet_counselor, corral_location, morning_activity, cabin_activity_duration_tuesday_ten_eleven, 47, 'Corral', 2),
            generic.task(jolliet_counselor, craftshop_location, morning_activity, cabin_activity_duration_tuesday_eleven_twelve, 48, 'Craftshop', 2),
            
            generic.task(jolliet_counselor, beach_location, morning_activity, cabin_activity_duration_wednesday_nine_ten, 49, 'Beach', 2),
            generic.task(jolliet_counselor, target_sports_location, morning_activity, cabin_activity_duration_wednesday_ten_eleven, 50, 'Archery', 2),
            generic.task(jolliet_counselor, nature_location, morning_activity, cabin_activity_duration_wednesday_eleven_twelve, 51, 'Nature', 2),
            
            generic.task(jolliet_counselor, kannacks_location, morning_activity, cabin_activity_duration_thursday_nine_ten, 52, 'Kannacks', 2),
            generic.task(jolliet_counselor, homestead_location, morning_activity, cabin_activity_duration_thursday_ten_eleven, 53, 'HH', 2),
            generic.task(jolliet_counselor, athletic_field_location, morning_activity, cabin_activity_duration_thursday_eleven_twelve, 54, 'AF', 2),
            
            generic.task(jolliet_counselor, outpost_location, morning_activity, thursday_overnight_1_duration, 55, 'Overnight', 2),
            generic.task(jolliet_counselor, outpost_location, morning_activity, thursday_overnight_2_duration, 56, 'Overnight', 2),

            generic.task(jolliet_counselor, jolliet_location, clean_cabin, duration_friday_second, 196, 'Clean Cabin', 2),
            
            ]

        all_tasks.extend(jolliet_cabin_tasks)

        hennepin_cabin_tasks = [
            generic.task(hennepin_counselor, athletic_field_location, morning_activity, cabin_activity_duration_monday_nine_ten, 57, 'AF', 2),
            generic.task(hennepin_counselor, kannacks_location, morning_activity, cabin_activity_duration_monday_ten_eleven, 58, 'Kannacks', 2),
            generic.task(hennepin_counselor, homestead_location, morning_activity, cabin_activity_duration_monday_eleven_twelve, 59, 'HH', 2),
            
            generic.task(hennepin_counselor, outpost_location, morning_activity, monday_overnight_1_duration, 60, 'Overnight', 2),
            generic.task(hennepin_counselor, outpost_location, morning_activity, monday_overnight_2_duration, 61, 'Overnight', 2),
            
            generic.task(hennepin_counselor, hennepin_location, morning_activity, cabin_activity_duration_wednesday_nine_ten, 62, 'Skit', 2),
            generic.task(hennepin_counselor, boat_house_location, morning_activity, cabin_activity_duration_wednesday_ten_eleven, 63, 'Boat House', 2),
            generic.task(hennepin_counselor, target_sports_location, morning_activity, cabin_activity_duration_wednesday_eleven_twelve, 64, 'Rifles', 2),
            
            generic.task(hennepin_counselor, craftshop_location, morning_activity, cabin_activity_duration_thursday_nine_ten, 65, 'Craftshop', 2),
            generic.task(hennepin_counselor, fishing_location, morning_activity, cabin_activity_duration_thursday_ten_eleven, 66, 'Fishing', 2),
            generic.task(hennepin_counselor, corral_location, morning_activity, cabin_activity_duration_thursday_eleven_twelve, 67, 'Corral', 2),
            
            generic.task(hennepin_counselor, nature_location, morning_activity, cabin_activity_duration_friday_nine_ten, 68, 'Nature', 2),
            generic.task(hennepin_counselor, beach_location, morning_activity, cabin_activity_duration_friday_ten_eleven, 69, 'Beach', 2),
            generic.task(hennepin_counselor, target_sports_location, morning_activity, cabin_activity_duration_friday_eleven_twelve, 70, 'Archery', 2),

            generic.task(hennepin_counselor, hennepin_location, clean_cabin, duration_friday_second, 198, 'Clean Cabin', 2),
            ]

        all_tasks.extend(hennepin_cabin_tasks)

        la_verendrye_cabin_tasks = [
            generic.task(la_verendrye_counselor, nature_location, morning_activity, cabin_activity_duration_monday_nine_ten, 71, 'Nature', 2),
            generic.task(la_verendrye_counselor, beach_location, morning_activity, cabin_activity_duration_monday_ten_eleven, 72, 'Beach', 2),
            generic.task(la_verendrye_counselor, target_sports_location, morning_activity, cabin_activity_duration_monday_eleven_twelve, 73, 'Archery', 2),
            
            generic.task(la_verendrye_counselor, athletic_field_location, morning_activity, cabin_activity_duration_tuesday_nine_ten, 74, 'AF', 2),
            generic.task(la_verendrye_counselor, kannacks_location, morning_activity, cabin_activity_duration_tuesday_ten_eleven, 75, 'Kannacks', 2),
            generic.task(la_verendrye_counselor, homestead_location, morning_activity, cabin_activity_duration_tuesday_eleven_twelve, 76, 'HH', 2),
            
            generic.task(la_verendrye_counselor, outpost_location, morning_activity, tuesday_overnight_1_duration, 77, 'Overnight', 2),
            generic.task(la_verendrye_counselor, outpost_location, morning_activity, tuesday_overnight_2_duration, 78, 'Overnight', 2),
            
            generic.task(la_verendrye_counselor, la_verendrye_location, morning_activity, cabin_activity_duration_thursday_nine_ten, 79, 'Skit', 2),
            generic.task(la_verendrye_counselor, boat_house_location, morning_activity, cabin_activity_duration_thursday_ten_eleven, 80, 'Boat House', 2),
            generic.task(la_verendrye_counselor, target_sports_location, morning_activity, cabin_activity_duration_thursday_eleven_twelve, 81, 'Rifles', 2),
            
            generic.task(la_verendrye_counselor, craftshop_location, morning_activity, cabin_activity_duration_friday_nine_ten, 82, 'Craftshop', 2),
            generic.task(la_verendrye_counselor, fishing_location, morning_activity, cabin_activity_duration_friday_ten_eleven, 83, 'Fishing', 2),
            generic.task(la_verendrye_counselor, corral_location, morning_activity, cabin_activity_duration_friday_eleven_twelve, 84, 'Corral', 2),

            generic.task(la_verendrye_counselor, la_verendrye_location, clean_cabin, duration_friday_second, 199, 'Clean Cabin', 2),
            ]
        all_tasks.extend(la_verendrye_cabin_tasks)

        le_sueur_tasks = [
            generic.task(le_sueur_counselor, craftshop_location, morning_activity, cabin_activity_duration_monday_nine_ten, 85, 'Craftshop', 2),
            generic.task(le_sueur_counselor, fishing_location, morning_activity, cabin_activity_duration_monday_ten_eleven, 86, 'Fishing', 2),
            generic.task(le_sueur_counselor, corral_location, morning_activity, cabin_activity_duration_monday_eleven_twelve, 87, 'Corral', 2),
            
            generic.task(le_sueur_counselor, nature_location, morning_activity, cabin_activity_duration_tuesday_nine_ten, 88, 'Nature', 2),
            generic.task(le_sueur_counselor, beach_location, morning_activity, cabin_activity_duration_thursday_ten_eleven, 89, 'Beach', 2),
            generic.task(le_sueur_counselor, target_sports_location, morning_activity, cabin_activity_duration_thursday_eleven_twelve, 90, 'Archery', 2),
            
            generic.task(le_sueur_counselor, athletic_field_location, morning_activity, cabin_activity_duration_wednesday_nine_ten, 91, 'AF', 2),
            generic.task(le_sueur_counselor, kannacks_location, morning_activity, cabin_activity_duration_wednesday_ten_eleven, 92, 'Kannacks', 2),
            generic.task(le_sueur_counselor, homestead_location, morning_activity, cabin_activity_duration_wednesday_eleven_twelve, 93, 'HH', 2),

            generic.task(le_sueur_counselor, outpost_location, morning_activity, wednesday_overnight_1_duration, 94, 'Overnight', 2),
            generic.task(le_sueur_counselor, outpost_location, morning_activity, wednesday_overnight_2_duration, 95, 'Overnight', 2),
            
            generic.task(le_sueur_counselor, le_sueur_location, morning_activity, cabin_activity_duration_friday_nine_ten, 96, 'Skit', 2),
            generic.task(le_sueur_counselor, boat_house_location, morning_activity, cabin_activity_duration_friday_ten_eleven, 97, 'Boat House', 2),
            generic.task(le_sueur_counselor, target_sports_location, morning_activity, cabin_activity_duration_friday_eleven_twelve, 98, 'Rifles', 2),

            generic.task(le_sueur_counselor, le_sueur_location, clean_cabin, duration_friday_second, 200, 'Clean Cabin', 2),
            ]

        all_tasks.extend(le_sueur_tasks)

        marquette_tasks = [
            generic.task(marquette_counselor, marquette_location, morning_activity, cabin_activity_duration_monday_nine_ten, 99, 'Skit', 2),
            generic.task(marquette_counselor, boat_house_location, morning_activity, cabin_activity_duration_monday_ten_eleven, 100, 'Boat House', 2),
            generic.task(marquette_counselor, target_sports_location, morning_activity, cabin_activity_duration_monday_eleven_twelve, 101, 'Rifles', 2),
            
            generic.task(marquette_counselor, craftshop_location, morning_activity, cabin_activity_duration_tuesday_nine_ten, 102, 'Craftshop', 2),
            generic.task(marquette_counselor, fishing_location, morning_activity, cabin_activity_duration_tuesday_ten_eleven, 103, 'Marquette', 2),
            generic.task(marquette_counselor, corral_location, morning_activity, cabin_activity_duration_tuesday_eleven_twelve, 104, 'Corral', 2),
            
            generic.task(marquette_counselor, nature_location, morning_activity, cabin_activity_duration_wednesday_nine_ten, 105, 'Nature', 2),
            generic.task(marquette_counselor, beach_location, morning_activity, cabin_activity_duration_wednesday_ten_eleven, 106, 'Beach', 2),
            generic.task(marquette_counselor, target_sports_location, morning_activity, cabin_activity_duration_wednesday_eleven_twelve, 107, 'Archery', 2),
            
            generic.task(marquette_counselor, athletic_field_location, morning_activity, cabin_activity_duration_thursday_nine_ten, 108, 'AF', 2),
            generic.task(marquette_counselor, kannacks_location, morning_activity, cabin_activity_duration_thursday_ten_eleven, 109, 'Kannacks', 2),
            generic.task(marquette_counselor, homestead_location, morning_activity, cabin_activity_duration_thursday_eleven_twelve, 110, 'HH', 2),
            
            generic.task(marquette_counselor, outpost_location, morning_activity, thursday_overnight_1_duration, 111, 'Overnight', 2),
            generic.task(marquette_counselor, outpost_location, morning_activity, thursday_overnight_2_duration, 112, 'Overnight', 2),

            generic.task(marquette_counselor, marquette_location, clean_cabin, duration_friday_second, 201, 'Clean Cabin', 2),

            ]
        all_tasks.extend(marquette_tasks)

        nicollet_tasks = [
            generic.task(nicollet_counselor, homestead_location, morning_activity, cabin_activity_duration_monday_nine_ten, 113, 'HH', 2),
            generic.task(nicollet_counselor, athletic_field_location, morning_activity, cabin_activity_duration_monday_ten_eleven, 114, 'AF', 2),
            generic.task(nicollet_counselor, kannacks_location, morning_activity, cabin_activity_duration_monday_eleven_twelve, 115, 'Kannacks', 2),
            
            generic.task(nicollet_counselor, outpost_location, morning_activity, monday_overnight_1_duration, 116, 'Overnight', 2),
            generic.task(nicollet_counselor, outpost_location, morning_activity, monday_overnight_2_duration, 117, 'Overnight', 2),
            
            generic.task(nicollet_counselor, target_sports_location, morning_activity, cabin_activity_duration_wednesday_nine_ten, 118, 'Rifles', 2),
            generic.task(nicollet_counselor, nicollet_location, morning_activity, cabin_activity_duration_wednesday_ten_eleven, 119, 'Skit', 2),
            generic.task(nicollet_counselor, boat_house_location, morning_activity, cabin_activity_duration_wednesday_eleven_twelve, 120, 'Boat House', 2),
            
            generic.task(nicollet_counselor, corral_location, morning_activity, cabin_activity_duration_thursday_nine_ten, 121, 'Corral', 2),
            generic.task(nicollet_counselor, craftshop_location, morning_activity, cabin_activity_duration_thursday_ten_eleven, 122, 'Craftshop', 2),
            generic.task(nicollet_counselor, fishing_location, morning_activity, cabin_activity_duration_thursday_eleven_twelve, 123, 'Fishing', 2),
            
            generic.task(nicollet_counselor, target_sports_location, morning_activity, cabin_activity_duration_friday_nine_ten, 124, 'Archery', 2),
            generic.task(nicollet_counselor, nature_location, morning_activity, cabin_activity_duration_friday_ten_eleven, 125, 'Nature', 2),
            generic.task(nicollet_counselor, beach_location, morning_activity, cabin_activity_duration_friday_eleven_twelve, 126, 'Beach', 2),

            generic.task(nicollet_counselor, nicollet_location, clean_cabin, duration_friday_second, 202, 'Clean Cabin', 2),

            ]
        all_tasks.extend(nicollet_tasks)

        radisson_tasks = [
            generic.task(radisson_counselor, target_sports_location, morning_activity, cabin_activity_duration_monday_nine_ten, 127, 'Archery', 2),
            generic.task(radisson_counselor, nature_location, morning_activity, cabin_activity_duration_monday_ten_eleven, 128, 'Nature', 2),
            generic.task(radisson_counselor, beach_location, morning_activity, cabin_activity_duration_monday_eleven_twelve, 129, 'Beach', 2),
            
            generic.task(radisson_counselor, homestead_location, morning_activity, cabin_activity_duration_tuesday_nine_ten, 130, 'HH', 2),
            generic.task(radisson_counselor, athletic_field_location, morning_activity, cabin_activity_duration_tuesday_ten_eleven, 131, 'AF', 2),
            generic.task(radisson_counselor, kannacks_location, morning_activity, cabin_activity_duration_tuesday_eleven_twelve, 132, 'Kannacks', 2),
            
            generic.task(radisson_counselor, outpost_location, morning_activity, tuesday_overnight_1_duration, 133, 'Overnight', 2),
            generic.task(radisson_counselor, outpost_location, morning_activity, tuesday_overnight_2_duration, 134, 'Overnight', 2),
            
            generic.task(radisson_counselor, target_sports_location, morning_activity, cabin_activity_duration_thursday_nine_ten, 135, 'Rifles', 2),
            generic.task(radisson_counselor, radisson_location, morning_activity, cabin_activity_duration_thursday_ten_eleven, 136, 'Skit', 2),
            generic.task(radisson_counselor, boat_house_location, morning_activity, cabin_activity_duration_thursday_eleven_twelve, 137, 'Boat House', 2),
            
            generic.task(radisson_counselor, corral_location, morning_activity, cabin_activity_duration_friday_nine_ten, 138, 'Corral', 2),
            generic.task(radisson_counselor, craftshop_location, morning_activity, cabin_activity_duration_friday_ten_eleven, 139, 'Craftshop', 2),
            generic.task(radisson_counselor, fishing_location, morning_activity, cabin_activity_duration_friday_eleven_twelve, 140, 'Fishing', 2),

            generic.task(radisson_counselor, radisson_location, clean_cabin, duration_friday_second, 203, 'Clean Cabin', 2),

            ]
        all_tasks.extend(radisson_tasks)
        
        schoolcraft_tasks = [
            generic.task(schoolcraft_counselor, corral_location, morning_activity, cabin_activity_duration_monday_nine_ten, 141, 'Corral', 2),
            generic.task(schoolcraft_counselor, craftshop_location, morning_activity, cabin_activity_duration_monday_ten_eleven, 142, 'Craftshop', 2),
            generic.task(schoolcraft_counselor, fishing_location, morning_activity, cabin_activity_duration_monday_eleven_twelve, 143, 'Fishing', 2),
            
            generic.task(schoolcraft_counselor, target_sports_location, morning_activity, cabin_activity_duration_tuesday_nine_ten, 144, 'Archery', 2),
            generic.task(schoolcraft_counselor, nature_location, morning_activity, cabin_activity_duration_tuesday_ten_eleven, 145, 'Nature', 2),
            generic.task(schoolcraft_counselor, beach_location, morning_activity, cabin_activity_duration_tuesday_eleven_twelve, 146, 'Beach', 2),
            
            generic.task(schoolcraft_counselor, homestead_location, morning_activity, cabin_activity_duration_wednesday_nine_ten, 147, 'HH', 2),
            generic.task(schoolcraft_counselor, athletic_field_location, morning_activity, cabin_activity_duration_wednesday_ten_eleven, 148, 'AF', 2),
            generic.task(schoolcraft_counselor, kannacks_location, morning_activity, cabin_activity_duration_wednesday_eleven_twelve, 149, 'Kannacks', 2),
            
            generic.task(schoolcraft_counselor, outpost_location, morning_activity, wednesday_overnight_1_duration, 150, 'Overnight', 2),
            generic.task(schoolcraft_counselor, outpost_location, morning_activity, wednesday_overnight_2_duration, 151, 'Overnight', 2),
            
            generic.task(schoolcraft_counselor, target_sports_location, morning_activity, cabin_activity_duration_friday_nine_ten, 152, 'Rifles', 2),
            generic.task(schoolcraft_counselor, schoolcraft_location, morning_activity, cabin_activity_duration_friday_ten_eleven, 153, 'Skit', 2),
            generic.task(schoolcraft_counselor, boat_house_location, morning_activity, cabin_activity_duration_friday_eleven_twelve, 154, 'Boat House', 2),

            generic.task(schoolcraft_counselor, schoolcraft_location, clean_cabin, duration_friday_second, 204, 'Clean Cabin', 2),
            ]
        all_tasks.extend(schoolcraft_tasks)

        ramsey_tasks = [
            generic.task(ramsey_counselor, target_sports_location, morning_activity, cabin_activity_duration_monday_nine_ten, 155, 'Rifles', 2),
            generic.task(ramsey_counselor, ramsey_location, morning_activity, cabin_activity_duration_monday_ten_eleven, 156, 'Skit', 2),
            generic.task(ramsey_counselor, boat_house_location, morning_activity, cabin_activity_duration_monday_eleven_twelve, 157, 'Boat House', 2),
            
            generic.task(ramsey_counselor, corral_location, morning_activity, cabin_activity_duration_tuesday_nine_ten, 158, 'Corral', 2),
            generic.task(ramsey_counselor, craftshop_location, morning_activity, cabin_activity_duration_tuesday_ten_eleven, 159, 'Craftshop', 2),
            generic.task(ramsey_counselor, fishing_location, morning_activity, cabin_activity_duration_tuesday_eleven_twelve, 160, 'Fishing', 2),
            
            generic.task(ramsey_counselor, target_sports_location, morning_activity, cabin_activity_duration_wednesday_nine_ten, 161, 'Archery', 2),
            generic.task(ramsey_counselor, nature_location, morning_activity, cabin_activity_duration_wednesday_ten_eleven, 162, 'Nature', 2),
            generic.task(ramsey_counselor, beach_location, morning_activity, cabin_activity_duration_wednesday_eleven_twelve, 163, 'Beach', 2),
            
            generic.task(ramsey_counselor, homestead_location, morning_activity, cabin_activity_duration_thursday_nine_ten, 164, 'HH', 2),
            generic.task(ramsey_counselor, athletic_field_location, morning_activity, cabin_activity_duration_thursday_ten_eleven, 165, 'AF', 2),
            generic.task(ramsey_counselor, kannacks_location, morning_activity, cabin_activity_duration_thursday_eleven_twelve, 166, 'Kannacks', 2),
            
            generic.task(ramsey_counselor, outpost_location, morning_activity, thursday_overnight_1_duration, 167, 'Overnight', 2),
            generic.task(ramsey_counselor, outpost_location, morning_activity, thursday_overnight_2_duration, 168, 'Overnight', 2),

            generic.task(ramsey_counselor, ramsey_location, clean_cabin, duration_friday_second, 205, 'Clean Cabin', 2),

            ]
        all_tasks.extend(ramsey_tasks)

        lower_cabin_tasks = [
            generic.task(lower_cabin_counselor, boat_house_location, morning_activity, cabin_activity_duration_monday_nine_twelve, 169, 'Boat House', 2),
            generic.task(lower_cabin_counselor, boat_house_location, morning_activity, cabin_activity_duration_tuesday_nine_twelve, 170, 'Boat House', 2),
            generic.task(lower_cabin_counselor, boat_house_location, morning_activity, cabin_activity_duration_wednesday_nine_twelve, 171, 'Boat House', 2),
            generic.task(lower_cabin_counselor, boat_house_location, morning_activity, cabin_activity_duration_thursday_nine_twelve, 172, 'Boat House', 2),
            generic.task(lower_cabin_counselor, boat_house_location, morning_activity, cabin_activity_duration_friday_nine_twelve, 173, 'Boat House', 2),

            generic.task(lower_cabin_counselor, lower_cabin_location, clean_cabin, duration_friday_second, 206, 'Clean Cabin', 2),

            ]
        all_tasks.extend(lower_cabin_tasks)

        yaqua_tasks = [
            generic.task(yaqua_counselor, corral_location, morning_activity, cabin_activity_duration_monday_nine_twelve, 174, 'Corral', 2),
            generic.task(yaqua_counselor, corral_location, morning_activity, cabin_activity_duration_tuesday_nine_twelve, 175, 'Corral', 2),
            generic.task(yaqua_counselor, corral_location, morning_activity, cabin_activity_duration_wednesday_nine_twelve, 176, 'Corral', 2),
            generic.task(yaqua_counselor, corral_location, morning_activity, cabin_activity_duration_thursday_nine_twelve, 177, 'Corral', 2),
            generic.task(yaqua_counselor, corral_location, morning_activity, cabin_activity_duration_friday_nine_twelve, 178, 'Corral', 2),

            generic.task(yaqua_counselor, yaqua_location, clean_cabin, duration_friday_second, 207, 'Clean Cabin', 2),

            ]
        all_tasks.extend(yaqua_tasks)

        erie_tasks = [
            generic.task(erie_counselor, pathfinder_location, morning_activity, cabin_activity_duration_monday_nine_twelve, 179, 'Pathfinders!', 2),
            generic.task(erie_counselor, pathfinder_location, morning_activity, cabin_activity_duration_tuesday_nine_twelve, 180, 'Pathfinders!', 2),
            generic.task(erie_counselor, pathfinder_location, morning_activity, cabin_activity_duration_wednesday_nine_twelve, 181, 'Pathfinders!', 2),
            generic.task(erie_counselor, pathfinder_location, morning_activity, cabin_activity_duration_thursday_nine_twelve, 182, 'Pathfinders!', 2),
            generic.task(erie_counselor, pathfinder_location, morning_activity, cabin_activity_duration_friday_nine_twelve, 183, 'Pathfinders!', 2),
            ]
        all_tasks.extend(erie_tasks)

        day_camper_tasks = [
            generic.task(day_camp_counselor, day_camper_location, morning_activity, cabin_activity_duration_monday_nine_twelve, 184, 'Day Campers!', 2),
            generic.task(day_camp_counselor, day_camper_location, morning_activity, cabin_activity_duration_tuesday_nine_twelve, 185, 'Day Campers!', 2),
            generic.task(day_camp_counselor, day_camper_location, morning_activity, cabin_activity_duration_wednesday_nine_twelve, 186, 'Day Campers!', 2),
            generic.task(day_camp_counselor, day_camper_location, morning_activity, cabin_activity_duration_thursday_nine_twelve, 187, 'Day Campers!', 2),
            generic.task(day_camp_counselor, day_camper_location, morning_activity, cabin_activity_duration_friday_nine_twelve, 188, 'Day Campers!', 2),
            ]
        all_tasks.extend(day_camper_tasks)

        willy_tasks = [
            generic.task(willy_counselor, corral_location, morning_activity, cabin_activity_duration_monday_nine_twelve, 189, 'Corral', 2),
            generic.task(willy_counselor, corral_location, morning_activity, cabin_activity_duration_tuesday_nine_twelve, 190, 'Corral', 2),
            generic.task(willy_counselor, corral_location, morning_activity, cabin_activity_duration_wednesday_nine_twelve, 191, 'Corral', 2),
            generic.task(willy_counselor, corral_location, morning_activity, cabin_activity_duration_thursday_nine_twelve, 192, 'Corral', 2),
            generic.task(willy_counselor, corral_location, morning_activity, cabin_activity_duration_friday_nine_twelve, 193, 'Corral', 2),

            generic.task(willy_counselor, willy_location, clean_cabin, duration_friday_second, 208, 'Clean Cabin', 2),

            ]
        all_tasks.extend(willy_tasks)

        corral_tasks = [
            generic.task(corral_director, corral_location, morning_activity, cabin_activity_duration_monday_nine_twelve, 209, 'Run Corral', 3),
            generic.task(corral_director, corral_location, morning_activity, cabin_activity_duration_tuesday_nine_twelve, 210, 'Run Corral', 3),
            generic.task(corral_director, corral_location, morning_activity, cabin_activity_duration_wednesday_nine_twelve, 211, 'Run Corral', 3),
            generic.task(corral_director, corral_location, morning_activity, cabin_activity_duration_thursday_nine_twelve, 212, 'Run Corral', 3),
            generic.task(corral_director, corral_location, morning_activity, cabin_activity_duration_friday_nine_twelve, 213, 'Run Corral', 3),

            generic.task(corral_director, corral_location, afternoon_activity, duration_monday_first, 214, 'Run Corral', 3),
            generic.task(corral_director, corral_location, afternoon_activity, duration_monday_second, 215, 'Run Corral', 3),

            generic.task(corral_director, corral_location, afternoon_activity, duration_tuesday_first, 216, 'Run Corral', 3),
            generic.task(corral_director, corral_location, afternoon_activity, duration_tuesday_second, 217, 'Run Corral', 3),

            generic.task(corral_director, corral_location, afternoon_activity, duration_wednesday_first, 218, 'Run Corral', 3),
            generic.task(corral_director, corral_location, afternoon_activity, duration_wednesday_second, 214, 'Run Corral', 3),

            generic.task(corral_director, corral_location, afternoon_activity, duration_thursday_first, 219, 'Run Corral', 3),
            generic.task(corral_director, corral_location, afternoon_activity, duration_thursday_second, 220, 'Run Corral', 3),

            generic.task(corral_director, corral_location, afternoon_activity, duration_friday_first, 221, 'Run Corral', 3),
            generic.task(corral_director, corral_location, afternoon_activity, duration_friday_second, 222, 'Run Corral', 3),            
            ]
        all_tasks.extend(corral_tasks)

        boat_house_tasks = [
            generic.task(boat_house_director, boat_house_location, morning_activity, cabin_activity_duration_monday_nine_twelve, 223, 'Run Boat House', 3),
            generic.task(boat_house_director, boat_house_location, morning_activity, cabin_activity_duration_tuesday_nine_twelve, 224, 'Run Boat House', 3),
            generic.task(boat_house_director, boat_house_location, morning_activity, cabin_activity_duration_wednesday_nine_twelve, 225, 'Run Boat House', 3),
            generic.task(boat_house_director, boat_house_location, morning_activity, cabin_activity_duration_thursday_nine_twelve, 226, 'Run Boat House', 3),
            generic.task(boat_house_director, boat_house_location, morning_activity, cabin_activity_duration_friday_nine_twelve, 227, 'Run Boat House', 3),

            generic.task(boat_house_director, boat_house_location, afternoon_activity, duration_monday_first, 228, 'Run Boat House', 3),
            generic.task(boat_house_director, boat_house_location, afternoon_activity, duration_monday_second, 229, 'Run Boat House', 3),

            generic.task(boat_house_director, boat_house_location, afternoon_activity, duration_tuesday_first, 230, 'Run Boat House', 3),
            generic.task(boat_house_director, boat_house_location, afternoon_activity, duration_tuesday_second, 231, 'Run Boat House', 3),

            generic.task(boat_house_director, boat_house_location, afternoon_activity, duration_wednesday_first, 232, 'Run Boat House', 3),
            generic.task(boat_house_director, boat_house_location, afternoon_activity, duration_wednesday_second, 233, 'Run Boat House', 3),

            generic.task(boat_house_director, boat_house_location, afternoon_activity, duration_thursday_first, 234, 'Run Boat House', 3),
            generic.task(boat_house_director, boat_house_location, afternoon_activity, duration_thursday_second, 235, 'Run Boat House', 3),

            generic.task(boat_house_director, boat_house_location, afternoon_activity, duration_friday_first, 236, 'Run Boat House', 3),
            generic.task(boat_house_director, boat_house_location, afternoon_activity, duration_friday_second, 237, 'Run Boat House', 3),            
            ]
        all_tasks.extend(boat_house_tasks)

        fishing_tasks = [
            generic.task(fishing_director, fishing_location, morning_activity, cabin_activity_duration_monday_nine_twelve, 238, 'Run Fishing', 1),
            generic.task(fishing_director, fishing_location, morning_activity, cabin_activity_duration_tuesday_nine_twelve, 239, 'Run Fishing', 1),
            generic.task(fishing_director, fishing_location, morning_activity, cabin_activity_duration_wednesday_nine_twelve, 240, 'Run Fishing', 1),
            generic.task(fishing_director, fishing_location, morning_activity, cabin_activity_duration_thursday_nine_twelve, 241, 'Run Fishing', 1),
            generic.task(fishing_director, fishing_location, morning_activity, cabin_activity_duration_friday_nine_twelve, 242, 'Run Fishing', 1),

            generic.task(fishing_director, fishing_location, afternoon_activity, duration_monday_first, 243, 'Run Fishing', 1),
            generic.task(fishing_director, fishing_location, afternoon_activity, duration_monday_second, 244, 'Run Fishing', 1),

            generic.task(fishing_director, fishing_location, afternoon_activity, duration_tuesday_first, 245, 'Run Fishing', 1),
            generic.task(fishing_director, fishing_location, afternoon_activity, duration_tuesday_second, 246, 'Run Fishing', 1),

            generic.task(fishing_director, fishing_location, afternoon_activity, duration_wednesday_first, 247, 'Run Fishing', 1),
            generic.task(fishing_director, fishing_location, afternoon_activity, duration_wednesday_second, 248, 'Run Fishing', 1),

            generic.task(fishing_director, fishing_location, afternoon_activity, duration_thursday_first, 249, 'Run Fishing', 1),
            generic.task(fishing_director, fishing_location, afternoon_activity, duration_thursday_second, 250, 'Run Fishing', 1),

            generic.task(fishing_director, fishing_location, afternoon_activity, duration_friday_first, 251, 'Run Fishing', 1),
            generic.task(fishing_director, fishing_location, afternoon_activity, duration_friday_second, 252, 'Run Fishing', 1),            
            ]
        all_tasks.extend(fishing_tasks)

        craftshop_tasks = [
            generic.task(craftshop_director, craftshop_location, morning_activity, cabin_activity_duration_monday_nine_twelve, 253, 'Run Craftshop', 1),
            generic.task(craftshop_director, craftshop_location, morning_activity, cabin_activity_duration_tuesday_nine_twelve, 254, 'Run Craftshop', 1),
            generic.task(craftshop_director, craftshop_location, morning_activity, cabin_activity_duration_wednesday_nine_twelve, 255, 'Run Craftshop', 1),
            generic.task(craftshop_director, craftshop_location, morning_activity, cabin_activity_duration_thursday_nine_twelve, 256, 'Run Craftshop', 1),
            generic.task(craftshop_director, craftshop_location, morning_activity, cabin_activity_duration_friday_nine_twelve, 257, 'Run Craftshop', 1),

            generic.task(craftshop_director, craftshop_location, afternoon_activity, duration_monday_first, 258, 'Run Craftshop', 1),
            generic.task(craftshop_director, craftshop_location, afternoon_activity, duration_monday_second, 259, 'Run Craftshop', 1),

            generic.task(craftshop_director, craftshop_location, afternoon_activity, duration_tuesday_first, 260, 'Run Craftshop', 1),
            generic.task(craftshop_director, craftshop_location, afternoon_activity, duration_tuesday_second, 261, 'Run Craftshop', 1),

            generic.task(craftshop_director, craftshop_location, afternoon_activity, duration_wednesday_first, 262, 'Run Craftshop', 1),
            generic.task(craftshop_director, craftshop_location, afternoon_activity, duration_wednesday_second, 263, 'Run Craftshop', 1),

            generic.task(craftshop_director, craftshop_location, afternoon_activity, duration_thursday_first, 264, 'Run Craftshop', 1),
            generic.task(craftshop_director, craftshop_location, afternoon_activity, duration_thursday_second, 265, 'Run Craftshop', 1),

            generic.task(craftshop_director, craftshop_location, afternoon_activity, duration_friday_first, 266, 'Run Craftshop', 1),
            generic.task(craftshop_director, craftshop_location, afternoon_activity, duration_friday_second, 267, 'Run Craftshop', 1),            
            ]
        all_tasks.extend(craftshop_tasks)

        beach_tasks = [
            generic.task(beach_director, beach_location, morning_activity, cabin_activity_duration_monday_nine_twelve, 268, 'Run Beach', 2),
            generic.task(beach_director, beach_location, morning_activity, cabin_activity_duration_tuesday_nine_twelve, 269, 'Run Beach', 2),
            generic.task(beach_director, beach_location, morning_activity, cabin_activity_duration_wednesday_nine_twelve, 270, 'Run Beach', 2),
            generic.task(beach_director, beach_location, morning_activity, cabin_activity_duration_thursday_nine_twelve, 271, 'Run Beach', 2),
            generic.task(beach_director, beach_location, morning_activity, cabin_activity_duration_friday_nine_twelve, 272, 'Run Beach', 2),

            generic.task(beach_director, beach_location, afternoon_activity, duration_monday_first, 273, 'Run Beach', 2),
            generic.task(beach_director, beach_location, afternoon_activity, duration_monday_second, 274, 'Run Beach', 2),

            generic.task(beach_director, beach_location, afternoon_activity, duration_tuesday_first, 275, 'Run Beach', 2),
            generic.task(beach_director, beach_location, afternoon_activity, duration_tuesday_second, 276, 'Run Beach', 2),

            generic.task(beach_director, beach_location, afternoon_activity, duration_wednesday_first, 277, 'Run Beach', 2),
            generic.task(beach_director, beach_location, afternoon_activity, duration_wednesday_second, 278, 'Run Beach', 2),

            generic.task(beach_director, beach_location, afternoon_activity, duration_thursday_first, 279, 'Run Beach', 2),
            generic.task(beach_director, beach_location, afternoon_activity, duration_thursday_second, 280, 'Run Beach', 2),

            generic.task(beach_director, beach_location, afternoon_activity, duration_friday_first, 281, 'Run Beach', 2),
            generic.task(beach_director, beach_location, afternoon_activity, duration_friday_second, 282, 'Run Beach', 2),            
            ]
        all_tasks.extend(beach_tasks)

        target_sports_tasks = [
            generic.task(target_sports_director, target_sports_location, morning_activity, cabin_activity_duration_monday_nine_twelve, 283, 'Run Target Sports', 1),
            generic.task(target_sports_director, target_sports_location, morning_activity, cabin_activity_duration_tuesday_nine_twelve, 284, 'Run Target Sports', 1),
            generic.task(target_sports_director, target_sports_location, morning_activity, cabin_activity_duration_wednesday_nine_twelve, 285, 'Run Target Sports', 1),
            generic.task(target_sports_director, target_sports_location, morning_activity, cabin_activity_duration_thursday_nine_twelve, 286, 'Run Target Sports', 1),
            generic.task(target_sports_director, target_sports_location, morning_activity, cabin_activity_duration_friday_nine_twelve, 287, 'Run Target Sports', 1),

            generic.task(target_sports_director, target_sports_location, afternoon_activity, duration_monday_first, 288, 'Run Target Sports', 1),
            generic.task(target_sports_director, target_sports_location, afternoon_activity, duration_monday_second, 289, 'Run Target Sports', 1),

            generic.task(target_sports_director, target_sports_location, afternoon_activity, duration_tuesday_first, 290, 'Run Target Sports', 1),
            generic.task(target_sports_director, target_sports_location, afternoon_activity, duration_tuesday_second, 291, 'Run Target Sports', 1),

            generic.task(target_sports_director, target_sports_location, afternoon_activity, duration_wednesday_first, 292, 'Run Target Sports', 1),
            generic.task(target_sports_director, target_sports_location, afternoon_activity, duration_wednesday_second, 293, 'Run Target Sports', 1),

            generic.task(target_sports_director, target_sports_location, afternoon_activity, duration_thursday_first, 294, 'Run Target Sports', 1),
            generic.task(target_sports_director, target_sports_location, afternoon_activity, duration_thursday_second, 295, 'Run Target Sports', 1),

            generic.task(target_sports_director, target_sports_location, afternoon_activity, duration_friday_first, 296, 'Run Target Sports', 1),
            generic.task(target_sports_director, target_sports_location, afternoon_activity, duration_friday_second, 297, 'Run Target Sports', 1),            
            ]
        all_tasks.extend(target_sports_tasks)

        nature_tasks = [
            generic.task(nature_director, nature_location, morning_activity, cabin_activity_duration_monday_nine_twelve, 298, 'Run Nature', 1),
            generic.task(nature_director, nature_location, morning_activity, cabin_activity_duration_tuesday_nine_twelve, 299, 'Run Nature', 1),
            generic.task(nature_director, nature_location, morning_activity, cabin_activity_duration_wednesday_nine_twelve, 300, 'Run Nature', 1),
            generic.task(nature_director, nature_location, morning_activity, cabin_activity_duration_thursday_nine_twelve, 301, 'Run Nature', 1),
            generic.task(nature_director, nature_location, morning_activity, cabin_activity_duration_friday_nine_twelve, 302, 'Run Nature', 1),

            generic.task(nature_director, nature_location, afternoon_activity, duration_monday_first, 303, 'Run Nature', 1),
            generic.task(nature_director, nature_location, afternoon_activity, duration_monday_second, 304, 'Run Nature', 1),

            generic.task(nature_director, nature_location, afternoon_activity, duration_tuesday_first, 305, 'Run Nature', 1),
            generic.task(nature_director, nature_location, afternoon_activity, duration_tuesday_second, 306, 'Run Nature', 1),

            generic.task(nature_director, nature_location, afternoon_activity, duration_wednesday_first, 307, 'Run Nature', 1),
            generic.task(nature_director, nature_location, afternoon_activity, duration_wednesday_second, 308, 'Run Nature', 1),

            generic.task(nature_director, nature_location, afternoon_activity, duration_thursday_first, 309, 'Run Nature', 1),
            generic.task(nature_director, nature_location, afternoon_activity, duration_thursday_second, 310, 'Run Nature', 1),

            generic.task(nature_director, nature_location, afternoon_activity, duration_friday_first, 311, 'Run Nature', 1),
            generic.task(nature_director, nature_location, afternoon_activity, duration_friday_second, 312, 'Run Nature', 1),            
            ]
        all_tasks.extend(nature_tasks)

        #Evening assignments
        campfires = [
            generic.task(pstaff, nature_location, campfire_category, duration_monday_night, 313, 'Campfire', 2),
            generic.task(pstaff, nature_location, campfire_category, duration_tuesday_night, 313, 'Campfire', 2),
            generic.task(pstaff, nature_location, campfire_category, duration_wednesday_night, 313, 'Campfire', 2),
            generic.task(pstaff, nature_location, campfire_category, duration_thursday_night, 313, 'Campfire', 2),

            generic.task(counselor, nature_location, campfire_category, duration_monday_night, 313, 'Campfire', 2),
            generic.task(counselor, nature_location, campfire_category, duration_tuesday_night, 313, 'Campfire', 2),
            generic.task(counselor, nature_location, campfire_category, duration_wednesday_night, 313, 'Campfire', 2),
            generic.task(counselor, nature_location, campfire_category, duration_thursday_night, 313, 'Campfire', 2),
        ]
        all_tasks.extend(campfires)

        flag_raising = [
            generic.task(counselor, flag_pole, flag_raising_category, duration_sunday_evening, 314, 'Flag Lowering',1),
            generic.task(counselor, flag_pole, flag_raising_category, duration_monday_evening, 315, 'Flag Lowering',1),
            generic.task(counselor, flag_pole, flag_raising_category, duration_tuesday_evening, 316, 'Flag Lowering',1),
            generic.task(counselor, flag_pole, flag_raising_category, duration_wednesday_evening, 317, 'Flag Lowering',1),
            generic.task(counselor, flag_pole, flag_raising_category, duration_thursday_evening, 318, 'Flag Lowering',1),
            generic.task(counselor, flag_pole, flag_raising_category, duration_friday_evening, 319, 'Flag Lowering',1),
            ]
        all_tasks.extend(flag_raising)

        breakfast_grace = [
            generic.task(counselor, dining_hall, breakfast_grace_category, duration_monday_morning, 320, 'Breakfast Grace', 1),
            generic.task(counselor, dining_hall, breakfast_grace_category, duration_tuesday_morning, 321, 'Breakfast Grace', 1),
            generic.task(counselor, dining_hall, breakfast_grace_category, duration_wednesday_morning, 322, 'Breakfast Grace', 1),
            generic.task(counselor, dining_hall, breakfast_grace_category, duration_thursday_morning, 323, 'Breakfast Grace', 1),
            generic.task(counselor, dining_hall, breakfast_grace_category, duration_friday_morning, 324, 'Breakfast Grace', 1),
            generic.task(counselor, dining_hall, breakfast_grace_category, duration_saturday_morning, 325, 'Breakfast Grace', 1),
            ]
        all_tasks.extend(breakfast_grace)

        lunch_grace = [
            generic.task(counselor, dining_hall, lunch_grace_category, duration_monday_lunch, 326, 'Lunch Grace', 1),
            generic.task(counselor, dining_hall, lunch_grace_category, duration_tuesday_lunch, 327, 'Lunch Grace', 1),
            generic.task(counselor, dining_hall, lunch_grace_category, duration_wednesday_lunch, 328, 'Lunch Grace', 1),
            generic.task(counselor, dining_hall, lunch_grace_category, duration_thursday_lunch, 329, 'Lunch Grace', 1),
            generic.task(counselor, dining_hall, lunch_grace_category, duration_friday_lunch, 330, 'Lunch Grace', 1),
            ]
        all_tasks.extend(lunch_grace)

        dinner_grace = [
            generic.task(counselor, dining_hall, dinner_grace_category, duration_sunday_evening, 331, 'Dinner Grace', 1),
            generic.task(counselor, dining_hall, dinner_grace_category, duration_monday_evening, 336, 'Dinner Grace', 1),
            generic.task(counselor, dining_hall, dinner_grace_category, duration_tuesday_evening, 332, 'Dinner Grace', 1),
            generic.task(counselor, dining_hall, dinner_grace_category, duration_wednesday_evening, 333, 'Dinner Grace', 1),
            generic.task(counselor, dining_hall, dinner_grace_category, duration_thursday_evening, 334, 'Dinner Grace', 1),
            generic.task(counselor, dining_hall, dinner_grace_category, duration_friday_evening, 335, 'Dinner Grace', 1),
            ]
        all_tasks.extend(dinner_grace)

        flag_lowering = [
            generic.task(counselor, flag_pole, flag_lowering_category, duration_sunday_evening, 337, 'Flag Lowering'),
            generic.task(counselor, flag_pole, flag_lowering_category, duration_monday_evening, 338, 'Flag Lowering'),
            generic.task(counselor, flag_pole, flag_lowering_category, duration_tuesday_evening, 339, 'Flag Lowering'),
            generic.task(counselor, flag_pole, flag_lowering_category, duration_wednesday_evening, 340, 'Flag Lowering'),
            generic.task(counselor, flag_pole, flag_lowering_category, duration_thursday_evening, 341, 'Flag Lowering'),
            generic.task(counselor, flag_pole, flag_lowering_category, duration_friday_evening, 342, 'Flag Lowering'),
            ]
        all_tasks.extend(flag_lowering)

        password = [
            generic.task(counselor, flag_pole, password_category, duration_monday_morning, 343, 'Password'),
            generic.task(counselor, flag_pole, password_category, duration_tuesday_morning, 344, 'Password'),
            generic.task(counselor, flag_pole, password_category, duration_wednesday_morning, 345, 'Password'),
            generic.task(counselor, flag_pole, password_category, duration_thursday_morning, 346, 'Password'),
            generic.task(counselor, flag_pole, password_category, duration_friday_morning, 347, 'Password'),
            generic.task(counselor, flag_pole, password_category, duration_saturday_morning, 348, 'Password'),
            ]
        all_tasks.extend(password)

        power_up = [
            generic.task(counselor, store, power_up_category, duration_monday_mid, 349, 'Power Up', 1),
            generic.task(counselor, store, power_up_category, duration_tuesday_mid, 350, 'Power Up', 1),
            generic.task(counselor, store, power_up_category, duration_wednesday_mid, 351, 'Power Up', 1),
            generic.task(counselor, store, power_up_category, duration_thursday_mid, 352, 'Power Up', 1),
            ]
        all_tasks.extend(power_up)

        quiet_cabin = [
            generic.task(pstaff, around_camp, quiet_cabin_category, duration_sunday_night, 353, 'QC', 2),
            generic.task(pstaff, around_camp, quiet_cabin_category, duration_monday_night, 354, 'QC', 2),
            generic.task(pstaff, around_camp, quiet_cabin_category, duration_tuesday_night, 355, 'QC', 2),
            generic.task(pstaff, around_camp, quiet_cabin_category, duration_wednesday_night, 356, 'QC', 2),
            generic.task(pstaff, around_camp, quiet_cabin_category, duration_thursday_night, 357, 'QC', 2),
            generic.task(pstaff, around_camp, quiet_cabin_category, duration_friday_night, 358, 'QC', 2),
            ]
        all_tasks.extend(quiet_cabin)

        trading_post = [
            generic.task(pstaff, store, trading_post_category, duration_monday_night, 359, 'Trading Post', 2),
            generic.task(pstaff, store, trading_post_category, duration_tuesday_night, 360, 'Trading Post', 2),
            generic.task(pstaff, store, trading_post_category, duration_wednesday_night, 361, 'Trading Post', 2),
            generic.task(pstaff, store, trading_post_category, duration_thursday_night, 362, 'Trading Post', 2),
            ]
        all_tasks.extend(trading_post)

        task = CampTaskCommon()
        # Afternoon assignments
        floater_count = 1
        kitchen_count = 1
        maintenance_count = 3
        kannacks_count = 2
        nature_count = 3
        target_sports_count = 2

        beach_count = 1
        life_gaurd_beach_count = 4

        craftshop_count = 5
        bikes_count = 2
        fishing_count = 2

        boat_house_count = 4
        skipper_boat_house_count = 4

        wrangler_corral_count = 2
        corral_count = 4
        afternoon_assignments = []

        afternoon_assignments += task.getAfternoon(counselor, around_camp, floater_category, 'Floater', floater_count)
        afternoon_assignments += task.getAfternoon(counselor, kitchen_location, kitchen_category, 'Kitchen', kitchen_count)
        afternoon_assignments += task.getAfternoon(counselor, maintenance_location, maintenance_category, 'Maintenance', maintenance_count)
        afternoon_assignments += task.getAfternoon(counselor, kannacks_location, kannacks_category, 'Kannacks', kannacks_count)
        afternoon_assignments += task.getAfternoon(counselor, nature_location, nature_category, 'Nature', nature_count)
        afternoon_assignments += task.getAfternoon(counselor, target_sports_location, target_sports_category, 'Target Sports', target_sports_count)
        afternoon_assignments += task.getAfternoon(lifegaurd, beach_location, beach_category, 'Beach - Lifegaurd', life_gaurd_beach_count)
        afternoon_assignments += task.getAfternoon(counselor, beach_location, beach_category, 'Beach', beach_count)
        afternoon_assignments += task.getAfternoon(counselor, craftshop_location, craftshop_category, 'Craftshop', craftshop_count)
        afternoon_assignments += task.getAfternoon(counselor, bikes_location, bikes_category, 'Bikes', bikes_count)
        afternoon_assignments += task.getAfternoon(counselor, fishing_location, fishing_category, 'Fishing', fishing_count)
        afternoon_assignments += task.getAfternoon(counselor, boat_house_location, boat_house_category, 'Boat House', boat_house_count)
        afternoon_assignments += task.getAfternoon(skipper, boat_house_location, boat_house_category, 'Boat House - Skipper', skipper_boat_house_count)
        afternoon_assignments += task.getAfternoon(wrangler, corral_location, corral_category, 'Corral - Wrangler', wrangler_corral_count)
        afternoon_assignments += task.getAfternoon(counselor, corral_location, corral_category, 'Corral', corral_count)

        all_tasks.extend(afternoon_assignments)
        #endregion

        #Staff Members
        #region
        staff_members = []
        staff = CampStaffCommon()

        # 34 staff. 
        preferences = [like_boat_house, like_target_sports, like_campfire]
        groups = [grossielliers_counselor]
        staff_members.append(staff.get_counselor('Sam R', preferences, groups))

        preferences = [like_kannacks, like_boat_house, like_fishing, like_beach, dislike_corral, like_campfire]
        groups = [grossielliers_counselor, lifegaurd]
        staff_members.append(staff.get_counselor('Nolan H', preferences, groups))

        preferences = [like_beach, like_kannacks, like_craftshop, dislike_corral, dislike_boat_house]
        groups = [frontenac_counselor, lifegaurd]
        staff_members.append(staff.get_counselor('Matthew L', preferences, groups))

        preferences = [like_kannacks, like_boat_house, dislike_corral, like_campfire]
        groups = [frontenac_counselor, lifegaurd]
        staff_members.append(staff.get_counselor('Jasper N', preferences, groups))

        preferences = [like_kannacks, like_nature, like_bikes]
        groups = [duluth_counselor]
        staff_members.append(staff.get_counselor('Jacob R', preferences, groups))

        preferences = [like_beach, like_kannacks, like_target_sports, dislike_corral, like_trading_post, like_quiet_cabin]
        groups = [duluth_counselor, lifegaurd]
        staff_members.append(staff.get_counselor('Leo A', preferences, groups))

        preferences = [like_beach, like_boat_house, like_kannacks, dislike_fishing]
        groups = [jolliet_counselor, lifegaurd]
        staff_members.append(staff.get_counselor('Peter F', preferences, groups))

        preferences = [like_bikes, like_nature, like_corral, dislike_fishing]
        groups = [jolliet_counselor]
        staff_members.append(staff.get_counselor('Eric O', preferences, groups))

        preferences = [like_nature, like_fishing, like_boat_house, dislike_craftshop, like_campfire]
        groups = [hennepin_counselor]
        staff_members.append(staff.get_counselor('Sam B', preferences, groups))

        preferences = [like_bikes, like_craftshop, like_fishing, dislike_beach, cannot_work_corral, like_quiet_cabin, like_trading_post, like_power_up]
        groups = [hennepin_counselor]
        staff_members.append(staff.get_counselor('Charlie M', preferences, groups))

        preferences = [like_nature, like_target_sports, like_boat_house, dislike_beach, like_quiet_cabin]
        groups = [la_verendrye_counselor]
        staff_members.append(staff.get_counselor('Sam D', preferences, groups))

        preferences = [like_kannacks, like_bikes, like_target_sports, like_quiet_cabin]
        groups = [la_verendrye_counselor]
        staff_members.append(staff.get_counselor('Mohmed R', preferences, groups))

        preferences = [like_boat_house, like_bikes, like_target_sports, dislike_corral, like_campfire]
        groups = [le_sueur_counselor, skipper]
        staff_members.append(staff.get_counselor('Graham C', preferences, groups))

        preferences = [like_beach, like_kannacks, like_bikes, dislike_corral, dislike_craftshop, dislike_nature, like_quiet_cabin]
        groups = [le_sueur_counselor, lifegaurd]
        staff_members.append(staff.get_counselor('Richard R', preferences, groups))

        preferences = [like_nature, like_target_sports, like_craftshop]
        groups = [marquette_counselor, lifegaurd]
        staff_members.append(staff.get_counselor('Patrick H', preferences, groups))

        preferences = [like_boat_house, like_beach, like_kannacks]
        groups = [marquette_counselor, lifegaurd]
        staff_members.append(staff.get_counselor('Sam P', preferences, groups))

        preferences = [like_boat_house, like_beach, like_kannacks, dislike_corral, like_trading_post, like_power_up]
        groups = [lifegaurd, wrangler, nicollet_counselor]
        staff_members.append(staff.get_counselor('Karen L', preferences, groups))

        preferences = [like_boat_house, like_beach, like_kannacks, dislike_corral, like_campfire]
        groups = [skipper, nicollet_counselor]
        staff_members.append(staff.get_counselor('Sarah P', preferences, groups))

        preferences = [like_craftshop, like_kannacks, like_target_sports, dislike_boat_house]
        groups = [radisson_counselor, lifegaurd]
        staff_members.append(staff.get_counselor('Katherine D', preferences, groups))

        preferences = [like_beach, like_kannacks, like_corral]
        groups = [radisson_counselor]
        staff_members.append(staff.get_counselor('Sophia S', preferences, groups))

        preferences = [like_corral, like_craftshop, like_nature, dislike_boat_house, dislike_beach, like_quiet_cabin]
        groups = [schoolcraft_counselor, wrangler]
        staff_members.append(staff.get_counselor('Sam L', preferences, groups))

        preferences = [like_corral]
        groups = [schoolcraft_counselor, wrangler, skipper, lifegaurd]
        staff_members.append(staff.get_counselor('Sarah F', preferences, groups))

        preferences = [like_boat_house, like_beach, like_kannacks, dislike_corral, like_trading_post, like_power_up]
        groups = [lifegaurd, ramsey_counselor]
        staff_members.append(staff.get_counselor('Lauren W', preferences, groups))

        preferences = [like_boat_house, like_craftshop, like_fishing, dislike_beach, dislike_corral, like_trading_post, like_power_up]
        groups = [ramsey_counselor]
        staff_members.append(staff.get_counselor('Hannah W', preferences, groups))

        preferences = [like_nature, like_craftshop, like_target_sports, cannot_work_corral, like_trading_post, like_power_up]
        groups = [lower_cabin_counselor]
        staff_members.append(staff.get_counselor('Madi C', preferences, groups))

        preferences = [like_corral, like_nature, like_target_sports, dislike_beach, dislike_boat_house, like_campfire]
        groups = [lower_cabin_counselor, lifegaurd, wrangler]
        staff_members.append(staff.get_counselor('Cate D', preferences, groups))

        preferences = [like_corral, like_beach, like_nature, dislike_bikes, like_campfire]
        groups = [yaqua_counselor, lifegaurd]
        staff_members.append(staff.get_counselor('Abby L', preferences, groups))

        preferences = [like_nature, like_bikes, like_craftshop, dislike_fishing, dislike_target_sports]
        groups = [yaqua_counselor]
        staff_members.append(staff.get_counselor('Leah F', preferences, groups))

        preferences = [like_corral, like_craftshop, like_kannacks, dislike_boat_house]
        groups = [erie_counselor, path_finder_counselor, wrangler]
        staff_members.append(staff.get_counselor('Emily L', preferences, groups))

        preferences = [like_corral, like_craftshop, like_beach, like_campfire]
        groups = [erie_counselor, path_finder_counselor, wrangler]
        staff_members.append(staff.get_counselor('Danee V', preferences, groups))

        preferences = [like_target_sports, like_craftshop, like_fishing, dislike_boat_house]
        groups = [day_camp_counselor]
        staff_members.append(staff.get_counselor('Kailey G', preferences, groups))

        preferences = [like_beach, like_boat_house, like_fishing, cannot_work_corral, dislike_campfire]
        groups = [day_camp_counselor]
        staff_members.append(staff.get_counselor('Emerald T', preferences, groups))

        preferences = [like_beach, like_boat_house, like_craftshop, dislike_corral, like_quiet_cabin]
        groups = [willy_counselor, lifegaurd]
        staff_members.append(staff.get_counselor('Lisa S', preferences, groups))

        preferences = [like_corral, dislike_campfire]
        groups = [willy_counselor, wrangler]
        staff_members.append(staff.get_counselor('Margriet', preferences, groups))

        scheduler = ScheduleGenerator(staff_members, [], all_tasks)
        scheduler_settings = SchedulerSettings(True, 100, True)
        all_staff = StaffMemberList(staff_members)
        scheduler.advanced_schedule(scheduler_settings, all_tasks, all_staff, [])

        #endregion


        

if __name__ == '__main__':
    unittest.main()
