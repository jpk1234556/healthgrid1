from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import HealthCheckView, OverviewView
from .viewsets import FacilityViewSet, PatientViewSet, ReferralViewSet

router = DefaultRouter()
router.register('facilities', FacilityViewSet)
router.register('patients', PatientViewSet)
router.register('referrals', ReferralViewSet)

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health-check'),
    path('overview/', OverviewView.as_view(), name='overview'),
    path('', include(router.urls)),
]
