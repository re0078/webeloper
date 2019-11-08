from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from re import findall

from web.models import Course


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name = forms.CharField(max_length=32, help_text='Last name')
    email = forms.EmailField(max_length=64, help_text='email address')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class CourseForm(ModelForm):
    # department = forms.CharField(max_length=100)
    # name = forms.CharField(max_length=100)
    # course_number = forms.IntegerField()
    # group_number = forms.IntegerField()
    # teacher = forms.CharField(max_length=100)
    # start_time = forms.CharField(max_length=100)
    # end_time = forms.CharField(max_length=100)
    # first_day = forms.ModelChoiceField([0, 1, 2, 3, 4])
    # second_day = forms.ModelChoiceField([0, 1, 2, 3, 4])

    class Meta:
        model = Course
        fields = ['department', 'name', 'course_number', 'group_number', 'teacher', 'start_time', 'end_time',
                  'first_day', 'second_day', 'exam_day']
