from django.db import models

from ..choices import PAYMENT_MODE, PAYMENT_STATUS, BANK

from .user_profile import UserProfile


class AccountDetails(models.Model):

    '''
    Account details keeps record of the user's account details.
    '''

    user_profile = models.ForeignKey(UserProfile)

    account_number = models.CharField(
        verbose_name='Account Number',
        max_length=25,
        unique=True,
        null=False,
    )

    institution = models.CharField(
        verbose_name='Institution name',
        choices=BANK,
        max_length=25,
        null=False,
    )

    payment_mode = models.CharField(
        verbose_name='Payment mode',
        max_length=25,
        choices=PAYMENT_MODE,
    )

    payment_status = models.CharField(
        verbose_name='Payment Status',
        max_length=25,
        choices=PAYMENT_STATUS,
    )

    class Meta:
        app_label = 'main'
