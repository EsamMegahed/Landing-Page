from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .api import CommentViewsets
 

app_name = "contact"

router = DefaultRouter()
router.register('', CommentViewsets)

urlpatterns = [
    path('', include(router.urls)),
]