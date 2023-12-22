from django.urls import path
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'admin-complaint',AdminComplaintViewSet,basename='admin-complaint')

urlpatterns = [
    path('create-complate/', UserComplaintCreateView.as_view(),name='create-complate')
]+router.urls