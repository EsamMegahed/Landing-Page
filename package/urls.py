from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .api import UmrahViewsets,HajjViewsets

app_name = "package"

router = DefaultRouter()
router.register('umrah', UmrahViewsets)
router.register('hajj', HajjViewsets)

urlpatterns = [
    path('', include(router.urls)),
]