from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CafeteriaViewset

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'cafeterias', CafeteriaViewset, basename='cafeteria')

urlpatterns = [
    path('', include(router.urls)),
]
