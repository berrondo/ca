from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ca.core import views

router = routers.DefaultRouter()
router.register(r"events", views.EventViewSet)
router.register(r"raw-events", views.RawEventViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path('example/', include('ca.example.urls')),
]
