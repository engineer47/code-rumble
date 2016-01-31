from django.db import models

from ..constants import NEW, UNDER_CONSIDERATION, REJECTED
from .job import Job
from .user_profile import UserProfile


class Bid(models.Model):

    '''
    This model describes the bids that companies are making against a job.
    '''

    job = models.ForeignKey(Job)

    bid_owner = models.ForeignKey(UserProfile)

    bid_status = models.CharField(
        verbose_name='Bid Status',
        max_length=20,
        default=NEW,
    )

    bidding_amount = models.DecimalField(
        verbose_name='Amount in Pula',
        max_digits=10,
        decimal_places=2
    )

    expired = models.BooleanField(default=False)

    class Meta:
        app_label = 'main'
