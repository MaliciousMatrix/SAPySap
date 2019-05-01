"""
Definition of urls for SAP1.
"""

from datetime import datetime
from django.conf.urls import url
#import django.contrib.auth.views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from app import views
import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),

    url(r'^logout$', auth_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
    url(r'^admin/', admin.site.urls),


    url(r'^Register$', app.views.Register, name='register'),
    #GM URLS

    url(r'^schedule$', app.views.schedule, name='schedule'),
    url(r'^SelectEmployees$', views.StaffView.as_view(), name='Select'),
    url(r'^SelectTemplate$', views.TemplateView.as_view(), name='SelectTemplate'),
    url(r'^Optimization$', views.OptimizationSettingsView.as_view(), name='OptimizationSettings'),
    url(r'^GeneratingSchedule$', views.GeneratingScheduleView.as_view(), name='GeneratingSchedule'),
    url(r'^AddEmployees$', app.views.AddEmployees, name='AddEmployees'),
    url(r'^AddTask$', app.views.AddTasks, name='AddTask'),
    # place holder. Fix later. 
    url(r'^SelectTask$', app.views.AddTasks, name='SelectTasks'),
    url(r'^Review$', app.views.Review, name='Review'),
    url(r'^EditTemplate$', views.EditCreateTemplate.as_view(), name='EditTemplate'),
    url(r'^EditEmployee$', app.views.EditEmployee, name='EditEmployee'),
    url(r'^GMHome', app.views.GMHome, name='GMHome'),
    url(r'^GMMessageInbox$', app.views.GMMessageInbox, name='GMInbox'),
    url(r'^ReviewTORequests$', app.views.ReviewRequest, name='ReviewTimeOffRequests'),
    url(r'^ScheduleGM$', app.views.SchedulePageGM, name='scheduleGM'),
    url(r'^ViewTORequests$', app.views.ViewTimeOffRequests, name='ViewTimeOffRequests'),
    url(r'^Workers$', app.views.WorkerList, name='Workers'),
    url(r'^profile$', app.views.profile, name='profile'),

    #Employee URLS
    url(r'^Coworkers$', app.views.Coworker, name='Coworker'),
    url(r'^timeOff$', app.views.timeOff, name='timeOff'),
    url(r'^EditProfile$', app.views.EditPersonalProfile, name='EditProfile'),
    url(r'^EmployeeHome$', views.EmployeeHome.as_view(), name='EmployeeHome'),
    url(r'^EmployeeInbox$', app.views.MessageInboxEmployeeSide, name='EmployeeInbox'),
    url(r'^EmployeeSchedules$', app.views.ScheduleListEmployee, name='EmployeeSchedules'),
    url(r'^SingleEmployeeSchedule$', app.views.SingleSchedulePageEmployee, name='EmployeeSingleSchedule'),
    url(r'^Notifications$', app.views.Notifications, name='Notifications'),
    url(r'^SelectError$', app.views.SelectError, name='SelectError'),
    url(r'^ShiftTradeForum$', app.views.ShiftTradeForumHome, name='ShiftTradeForum'),
    url(r'^ShiftTradeExtend$', app.views.ShiftTradeExtend, name='ShiftTradeExtend'),
    url(r'^CreatePost$', app.views.CreatePostOffer, name='CreatePostOffer'),
    path('accounts/', include('django.contrib.auth.urls')),
]
