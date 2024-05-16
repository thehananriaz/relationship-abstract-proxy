from django.db import models

class CommonInfo(models.Model):
    Name = models.CharField(max_length=70)
    Age = models.IntegerField(null=True, blank=True)
    Salary = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True

class Employee(CommonInfo):
    hours = models.IntegerField()

class Manager(CommonInfo):
    role = models.CharField(max_length=100)

class Contractor(CommonInfo):
    payment = models.IntegerField()
    Salary = None