from django.db import models


class Facility(models.Model):
    name = models.CharField(max_length=180)
    code = models.CharField(max_length=32, unique=True)
    district = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Patient(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        REVIEW = 'review', 'Review'
        INACTIVE = 'inactive', 'Inactive'

    healthgrid_id = models.CharField(max_length=32, unique=True)
    given_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    registered_facility = models.ForeignKey(Facility, on_delete=models.PROTECT, related_name='registered_patients')
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        ordering = ['family_name', 'given_name']

    def __str__(self):
        return f'{self.given_name} {self.family_name}'


class Referral(models.Model):
    class Priority(models.TextChoices):
        HIGH = 'high', 'High'
        MEDIUM = 'medium', 'Medium'
        ROUTINE = 'routine', 'Routine'

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending acceptance'
        IN_PROGRESS = 'in_progress', 'In progress'
        COMPLETED = 'completed', 'Completed'

    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='referrals')
    origin = models.ForeignKey(Facility, on_delete=models.PROTECT, related_name='outgoing_referrals')
    destination = models.ForeignKey(Facility, on_delete=models.PROTECT, related_name='incoming_referrals')
    specialty = models.CharField(max_length=120)
    priority = models.CharField(max_length=16, choices=Priority.choices, default=Priority.ROUTINE)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.patient.healthgrid_id}: {self.origin} -> {self.destination}'
