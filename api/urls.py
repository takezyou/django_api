from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'signup', SignUpView, base_name='signup')
