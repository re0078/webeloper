from re import findall

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Course(models.Model):
    DAY_CHOICES = (
        (0, "شنبه"),
        (1, " یک شنبه"),
        (2, " دو شنبه"),
        (3, " سه شنبه"),
        (4, " چهار شنبه"),
    )
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    first_day = models.IntegerField(choices=DAY_CHOICES)
    second_day = models.IntegerField(choices=DAY_CHOICES)
    exam_day = models.CharField(max_length=100)
    students = models.ManyToManyField(User)

    def is_valid(self):
        print(self.exam_day)
        if len(findall(r'^\d\d:\d\d$', str(self.start_time))) > 0 and len(
                findall(r'^\d\d:\d\d$', str(self.end_time))) > 0 and len(
                    findall(r'^\d\d\d\d-\d\d-\d\d$', str(self.exam_day))) > 0:
            return True
        return False


class profile(models.Model):
    image_url = models.CharField(max_length=1000)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True, )
