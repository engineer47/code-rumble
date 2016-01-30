from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext


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
