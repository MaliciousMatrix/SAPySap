from task import Task
from staff_member import StaffMember

class TaskSorter:
    def get_hardest_to_assign_tasks(tasks, staff_members, sort_out_zeroes=True):
        '''
        Orders the given tasks with the first being the most difficult to assign to the given staff members and the last one being the easiest to assign based on
        how many staff members can take each task.
        '''
        task_dict = {}
        task_list = []
        # For each task we pass in we check how many staff could be given that task. 
        for task in tasks:
            availabile_employees = task.amount_of_staff_who_can_take_this_task(staff_members)
            task_dict[task.id] = availabile_employees
        max_value = 0
        min_value = 0

        if sort_out_zeroes:
            min_value = 1

        # Get the maximum value of num employees that a task can take. 
        for key, value in task_dict.items():
            if value > max_value:
                max_value = value

        # Lastly, go through the dictionary of tasks and the num of employees that can be assigned to each one. 
        # Starting with the ones that can be assigned to the least amount of employees, add them to the return list.
        for i in range(min_value, max_value + 1):
            for key, value in task_dict.items():
                if value == i:
                    task_list.append(TaskSorter.get_task_from_id(key, tasks))

        return task_list

    def get_easiest_to_assign_tasks(tasks, staff_members, sort_out_zeroes=True):
        '''
        Orders the given tasks with the first being the easiest to assign to the given staff members and the last one being the most difficult to assign based on
        how many staff members can take each task.
        '''
        return TaskSorter.get_hardest_to_assign_tasks(tasks, staff_members, sort_out_zeroes)[::-1]

    def get_most_difficult_task_to_assign(tasks, staff_members, sort_out_zeroes=True):
        hardest_list = TaskSorter.get_hardest_to_assign_tasks(tasks, staff_members, sort_out_zeroes)
        if len(hardest_list) == 0:
            return None
        return hardest_list[0]

    def get_easiest_task_to_assign(tasks, staff_members, sort_out_zeroes):
        easiest_list = TaskSorter.get_easiest_to_assign_tasks(tasks, staff_members, sort_out_zeroes)
        if len(easiest_list) == 0:
            return None
        return easiest_list[0]

    def get_task_from_id(id, tasks):
        for task in tasks:
            if task.id == id:
                return task

