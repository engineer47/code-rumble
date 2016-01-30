from django.db import models

from .payment import Payment


class Job(models.Model):

    """
    This model describes the job and its details.
    """
    payment = models.ForeignKey(Payment)

    name = models.CharField(
        verbose_name='Name',
        max_length=25,
        unique=True,
    )

    weight = models.DecimalField(
        verbose_name='Weight of the Cargo',
        max_digits=6,
        decimal_places=4,
    )

    insurance = models.CharField(
        verbose_name='Insurance',
        max_length=25,
        unique=False,
        blank=True
    )
