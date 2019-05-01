"""
Definition of forms.
"""

from django import forms
from app import models
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from app.models import Profile
from .models import Task
from .models import Availability
#from .models import Profile

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Profile
        users = User.objects.all()
        fields = ()
    def save(self, commit = True):
        employee = super(AddEmployeeForm, self).save(commit = False)
        if commit:
            employee.save()
        return employee

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ()
    def save(self, commit = True):
        task = super(AddTaskForm, self).save(commit = False)
        if commit:
            pass;
            #task.save()
        return task
