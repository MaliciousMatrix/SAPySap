from staff_member import StaffMember
from task import Task 
from bad_task_assignment_exception import BadTaskAssignmentException
from task_trade_exception import TaskTradeException
class TaskTrader():
    def trade_2_tasks(self, staff_member1, staff_member2, task1, task2):
        '''
        By the end of method execution staff_member1 will have task2 and staff_member2 will have task1. 
        The staff members must be able to be assigned the others tasks. 
        '''
        staff_members = [
            staff_member1,
            staff_member2,
            ]

        tasks = [
            task1,
            task2,
            ]
        self.trade_tasks(staff_members, tasks)

    def trade_3_tasks(self, staff_member1, staff_member2, staff_member3, task1, task2, task3):
        staff_members = [
            staff_member1,
            staff_member2,
            staff_member3,
            ]

        tasks = [
            task1,
            task2,
            task3,
            ]
        self.trade_tasks(staff_members, tasks)

    def trade_tasks(self, staff_members, tasks):
        '''
        Will trade the tasks among the staff members. the first staff will get the second task, the second staff will get the third task
        and so on until the last staff gets the first task. 

        '''
        assert len(staff_members) == len(tasks), 'The length of the staff members list must be the same as the length of the task list.'
        assert len(staff_members) >= 2, 'The length of the staff members list must be 2 or greater. '

        # First we check that we can remove the tasks. This way if we can't we don't get into a state where some members have removed tasks and others don't.
        for i in range(len(staff_members)):
            assert staff_members[i].can_remove_task(tasks[i]), 'Staff member at index %d must have task at that index %d and it must be able to be removed from the staff member.' % (i,i)

        # Remove the tasks. 
        for i in range(len(staff_members)):
            staff_members[i].remove_task(tasks[i])


        # we don't want to go to the last staff member other wise we'll assign a task outside of the task list.
        # Next, we'll run a check to see if we can assign the task to the member. 
        try:
            for i in range(len(staff_members)-1):
                assert staff_members[i].can_assign_task(tasks[i+1]), 'tried to assign a task %s to a staff member %s during a trade but it failed. ' % (str(staff_members[i]), str(tasks[i]))
            staff_members[len(staff_members)-1].can_assign_task(tasks[0]), 'tried to assign a task %s to a staff member %s during a trade but it failed. ' % (str(staff_members[len(staff_members)-1]), str(tasks[0]))
        except:
            # In the event of an exception while checking to see if we can assign the task we reassign all of the original tasks to the 
            # staff members that way we know what state the system is in. 
            for i in range(len(staff_members)):
                staff_member[i].assign_task(tasks[i])

            raise BadTaskAssignmentException('Cannot one of the tasks to the members.')

        #Lastly, we assign the new tasks to the members. 
        try:
            for i in range(len(staff_members)-1):
                staff_members[i].assign_task(tasks[i+1])
            staff_members[len(staff_members)-1].assign_task(tasks[0])
        except BadTaskAssignmentException:
            # In this case because we are in an error state and have no idea who has been assigned what tasks we raise a custom exception.
            raise TaskTradeException()

