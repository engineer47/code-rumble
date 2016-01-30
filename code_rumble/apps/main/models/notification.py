from django.db import models

from .user_profile import UserProfile


class Notification(models.Model):

    '''
    This model keeps record of all the notifications sent to all the users.
    '''

    user_profile = models.ForeignKey(UserProfile)

    message_to = models.CharField(
        verbose_name='Recipient: ',
        max_length=50,
        unique=True,
    )

    message_from = models.CharField(
        verbose_name='Sender: ',
        max_length=50,
        unique=True,
    )

    subject = models.CharField(
        verbose_name='Subject',
        max_length=25,
    )

    message = models.CharField(
        verbose_name='Message: ',
        max_length=5000,
    )

    class Meta:
        app_label = 'main'

