from task import Task
from staff_member import StaffMember

class StaffMemberSorter:
     def get_least_available_staff_members_for_tasks(tasks, staff_members, sort_out_unavailable=True):
        staff_dict = {}
        staff_list = []
        for member in staff_members:
            task_count = member.get_amount_of_tasks_this_can_take(tasks)
            staff_dict[member.id] = task_count
        max_value = 0
        min_value = 0

        if sort_out_unavailable:
            min_value = 1

        # Get the maximum value of the number of tasks that a staff member can take. 
        for key, value in staff_dict.items():
            if value > max_value:
                max_value = value

        # Lastly, go through the dictionary of staff members and the num tasks that can be assigned to each one. 
        #Starting with the ones that can be assigned the least amount of tasks. 
        for i in range(min_value, max_value + 1):
            for key, value in staff_dict.items():
                if value == i:
                    staff_list.append(StaffMemberSorter.get_staff_member_from_id(key, staff_members))

        return staff_list

     def get_least_available_staff_member(tasks, staff_members, sort_out_unavailable=True):
        return StaffMemberSorter.get_least_available_staff_members_for_tasks(tasks, staff_members, sort_out_unavailable)[0]

     def get_most_available_staff_members_for_tasks(tasks, staff_members, sort_out_unavailable=True):
        return StaffMemberSorter.get_least_available_staff_members_for_tasks(tasks, staff_members, sort_out_unavailable)[::-1]

     def get_most_available_staff_member(tasks, staff_members, sort_out_unavailable=True):
        return StaffMemberSorter.get_most_available_staff_members_for_tasks(tasks, staff_members, sort_out_unavailable)[0]

     def get_staff_member_from_id(id, staff_members):
        for member in staff_members:
            if member.id == id:
                return member