from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify', verify_jwt_token),
]
