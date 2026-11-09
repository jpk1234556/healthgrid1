from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Patient, Referral


class HealthCheckView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'status': 'ok', 'service': 'healthgrid-api', 'version': '0.1.0'})


class OverviewView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = timezone.localdate()
        active_referrals = Referral.objects.filter(
            status__in=[Referral.Status.PENDING, Referral.Status.IN_PROGRESS]
        )
        return Response({
            'patients_total': Patient.objects.count(),
            'referrals_active': active_referrals.count(),
            'referrals_pending': active_referrals.filter(status=Referral.Status.PENDING).count(),
            'referrals_in_progress': active_referrals.filter(status=Referral.Status.IN_PROGRESS).count(),
            'referrals_completed_today': Referral.objects.filter(
                status=Referral.Status.COMPLETED, created_at__date=today
            ).count(),
        })
