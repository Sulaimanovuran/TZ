from django.urls import include, path
from rest_framework.routers import DefaultRouter

from sample.views import *

router = DefaultRouter()

router.register('scroll', ScrollView)
router.register('date', DateView)

urlpatterns = [
    path('', include(router.urls)),
    path('filter/', get_employee)
]