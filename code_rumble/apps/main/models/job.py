import uuid
from django.db import models

from .payment import Payment
from .user_profile import UserProfile

from ..constants import NEW
from ..choices import JOB_STATUS


class Job(models.Model):

    """
    This model describes the job and its details.
    """

    payment = models.ForeignKey(Payment, null=True)

    sumbittor = models.ForeignKey(UserProfile)

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

    def save(self, *args, **kwargs):
        if not self.id:
            self.job_identifier = str(uuid.uuid4())
        super(Job, self).save(*args, **kwargs)

    class Meta:
        app_label = 'main'
