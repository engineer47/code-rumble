import json
from datetime import datetime
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count, Q
from django.db import transaction
from django.http import HttpResponseRedirect
from django.http import Http404
from ..forms import (AuthenticateForm, UserCreateForm, UserProfileForm)
from ..models import UserProfile

def get_latest(user):
    try:
        return user.ribbit_set.order_by('-id')[0]
    except IndexError:
        return ""
 
@login_required
def users(request, username="", ribbit_form=None):
    if username:
        # Show a profile
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        ribbits = Ribbit.objects.filter(user=user.id)
        if username == request.user.username or request.user.profile.follows.filter(user__username=username):
            # Self Profile or buddies' profile
            return render(request, 'user.html', {'user': user, 'ribbits': ribbits, })
        return render(request, 'user.html', {'user': user, 'ribbits': ribbits, 'follow': True, })
    users = User.objects.all().annotate(ribbit_count=Count('ribbit'))
    ribbits = map(get_latest, users)
    obj = zip(users, ribbits)
    ribbit_form = ribbit_form or LeoForm()
    return render(request,
                  'profiles.html',
                  {'obj': obj, 'next_url': '/users/',
                   'ribbit_form': ribbit_form,
                   'username': request.user.username, })

@login_required
def user_profile(request, username=None):
    user_profile = UserProfile.objects.get(user=request.user)
    my_people = user_profile.linked_to.through.objects.all()
    #my_people = []
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            updated_user_values = {}
            updated_profile_values = {}
            for fld in UserProfileForm.Meta.fields:
                updated_user_values[fld] = form.cleaned_data.get(fld)
            for fld in UserProfileForm.Meta.profile_fields:
                updated_profile_values[fld] = form.cleaned_data.get(fld)
            User.objects.filter(id=request.user.id).update(**updated_user_values)
            UserProfile.objects.filter(user=request.user).update(**updated_profile_values)
            # TODO: search cars by registration not model name.
            updated_vehicles = []
            for key, value in request.POST.iteritems():
                if key.find('car') != -1:
                    updated_vehicles.append(value)
            # release all vehicles previously attached to this profile
            Vehicle.objects.filter(owner=user_profile).update(owner=None)
            # attach the updated list of vehicles to this profile
            Vehicle.objects.filter(model__in=updated_vehicles).update(owner=user_profile)

            # TODO: search People by omang-ID not firstname and lastname.
            updated_people = []
            for key, value in request.POST.iteritems():
                if key.find('per') != -1:
                    updated_people.append(value)
            # release all other users previously linked to this profile
            UserProfile.objects.get(user__username=request.user.username).linked_to.clear()
            # link the updated list of users to this profile
            for name in updated_people:
                first_name, surname = name.split('.')
                named_user = UserProfile.objects.get(user__first_name=first_name, user__last_name=surname)
                user_profile.linked_to.add(named_user)
            my_people = user_profile.linked_to.through.objects.all()
            return HttpResponseRedirect('/user_profile/{}/'.format(form.cleaned_data.get('username')))
    else:
        #user = request.GET.get('username')
        print request.GET
        user_profile = UserProfile.objects.get(user__username=username)
        form_values = {}
        for fld in UserProfileForm.Meta.fields:
            form_values[fld] = user_profile.user.__dict__[fld]
        for fld in UserProfileForm.Meta.profile_fields:
            form_values[fld] = user_profile.__dict__[fld]
        form = UserProfileForm(form_values)

    return render(request, 
                  'profiles.html', 
                  {'form': form,
                   'vehicles': Vehicle.objects.all(),
                   'my_vehicles': Vehicle.objects.filter(owner=user_profile),
                   'people': UserProfile.objects.all().exclude(user__username=request.user.username).exclude(
                                                               user__in=my_people),
                   'my_people': my_people,
                   'username': request.user.username, })


# def vehicle_lov(request):
#     return render(request, 
#                   'vehicle_lov.html',
#                   {'vehicles': Vehicle.objects.all()})
# 
# 
# def people_lov(request):
#     return render(request,
#                   'people_lov.html',
#                   {'people': UserProfile.objects.all()})
# 
# def infridgement_lov(request):
#     return render(request, 
#                   'infridgement_lov.html',
#                   {'infridgements': Infridgement.objects.all()})


def index(request, auth_form=None, user_form=None):
    # User is logged in
    if request.user.is_authenticated():
#         ribbit_form = LeoForm()
        user = request.user
        model = ''
#         registration = ''
#         ribbits_self = Ribbit.objects.filter(user=user.id)
#         my_notifications = None
#         my_vehicles = []
#         #ribbits_buddies = Ribbit.objects.filter(user__userprofile__in=user.profile.follows.all)
#         #ribbits = ribbits_self | ribbits_buddies
#         my_vehicles = Vehicle.objects.filter(owner__user__username=request.user.username)
#         user_profile = UserProfile.objects.get(user=request.user)
#         my_people = user_profile.linked_to.through.objects.all()
#         my_people_usernames = [person.to_userprofile.user.username for person in my_people]
#         my_notifications = Notification.objects.filter(Q(sighting__human__user__username__in=my_people_usernames) |
#                                                            Q(sighting__vehicle__in=my_vehicles)).order_by('-notification_datetime')
#         if request.method == 'POST':
#             # All POST data will contain a value for sighting
#             sighting_type = request.POST.get('sighting')
#             if sighting_type == 'vehicle':
#                 form = VehicleSightingForm(request.POST)
#             elif sighting_type == 'human':
#                 form = HumanSightingForm(request.POST)
#             elif sighting_type == 'infrastructure':
#                 form = InfrastructureSightingForm(request.POST)
#             else:
#                 sighting_type = '------'
#             # check whether it's valid:
#             if form.is_valid():
#                 if sighting_type == 'vehicle':
#                     car = Vehicle.objects.get(registration=form.cleaned_data.get('registration'))
#                     infridgement = Infridgement.objects.get(code=form.cleaned_data.get('infridgement_code'))
#                     longitude = form.cleaned_data.get('longitude')
#                     latitude = form.cleaned_data.get('latitude')
#                     Sighting.objects.create(vehicle=car, infridgement=infridgement, longitude=longitude,
#                                             latitude=latitude, sighting_datetime=datetime.now())
#                 elif sighting_type == 'human':
#                     name = form.cleaned_data.get('human_name')
#                     first_name, surname = name.split('.')
#                     human = UserProfile.objects.get(user__first_name=first_name, user__last_name=surname)
#                     infridgement = Infridgement.objects.get(code=form.cleaned_data.get('infridgement_code'))
#                     longitude = form.cleaned_data.get('longitude')
#                     latitude = form.cleaned_data.get('latitude')
#                     Sighting.objects.create(human=human, infridgement=infridgement, longitude=longitude,
#                                             latitude=latitude, sighting_datetime=datetime.now())
#                 #msg = "Sucessfully registered a sighting agains vehicle registered {}".format(car.registration)
#                 #messages.add_message(request, messages.INFO, msg)
#         # What if the method is a get?
#         else:
#             sighting_type = '------'
        return render(request,
                      'buddies.html',
                      {#'ribbit_form': ribbit_form, 
                       'user': user,
                       'model': model,
                       'registration': [],
                       'sighting_type': [],
                       'notifications': [],
                       'public_notifications': [],
                       'next_url': '/',
                       'username': request.user.username,  })
    else:
        # User is not logged in
        auth_form = auth_form or AuthenticateForm()
        user_form = user_form or UserCreateForm()

        return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form, })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid() and UserProfile.objects.filter(user__username=request.POST.get('username'), validated=True):
            login(request, form.get_user())
            # Success
            return redirect('/shipper')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')


def verify_account(request, username):
    try:
        user_profile = UserProfile.objects.get(user__username=username)
        user_profile.validated = True
        user_profile.save()
        message = "Congratulations '{}', your account has been verified.".format(user_profile.user.first_name)
    except UserProfile.DoesNotExist:
        message = "The username '{}' does not exist in the system. Please register first.".format(username)
    return render(request,
                    'verify.html',
                    {'message': message
                     })

def signup(request):
    user_form = UserCreateForm(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            with transaction.atomic():
                user_form.save()
                user = user_form.instance
                form_values = {}
                for fld in UserCreateForm.Meta.profile_fields:
                    form_values[fld] = user_form.cleaned_data[fld]
                form_values['user'] = user
                UserProfile.objects.create(**form_values)
                subject = "verify account (BW shipping portal)"
                body = 'Thank you for registering with BW shipping portal ' \
                        'click the following link to verify your email.' \
                        'http://localhost:8000/verify/{}'.format(user.username)
                email_sender = "coderumble2016@gmail.com"
                recipient_list = [user.email, ]
                send_mail(subject, body, email_sender, recipient_list, fail_silently=False)
                return redirect('/')
        else:
            return index(request, user_form=user_form)
    return redirect('/')

# @login_required
# def public(request, ribbit_form=None):
#     ribbit_form = ribbit_form or LeoForm()
#     ribbits = Ribbit.objects.reverse()[:10]
#     return render(request,
#                    'public.html',
#                    {'ribbit_form': ribbit_form, 'next_url': '/ribbits',
#                     'ribbits': ribbits, 'username': request.user.username})

