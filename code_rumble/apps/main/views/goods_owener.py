from django.shortcuts import render_to_response
from django.template import RequestContext
from .base_dashboard import BaseDashboard

from ..models import Job
from ..forms import JobForm
from ..constants import NEW, IN_PROGRESS, ACCEPTED, ASSIGNED, COMPLETED
from code_rumble.apps.main.models.user_profile import UserProfile
from code_rumble.apps.main.choices import ACCOUNT_TYPE


class GoodsOwner(BaseDashboard):

    def __init__(self):
        self.context = {}
        self.template_name = 'owner_job_bids.html'
        super(GoodsOwner, self).__init__()

    def get(self, request, *args, **kwargs):
        public_jobs = Job.objects.filter(job_status__in=[NEW])
        task = kwargs.get('task_id', '1')
        job = kwargs.get('task_id', '1')
        if task == '1':
            self.template_name = 'owner_job_bids.html'
        elif task == '2':
            self.template_name = 'job_assignment.html'
        elif task == '3':
            self.template_name = 'add_job.html'
        elif task == '4':
            self.template_name = 'job_form.html'
        job_form = JobForm()
        my_jobs = Job.objects.filter(sumbittor__user__username=request.user.username)
#         for job in Job.objects.all():
#             print job.sumbittor.user.username
        print request.user.username
        truck_plan_coordinates = [
            [-24.619168, 25.934612],
            [-24.378842, 26.062498],
            [-24.348581, 26.086359],
            [-24.025998, 26.317072],
            [-23.146262, 26.819975],
            [-21.949307, 27.301839],
            [-21.179817, 27.510579]
        ]
        destination = [-21.179817, 27.510579]
        self.context.update({
            'title': self.title,
            'public_jobs': public_jobs,
            'my_jobs': my_jobs,
            'truck_plan_coordinates': truck_plan_coordinates,
            'coordinates_list_len': len(truck_plan_coordinates),
            'job_bids_id': 1,
            'assign_job_id': 2,
            'add_job_id': 3,
            'job_form_id': 4,
            'destination': destination,
            'job_form': job_form,
            'shippers': self.shippers(),
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def shippers(self):
        return UserProfile.objects.filter(account=ACCOUNT_TYPE[0][0])

    def post(self, request, *args, **kwargs):

        job_form = JobForm(request.POST)
        if job_form.is_valid():
            job_form.save()
        public_jobs = Job.objects.filter(job_status__in=[NEW])
        task = kwargs.get('task_id', '1')
        job = kwargs.get('task_id', '1')
        if task == '1':
            self.template_name = 'owner_job_bids.html'
        elif task == '2':
            self.template_name = 'job_assignment.html'
        elif task == '3':
            self.template_name = 'add_job.html'
        elif task == '4':
            self.template_name = 'job_form.html'
        job_form = JobForm()
        my_jobs = Job.objects.filter(sumbittor__user__username=request.user.username, job_status__in=[NEW])
        truck_plan_coordinates = [
            [-24.619168, 25.934612],
            [-24.378842, 26.062498],
            [-24.348581, 26.086359],
            [-24.025998, 26.317072],
            [-23.146262, 26.819975],
            [-21.949307, 27.301839],
            [-21.179817, 27.510579]
        ]
        destination = [-21.179817, 27.510579]
        self.context.update({
            'title': self.title,
            'public_jobs': public_jobs,
            'my_jobs': my_jobs,
            'truck_plan_coordinates': truck_plan_coordinates,
            'coordinates_list_len': len(truck_plan_coordinates),
            'job_bids_id': 1,
            'assign_job_id': 2,
            'add_job_id': 3,
            'job_form_id': 4,
            'destination': destination,
            'job_form': job_form,
            'shippers': self.shippers(),
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def get_context_data(self, **kwargs):
        return super(GoodsOwner, self).get_context_data(**kwargs)
