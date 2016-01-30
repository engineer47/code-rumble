from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import hashlib
from code_rumble.apps.main.choices import SENDING_METHODS

from .company import Company


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    mobile = models.CharField(max_length=10)
    validated = models.BooleanField(default=False)
    account = models.CharField(max_length=10)
    company = models.ForeignKey(Company, null=True)

    def create_job(self, options):
        Job = models.get_model('main', 'Job')
        try:
            Job.objects.get(sumbittor=self)
        except Job.DoesNotExist:
            Job.objects.create(sumbittor=self, **options)

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()

    class Meta:
        app_label = 'main'

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
