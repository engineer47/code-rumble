from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.views.index'), # root
    url(r'^login$', 'apps.views.login_view'), # login
    url(r'^logout$', 'apps.views.logout_view'), # logout
    url(r'^signup$', 'apps.views.signup'), # signup
#     url(r'^footprint/$', 'apps.views.footprint'), # road safety foot print
    url(r'^submit$', 'apps.views.submit'), # s
    url(r'^users/$', 'apps.views.users'),
    url(r'^users/(?P<username>\w{0,30})/$', 'apps.views.users'),
    url(r'^user_profile/(?P<username>\w{0,30})/$', 'apps.views.user_profile'),
    url(r'^user_profile/$', 'apps.views.user_profile'),
#     url(r'^vehicle_owner/$', 'apps.views.vehicle_owner'),
#     url(r'^vehicle_lov/$', 'apps.views.vehicle_lov'),
#     url(r'^infridgement_lov/$', 'apps.views.infridgement_lov'),
#     url(r'^people_lov/$', 'apps.views.people_lov'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
)