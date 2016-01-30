import hashlib
from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from ..constants import INDIVIDUAL, SHIPPER, UNDER_CONSIDERATION, ACCEPTED, REJECTED
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
            raise ValidationError('Only INDIVIDUAL accounts can submit jobs. This is a "{}" account'.format(SHIPPER))

    def submit_bid(self, job, amount):
        Bid = models.get_model('main', 'Bid')
        if self.account == SHIPPER:
            Bid.objects.create(bid_owner=self, job=job, bidding_amount=amount, bid_status=UNDER_CONSIDERATION)
        else:
            raise ValidationError('Only SHIPPER accounts can submit bids against jobs. This is a "{}" account'.format(
                INDIVIDUAL))

    def accept_bid(self, bid):
        Bid = models.get_model('main', 'Bid')
        if self.account == INDIVIDUAL:
            bid.bid_status = ACCEPTED
            bid.save()
            for other_bid in Bid.objects.filter(job=bid.job).exclude(id=bid.id):
                other_bid.bid_status = REJECTED
                other_bid.save()
        else:
            raise ValidationError('Only SHIPPER accounts can submit bids against jobs. This is a "{}" account'.format(
                SHIPPER))

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()

    class Meta:
        app_label = 'main'

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
