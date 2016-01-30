import hashlib
from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from ..constants import INDIVIDUAL, SHIPPER
from .company import Company


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    mobile = models.CharField(max_length=10)
    validated = models.BooleanField(default=False)
    account = models.CharField(max_length=10)
    company = models.ForeignKey(Company, null=True)

    def create_job(self, options):
        Job = models.get_model('main', 'Job')
        if self.account == INDIVIDUAL:
            Job.objects.create(sumbittor=self, **options)
        else:
            raise ValidationError('Only INDIVIDUAL accounts can sumit jobs. This is a "{}" account'.format(SHIPPER))

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()

    class Meta:
        app_label = 'main'

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
