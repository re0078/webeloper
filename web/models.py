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
