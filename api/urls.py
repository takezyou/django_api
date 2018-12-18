from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'signup', SignUpView, base_name='signup')
router.register(r'login', LoginView, base_name='login')
router.register(r'logout', LogoutView, base_name='logout')
router.register(r'post', PostView, base_name='post')
router.register(r'post_list', PostListView, base_name='post_list')
