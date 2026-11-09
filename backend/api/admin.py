from django.contrib import admin
from .models import Facility, Patient, Referral


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'district', 'is_active']
    search_fields = ['name', 'code', 'district']


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['healthgrid_id', 'family_name', 'given_name', 'registered_facility', 'status']
    search_fields = ['healthgrid_id', 'given_name', 'family_name']
    list_filter = ['status', 'registered_facility']


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ['patient', 'origin', 'destination', 'priority', 'status', 'created_at']
    list_filter = ['priority', 'status', 'origin', 'destination']
