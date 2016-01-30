from django.conf.urls import patterns, include, url

from .views import user_profile, users, index, login_view, signup, submit, logout_view

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index), # root
    url(r'^login$', login_view), # login
    url(r'^logout$', logout_view), # logout
    url(r'^signup$', signup), # signup
#     url(r'^footprint/$', 'apps.views.footprint'), # road safety foot print
    url(r'^submit$', submit), # s
    url(r'^users/$', users),
    url(r'^users/(?P<username>\w{0,30})/$', users),
    url(r'^user_profile/(?P<username>\w{0,30})/$', user_profile),
    url(r'^user_profile/$', user_profile),
#     url(r'^vehicle_owner/$', 'apps.views.vehicle_owner'),
#     url(r'^vehicle_lov/$', 'apps.views.vehicle_lov'),
#     url(r'^infridgement_lov/$', 'apps.views.infridgement_lov'),
#     url(r'^people_lov/$', 'apps.views.people_lov'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
)