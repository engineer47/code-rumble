from django.test.testcases import TestCase
from django.core.exceptions import ValidationError

from ..models import Job, Bid
from ..constants import NEW, IN_PROGRESS, SHIPPER, INDIVIDUAL, UNDER_CONSIDERATION, ACCEPTED, REJECTED
from .factories import UserProfileFactory


class TestJobManagement(TestCase):

    def setUp(self):
        pass

    def test_individual_submit_job(self):
        individual = UserProfileFactory(account=INDIVIDUAL)
        job_options = {'weight': 300.00}
        individual.create_job(job_options)
        self.assertEqual(Job.objects.filter(sumbittor__user__username=individual.user.username,
                                            job_status=NEW).count(), 1)
        exercutor = UserProfileFactory(account=SHIPPER)
        with self.assertRaises(ValidationError):
            individual.create_job(exercutor)

    def test_directly_assign_job_to_shipper(self):
        individual = UserProfileFactory(account=INDIVIDUAL)
        job_options = {}
        individual.create_job(job_options)
        job = Job.objects.get(sumbittor__user__username=individual.user.username,
                              job_status=NEW)
        exercutor = UserProfileFactory(account=SHIPPER)
        job.assign_job(exercutor)
        self.assertEqual(Job.objects.filter(exercutor__user__username=exercutor.user.username,
                         job_status=IN_PROGRESS).count(), 1)
        with self.assertRaises(ValidationError):
            job.assign_job(individual)

    def test_multiple_shipper_bids_for_job(self):
        individual = UserProfileFactory(account=INDIVIDUAL)
        job_options = {}
        individual.create_job(job_options)
        job = Job.objects.get(sumbittor__user__username=individual.user.username,
                              job_status=NEW)
        exercutor1 = UserProfileFactory(account=SHIPPER)
        exercutor1.submit_bid(job, 200)
        self.assertEqual(Bid.objects.filter(job=job, bid_owner=exercutor1,
                                            bid_status=UNDER_CONSIDERATION, expired=False).count(), 1)
        exercutor2 = UserProfileFactory(account=SHIPPER)
        exercutor2.submit_bid(job, 200)
        self.assertEqual(Bid.objects.filter(job=job, bid_owner=exercutor2,
                                            bid_status=UNDER_CONSIDERATION, expired=False).count(), 1)

    def test_individual_accepts_bid(self):
        individual = UserProfileFactory(account=INDIVIDUAL)
        job_options = {}
        individual.create_job(job_options)
        job = Job.objects.get(sumbittor__user__username=individual.user.username,
                              job_status=NEW)
        exercutor1 = UserProfileFactory(account=SHIPPER)
        exercutor1.submit_bid(job, 200)
        exercutor2 = UserProfileFactory(account=SHIPPER)
        exercutor2.submit_bid(job, 200)
        bid = Bid.objects.get(job=job, bid_owner=exercutor2, status=NEW, expired=False)
        individual.accept_bid(bid)
        self.assertEqual(Bid.objects.filter(job=job, bid_owner=exercutor2,
                                            bid_status=ACCEPTED, expired=False).count(), 1)

    def test_unaccepted_bid_automatically_rejected(self):
        individual = UserProfileFactory(account=INDIVIDUAL)
        job_options = {}
        individual.create_job(job_options)
        job = Job.objects.get(sumbittor__user__username=individual.user.username,
                              job_status=NEW)
        exercutor1 = UserProfileFactory(account=SHIPPER)
        exercutor1.submit_bid(job, 200)
        exercutor2 = UserProfileFactory(account=SHIPPER)
        exercutor2.submit_bid(job, 200)
        exercutor3 = UserProfileFactory(account=SHIPPER)
        exercutor3.submit_bid(job, 200)
        bid = Bid.objects.get(job=job, bid_owner=exercutor2, expired=False)
        individual.accept_bid(bid)
        self.assertEqual(Bid.objects.filter(job=job, bid_owner=exercutor2,
                                            bid_status=ACCEPTED, expired=False).count(), 1)
        for bid_item in Bid.objects.filter(job=job).exclude(bid_status=ACCEPTED):
            self.assertEqual(bid_item.bid_status, REJECTED)

    def test_rejected_bid_cannot_bid_again(self):
        pass

    def test_job_in_progress(self):
        pass

