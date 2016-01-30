from django.conf.urls import patterns, url

from code_rumble.apps.main.views.user_login import user_profile, users, index, login_view, signup, submit, logout_view
from code_rumble.apps.main.views import Shipper

urlpatterns = patterns(
    '',
    url(r'^$', index),
    url(r'^login$', login_view),
    url(r'^logout$', logout_view),
    url(r'^signup$', signup),
    url(r'^submit$', submit),
    url(r'^users/$', users),
    url(r'^users/(?P<username>\w{0,30})/$', users),
    url(r'^user_profile/(?P<username>\w{0,30})/$', user_profile),
    url(r'^user_profile/$', user_profile),
    url(r'shipper^$', Shipper.as_view(), name='shipper_url'),
)

urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve'),
)
