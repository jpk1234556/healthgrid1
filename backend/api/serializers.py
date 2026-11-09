from rest_framework import serializers
from .models import Facility, Patient, Referral


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ['id', 'name', 'code', 'district', 'is_active']


class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    registered_facility_name = serializers.CharField(source='registered_facility.name', read_only=True)

    class Meta:
        model = Patient
        fields = [
            'id', 'healthgrid_id', 'given_name', 'family_name', 'full_name',
            'date_of_birth', 'registered_at', 'registered_facility',
            'registered_facility_name', 'status',
        ]
        read_only_fields = ['registered_at']

    def get_full_name(self, obj):
        return f'{obj.given_name} {obj.family_name}'


class ReferralSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()
    origin_name = serializers.CharField(source='origin.name', read_only=True)
    destination_name = serializers.CharField(source='destination.name', read_only=True)

    class Meta:
        model = Referral
        fields = [
            'id', 'patient', 'patient_name', 'origin', 'origin_name',
            'destination', 'destination_name', 'specialty', 'priority',
            'status', 'created_at', 'accepted_at',
        ]
        read_only_fields = ['created_at']

    def get_patient_name(self, obj):
        return str(obj.patient)
