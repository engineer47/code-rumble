from django.conf.urls import patterns, url

from code_rumble.apps.main.views.user_login import (user_profile, users, login_view, signup, logout_view,
                                                    verify_account)
from code_rumble.apps.main.views import Shipper, AddBid, ViewBids, create_get
from code_rumble.apps.main.views import Shipper, create_get, GoodsOwner

from .views import Home


urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home_url'),
    url(r'^login$', login_view),
    url(r'^logout$', logout_view),
    url(r'^signup$', signup),
    url(r'^users/$', users),
    url(r'^verify/(?P<username>\w{0,30})$', verify_account),
    url(r'^users/(?P<username>\w{0,30})/$', users),
    url(r'^user_profile/(?P<username>\w{0,30})/$', user_profile, name='user_profile'),
    url(r'^user_profile/$', user_profile),
    url(r'shipper$', Shipper.as_view(), name='shipper_url'),
    url(r'add_bid', AddBid.as_view(), name='submit_bid_url'),
    url(r'view_bids', ViewBids.as_view(), name='view_bids_url'),
    url(r'^goods_owner/(?P<task_id>[1-9]{1})$', GoodsOwner.as_view(), name='goods_owner_url'),
    url(r'job', create_get, name='job_url'),
)

urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve'),
)
