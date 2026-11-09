from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Facility, Patient, Referral
from .serializers import FacilitySerializer, PatientSerializer, ReferralSerializer


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.filter(is_active=True)
    serializer_class = FacilitySerializer
    permission_classes = [IsAuthenticated]


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.select_related('registered_facility').all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['healthgrid_id', 'given_name', 'family_name']
    filterset_fields = ['status', 'registered_facility']


class ReferralViewSet(viewsets.ModelViewSet):
    queryset = Referral.objects.select_related('patient', 'origin', 'destination').all()
    serializer_class = ReferralSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['status', 'priority', 'origin', 'destination']
