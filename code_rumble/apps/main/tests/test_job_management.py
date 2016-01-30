from django.test.testcases import TestCase

from ..models import Job
from ..constans import NEW
from ..choices import ACCOUNT_TYPE
from .factories import UserProfileFactory


class TestConfiguration(TestCase):

    def setUp(self):
        pass

    def test_individual_submit_job(self):
        individual = UserProfileFactory(account=ACCOUNT_TYPE[0][1])
        job_options = {}
        individual.create_job(job_options)
        self.assertEqual(Job.objects.filter(sumbittor__user__user_name=individual.user.username,
                                            job_status=NEW))