from django.urls import path, include

from rest_framework import routers

from api.viewsets import PostViewset


router = routers.SimpleRouter()

router.register(r'post', PostViewset)

urlpatterns = [
    path('', include(router.urls)),
]