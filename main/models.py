from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Immunization(models.Model):
    duration_CHOICES = (
                    ('month', 'month'),
                    ('year', 'year'),
                    )
    dose_CHOICES = (
                    ('recommended','recommended'),
                    ('catching-up','catching-up')
    )
    name = models.CharField(max_length = 100, blank = False, verbose_name = 'Name of the vaccine')
    dose_no = models.IntegerField()
    total_dose = models.IntegerField()
    Type_of_dose = models.CharField(max_length = 20,choices=dose_CHOICES)
    duration_from = models.IntegerField( )
    duration_to = models.IntegerField( )
    duration_in = models.CharField(max_length = 6, verbose_name="Select duration",choices=duration_CHOICES)
    description = models.TextField(max_length = 200)

    def __str__(self):
        return self.name + ' - Dose ' + str(self.dose_no)

@receiver(post_save, sender=Immunization)
def update_sched_immun_create(sender, instance, **kwargs):
     pat = Patient.objects.all()
     for p in pat:
         m1 = Schedule(immunization=instance, patient=p)
         m1.save()

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    vaccine = models.ManyToManyField(Immunization, through='Schedule')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

@receiver(post_save, sender=Patient)
def update_sched_pat_create(sender, instance, **kwargs):
     immun = Immunization.objects.all()
     for im in immun:
         m1 = Schedule(immunization=im, patient=instance)
         m1.save()


class Schedule(models.Model):
    immunization = models.ForeignKey(Immunization, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    administered = models.BooleanField(default = False)
    date_of_admin = models.DateField(default = '1900-01-01')

    def __str__(self):
        return self.patient.__str__() + ' - ' + self.immunization.name


# Create your models here.
