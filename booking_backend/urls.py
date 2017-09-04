from django.conf.urls import url, include
from rest_framework import routers
from api.views import view_user

router = routers.DefaultRouter()
router.register(r'users', view_user.UserViewSet)
router.register(r'groups', view_user.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
