"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from app.models import Profile
from app.models import Availability
from .models import Task
from django.db import connection
from django.contrib.auth.models import Group, User
from .forms import AddTaskForm
from .forms import AddEmployeeForm
from app.models import Task
from app.models import Schedule
from app.models import Template
from .models import Notification
from .mixins import RequireLoginMixin
from app.models import OptimizationSettings
from django.views import generic
from django.views.generic.base import TemplateResponseMixin
import sys
import os
from schedule_generation_assembler import ScheduleGenerationAssembler
from .models import OptimizationSettings
session_staff_id_tag = 'selected_staff_ids'
session_template_tag = 'selected_template_id'

## App Pages
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/App Pages/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Staff Assignment Program',
            'message': 'Home page of SAP.',
            'year':datetime.now().year,
        }
    )

## GM Pages

def AddEmployees(request):
    """Renders the add employees page"""
    assert isinstance(request, HttpRequest)
    context = {
            'title': 'Add a new task',
            'message': 'The page for adding a new task.',
            'year':datetime.now().year,
            }
    if request.method == 'POST':    #if sending data to the server (POST)
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/SelectEmployees')
    else: #(GET)
        form = AddEmployeeForm()    #Form to render
        context = {
            'title': 'Add a new employee',
            'message': 'The page for adding a new employee.',
            'year':datetime.now().year,
            'form': form
            }
        return render(request, 'app/GM Pages/AddEmployees.html', context) #Receiving data from the server (GET)

def AddTasks(request):
    """Renders the add tasks page"""
    assert isinstance(request, HttpRequest)
    context = {
            'title': 'Add a new task',
            'message': 'The page for adding a new task.',
            'year':datetime.now().year,
            }
    if request.method == 'POST':    #if sending data to the server (POST)
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/SelectTask')
    else: #(GET)
        form = AddTaskForm()    #Form to render
        context = {
            'title': 'Add a new Task',
            'message': 'The page for adding a new task.',
            'year':datetime.now().year,
            'form': form
            }
        return render(request, 'app/GM Pages/AddTask.html', context) #Receiving data from the server (GET)


class EditCreateTemplate(RequireLoginMixin, generic.ListView):
    template_name = "app/GM Pages/CreateEditTemplate.html"
    context_object_name = 'Task_List'
    def get_queryset(self):
        return Task.objects

def EditEmployee(request):
    """Renders the edit Employee Page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/GM Pages/EditEmployee.html',
        {
            'title':'Edit Employee',
            'message':'Edit employee pay/certification',
            'year':datetime.now().year,
        }
    )

def GMHome(request):
    """Renders the home page for GM."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/GM Pages/GMHome.html',
        {
            'title':'Home',
            'message':'Home for GM',
            'year':datetime.now().year,
        }
    )

def GMMessageInbox(request):
    """Renders the inbox for GM."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/GM Pages/GMMessageInbox.html',
        {
            'title':'Messages',
            'message':'Messages for GM',
            'year':datetime.now().year,
        }
    )

def ReviewRequest(request):
    """Renders the review request page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/GM Pages/ReviewRequest.html',
        {
            'title':'Review Requests',
            'message':'Review employee time off requests',
            'year':datetime.now().year,
        }
    )

def SchedulePageGM(request):
    """Renders the schedule page for GM."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/GM Pages/SchedulePageGM.html',
        {
            'title':'Schedules',
            'message':'Schedule list for GM',
            'year':datetime.now().year,
        }
    )

def schedule(request):
    """Renders the Schedule page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/GM Pages/schedule.html',
        {
            'title': 'Schedule',
            'message': 'The schedule generation page.',
            'year':datetime.now().year,
        }
    )

class StaffView(RequireLoginMixin, generic.ListView):
    template_name='app/GM Pages/SelectEmployees.html'
    context_object_name = 'Employee_List'
    def get_queryset(self):
        return Profile.objects
    def get_context_data(self, **kwargs):
        context = super(StaffView, self).get_context_data(**kwargs)
        context['Availability_List'] = Availability.objects

        return context

class TemplateView(RequireLoginMixin, generic.ListView):
    template_name='app/GM Pages/SelectTemplate.html'
    context_object_name = 'Template_List'

    def get_queryset(self):
        return Template.objects



    def post(self, request):
        staff_choices = request.POST.getlist('staff_choice')
        request.session[session_staff_id_tag] = None
        request.session[session_staff_id_tag] = staff_choices
        return redirect('SelectTemplate')

class OptimizationSettingsView(TemplateResponseMixin, generic.View):
    template_name='app/GM Pages/OptimizationSettings.html'
    model = OptimizationSettings

    def get_queryset(self, optimization_id):
        return OptimizationSettings.objects.get(pk=optimization_id)

    def post(self, request):
        optimization_id = request.POST.get('template_choice')
        request.session[session_template_tag] = None
        request.session[session_template_tag] = optimization_id
        queryset = self.get_queryset(optimization_id)
        context = {'settings' : queryset}
        return self.render_to_response(context)

class GeneratingScheduleView(TemplateResponseMixin, generic.View):
    template_name='app/GM Pages/GeneratingSchedule.html'
    model = Schedule

    def post(self, request):
        context = {}
        generator = ScheduleGenerationAssembler()
        staff_ids = request.session[session_staff_id_tag]
        template_id = request.session[session_template_tag]

        template = Template.objects.get(id=template_id)
        staff = Profile.objects.filter(id__in=staff_ids)

        settings = OptimizationSettings()
        settings.avoid_overtime = True
        settings.start_overtime_at = 40
        settings.take_preferences_into_account = True  
        allow_split_shifts = True

        generator.assemble(staff, template, settings, 'My schedule');
        context = {'staff': staff, 'template':template}
        return self.render_to_response(context)

def SelectTasks(request):
    """Renders the add tasks page"""
    #Tasks = Task

    assert isinstance(request, HttpRequest)
    context = {
        'title': 'Select Task', 
        'message': 'The page for selecting tasks.',
        'year':datetime.now().year,
        }
    return render(request, 'app/GM Pages/SelectTasks.html', context)    #Render this form
    #if request.method == 'POST':    #if sending data to the server (POST)
    #    form = SelectTasksForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        return redirect('/Review')
    #else: #(GET)
    #    form = SelectTasksForm()    #Form to render
    #    context = {
    #        'title': 'Select Task',
    #        'message': 'The page for selecting tasks.',
    #        'year':datetime.now().year,
    #        'form': form,
    #        'Task_List' : Tasks

    #        }

def SelectTemplate(request):
    """Renders the select template page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/GM Pages/SelectTemplate.html',
        {
            'title':'Select Template',
            'message':'Select template for schedule',
            'year':datetime.now().year,
        }
    )

def ViewTimeOffRequests(request):
    """Renders the page that shows all the time off requests."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/GM Pages/ViewTimeOffRequests.html',
        {
            'title':'Time Off Requests',
            'message':'View list of time off requests',
            'year':datetime.now().year,
        }
    )

def WorkerList(request):
    """Renders the employee time off page."""
    assert isinstance(request, HttpRequest)
    workers = Profile.objects
    context = {}
    return render(
        request,
        'app/GM Pages/WorkerList.html',
        {
            'title':'Workers',
            'message':'See list of workers for a company',
            'year':datetime.now().year,
            'Employee_List' : workers,
        }
    )
       

def Review(request):
    """Renders the review page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/GM Pages/Review.html',
        {
            'title': 'Review',
            'message': 'The page for reviewing a schedule details.',
            'year':datetime.now().year,
        }
    )
    
def profile(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Employee Pages/profile.html',
        {
           'title':'Show Profile',
           'message': 'the page for viewing a user profile',
           'year':datetime.now().year,
           }
        )

## Employee Pages

def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def EditPersonalProfile(request):
    """Renders the employe edit page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Employee Pages/EditPersonalProfile.html',
        {
            'title':'Edit Profile',
            'message':'Edit Profile',
            'year':datetime.now().year,
        }
    )

class EmployeeHome(RequireLoginMixin, generic.ListView):
    template_name='app/Employee Pages/EmployeeHomePage.html'
    context_object_name = 'Schedule_List'
    
    def get_queryset(self):
        return Schedule.objects

def MessageInboxEmployeeSide(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Employee Pages/MessageInboxEmployeeSide.html',
        {
            'title':'Messages',
            'message':'View personal inbox',
            'year':datetime.now().year,
        }
    )

def Notifications(request):
    assert isinstance(request, HttpRequest)
    notifications = Notification.objects.order_by('time_sent').reverse().filter(user = request.user)
    return render(
        request,
        'app/Employee Pages/Notifications.html',
        {
            'year':datetime.now().year,
            'notifications':notifications,
        }
    )

def ScheduleListEmployee(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Employee Pages/ScheduleListEmployee.html',
        {
            'title':'Schedules',
            'message':'Personal schedules',
            'year':datetime.now().year,
        }
    )

def SelectError(request):    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Employee Pages/SelectError.html',
        {
            'title':'Select Error',
            'message':'Select error in scheudle',
            'year':datetime.now().year,
        }
    )

def ShiftTradeForumHome(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Employee Pages/ShiftTradeForumHome.html',
        {
            'title':'Shift Trading Forum',
            'message':'Forum for trading shifts',
            'year':datetime.now().year,
        }
    )

def ShiftTradeExtend(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Employee Pages/ShiftTradePost.html',
        {
            'year':datetime.now().year,
        }
    )

def CreatePostOffer(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Employee Pages/CreatePostOffer.html',
        {
            'year':datetime.now().year,
        }
    )

def SingleSchedulePageEmployee(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Employee Pages/SingleSchedulePageEmployee.html',
        {
            'title':'Schedule',
            'message':'Single personal Schedule',
            'year':datetime.now().year,
        }
    )


def Coworker(request):
    """Renders the coworker list page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Employee Pages/ViewCoworker.html',
        {
            'title':'Coworkers',
            'message':'List of coworkers',
            'year':datetime.now().year,
        }
    )

def timeOff(request):
    """Renders the employee time off page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Employee Pages/TimeOffRequestEmployee.html',
        {
            'title':'Time Off',
            'message':'View personal time off requests',
            'year':datetime.now().year,
        }
    )

def Register(request):
    """Renders the register page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Misc Screens/Register.html',
        {
            'year':datetime.now().year,
        }
    )