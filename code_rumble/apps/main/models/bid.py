from django.db import models

from .job import Job
from .user_profile import UserProfile


class Bid(models.Model):

    '''
    This model describes the bids that companies are making against a job.
    '''

    job = models.ForeignKey(Job)

    user_profile = models.ForeignKey(UserProfile)

    bidding_amount = models.DecimalField(
        verbose_name='Amount in Pula',
        max_digits=10,
        decimal_places=2
    )
