from django.contrib import admin
from .models import Immunization,Patient, Schedule



class ImmunizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'dose_no', 'duration_from','duration_to','duration_in']
    class Meta:
		model = Immunization


admin.site.register(Immunization,ImmunizationAdmin)
admin.site.register(Patient)
admin.site.register(Schedule)
# Register your models here.
