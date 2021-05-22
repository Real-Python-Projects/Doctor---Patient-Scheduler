from django.contrib import admin
from .models import Appointment, Doctor

admin.site.site_title = "Ceder Court Interview"
admin.site.site_header = "Ceder Court Interview"

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'date', 'timeslot', 'patient_name']
    list_filter = ['doctor', ]

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Doctor)
