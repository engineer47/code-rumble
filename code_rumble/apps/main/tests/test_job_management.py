from django.test.testcases import TestCase
from django.core.exceptions import ValidationError

from ..models import Job
from ..constants import NEW, IN_PROGRESS, SHIPPER, INDIVIDUAL
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
        pass

    def test_individual_accepts_bid(self):
        pass

    def test_individual_rejects_bid(self):
        pass

    def test_rejected_bid_cannot_bid_again(self):
        pass

    def test_job_in_progress(self):
        pass
    
