from django import forms
from django.forms import ModelForm
from main.models import Patient
from django.contrib.admin.widgets import AdminDateWidget

class PatientForm(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()
    dob = forms.DateField(widget = forms.SelectDateWidget(years=range(1940, 2017)))
