from django.db import models

from .user_profile import UserProfile
from .account_details import AccountDetails


class Payment(models.Model):

    '''
    The payment model maintains a records of all the payments
    '''

    user_profile = models.ForeignKey(UserProfile)

    account_details = models.ForeignKey(AccountDetails)

    amount = models.DecimalField(
        verbose_name='Amount in Pula',
        max_digits=10,
        decimal_places=2,
    )
