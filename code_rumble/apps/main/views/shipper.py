import json

from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http.response import HttpResponse
from .job_datatable_view import JobDatatableView


class Shipper(View):

    def __init__(self):
        self.context = {}
        self.template_name = 'shipper.html'
        self.title = 'This is Home'

    def get(self, request, *args, **kwargs):
        notifications = 'Notifications.objects.all()'
        self.context.update({
            'title': self.title,
            'notifications': notifications,
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def get_context_data(self, **kwargs):
        return super(Shipper, self).get_context_data(**kwargs)


def create_get(request):
    if request.method == 'GET':
        post_text = request.GET.get('job_type')
        response_data = dict({"job_type": "My Job"})
        print "Ihfdashfdsajkgfakgfasgkfkg", request.GET

#         post = Post(text=post_text, author=request.user)
#         post.save()

#         response_data['result'] = 'Create post successful!'
#         response_data['postpk'] = post.pk
#         response_data['text'] = post.text
#         response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
#         response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        #post_text = request.GET.get('job_type')
        response_data = dict({"job_type": "My Job"})
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
