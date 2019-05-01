from django.contrib import admin
from .models import Availability
from .models import Certification
from .models import Task
from .models import Schedule
from .models import Profile
from .models import Vehicle
from .models import TimeOffRequest
from .models import AssignedTask
from .models import Template
from .models import Location
from .models import Role
from .models import Preference
from .models import Category
from django.contrib.auth.models import User
from .models import OptimizationSettings
from .models import Notification

#----------------------------------------------------------------------
# Register profile and associated (USER)
#----------------------------------------------------------------------

class AvailabilityInLine(admin.TabularInline):
    model = Availability
    extra = 0

class VehicleInLine(admin.TabularInline):
    model = Vehicle
    extra = 0

class TimeOffRequestInLine(admin.TabularInline):
    model = TimeOffRequest
    extra = 0

class PreferenceInLine(admin.TabularInline):
    model = Preference
    extra = 0

class ProfileAdmin(admin.ModelAdmin):
    #fields = ['Day', 'AvailabilityStartTime', 'AvailabilityEndTime']
    inlines = [AvailabilityInLine, TimeOffRequestInLine, VehicleInLine, PreferenceInLine]

admin.site.register(Profile, ProfileAdmin)

#----------------------------------------------------------------------
# Register Template and associated
#----------------------------------------------------------------------


class TaskInLine(admin.TabularInline):
    model = Task
    extra = 0

class RoleInLine(admin.TabularInline):
    model = Role
    extra = 0

class TemplateAdmin(admin.ModelAdmin):
    inlines = [TaskInLine]

admin.site.register(Template, TemplateAdmin)

#----------------------------------------------------------------------
# Register schedule and associated
#----------------------------------------------------------------------

class AssignedTaskInline(admin.TabularInline):
    model = AssignedTask
    extra = 0

class ScheduleAdmin(admin.ModelAdmin):
    inlines = [AssignedTaskInline]

#----------------------------------------------------------------------
# Misc
#----------------------------------------------------------------------

admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Task)
admin.site.register(Vehicle)
admin.site.register(Availability)
admin.site.register(TimeOffRequest)
admin.site.register(AssignedTask)
admin.site.register(Certification)
admin.site.register(Location)
admin.site.register(Role)
admin.site.register(Category)
admin.site.register(OptimizationSettings)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']
admin.site.register(Notification)

