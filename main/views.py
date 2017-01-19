from django.shortcuts import render,redirect
import requests
import datetime
from dateutil.relativedelta import relativedelta
from main.models import Immunization,Patient,Schedule
from main.forms import PatientForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

# Create your views here.
def intro(request):
    timeNow = datetime.datetime.strptime(request.session['dob'], "%Y-%m-%d").date()
    dateFormat = "%d %b, %Y"
    immun = Immunization.objects.filter(patient__dob = request.session['dob'],patient__last_name = request.session['lname'],duration_in = 'month').order_by('duration_from')
    immun_list = list(immun)
    immun = Immunization.objects.filter(patient__dob = request.session['dob'],patient__last_name = request.session['lname'],duration_in = 'year').order_by('duration_from')
    immun_list += list(immun)
    pat = Patient.objects.filter(dob=request.session['dob'],last_name = request.session['lname'])

    for im in immun_list:
        if im.duration_in == 'month':
            im.duration_from_date = timeNow + relativedelta(months=im.duration_from)
            im.duration_from_date = im.duration_from_date.strftime(dateFormat)
            im.duration_to_date = timeNow + relativedelta(months=im.duration_to)
            im.duration_to_date = im.duration_to_date.strftime(dateFormat)
            sched = Schedule.objects.filter(patient=pat,immunization=im)[0]
            im.admin = sched.administered
            im.date_admin = sched.date_of_admin.strftime(dateFormat)

        if im.duration_in == 'year':
            im.duration_from_date = timeNow + relativedelta(years=im.duration_from)
            im.duration_from_date = im.duration_from_date.strftime(dateFormat)
            im.duration_to_date = timeNow + relativedelta(years=im.duration_to)
            im.duration_to_date = im.duration_to_date.strftime(dateFormat)
            sched = Schedule.objects.filter(patient=pat,immunization=im)[0]
            im.admin = sched.administered
            im.date_admin = sched.date_of_admin.strftime(dateFormat)
    return render(request,'intro.html',{
                'data' : immun_list
                })

def entry(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            if Patient.objects.filter(first_name = form.cleaned_data['fname'], last_name = form.cleaned_data['lname'], dob = form.cleaned_data['dob']).exists():
                request.session['lname'] = form.cleaned_data['lname']
                request.session['dob'] = str(form.cleaned_data['dob'])
                return HttpResponseRedirect('/detail/')
            else:
                pat = Patient()
                pat.first_name = form.cleaned_data['fname']
                pat.last_name = form.cleaned_data['lname']
                pat.dob = form.cleaned_data['dob']
                pat.save()
                request.session['lname'] = pat.last_name
                request.session['dob'] = str(pat.dob)
                return HttpResponseRedirect('/detail/')
    else:
        form = PatientForm()

    return render(request, 'entry.html', {'form': form})

def trial(request,id):
    immun = Immunization.objects.get(id=id)
    d = datetime.datetime.strptime(request.session['dob'], "%Y-%m-%d").date()
    pat = Patient.objects.filter(dob=request.session['dob'],last_name = request.session['lname'])
    sc = Schedule.objects.get(immunization=immun,patient=pat)
    sc.administered = True;
    sc.date_of_admin = request.POST.get("date_admin","")
    sc.save()
    return HttpResponseRedirect('/detail/')
