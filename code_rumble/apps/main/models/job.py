import uuid
from django.db import models
from django.core.exceptions import ValidationError

from .payment import Payment
from .user_profile import UserProfile

from ..constants import NEW, INDIVIDUAL, SHIPPER, IN_PROGRESS
from ..choices import JOB_STATUS


class Job(models.Model):

    """
    This model describes the job and its details.
    """

    payment = models.ForeignKey(Payment, null=True)

    sumbittor = models.ForeignKey(UserProfile, related_name='profile_sumbittor')

    exercutor = models.ForeignKey(UserProfile, null=True)

    job_identifier = models.CharField(
        verbose_name='Job Identifier',
        default=None,
        max_length=36,
        unique=True,
        editable=False
    )

    job_status = models.CharField(
        verbose_name='Job Status',
        max_length=10,
        default=NEW,
        choices=JOB_STATUS,
    )

    weight = models.DecimalField(
        verbose_name='Weight of the Cargo',
        max_digits=6,
        decimal_places=4,
        null=True,
        blank=True
    )

    insurance = models.CharField(
        verbose_name='Insurance',
        max_length=25,
        null=True,
        blank=True
    )

    def assign_job(self, exercutor):
        if exercutor.account == SHIPPER:
            self.exercutor = exercutor
            self.job_status = IN_PROGRESS
            self.save()
        else:
            raise ValidationError('Only SHIPPER accounts can exercute jobs. This is a "{}" account'.format(INDIVIDUAL))

    def save(self, *args, **kwargs):
        if not self.id:
            self.job_identifier = str(uuid.uuid4())
        super(Job, self).save(*args, **kwargs)

    class Meta:
        app_label = 'main'
