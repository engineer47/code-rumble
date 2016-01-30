import factory
from django.contrib.auth.models import User

from ..choices import ACCOUNT_TYPE
from ..models import UserProfile


class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = User

    email = 'admin@gmail.com'
    first_name = 'system'
    last_name = 'admin'
    username = 'django'
    password1 = '1'
    password2 = '1'


class UserProfileFactory(factory.DjangoModelFactory):

    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)
    mobile = factory.Sequence(lambda n: '7765769{0}'.format(n))
    validated = True
    account = account=ACCOUNT_TYPE[0][1]