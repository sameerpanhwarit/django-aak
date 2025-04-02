# from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, LabelViewSet

router  =  DefaultRouter()
router.register(r'tasks',TaskViewSet,basename='tasks')
router.register(r'labels', LabelViewSet,basename='labels')

urlpatterns = [
    path('',include(router.urls)),
]