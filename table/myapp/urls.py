from django.urls import path
from .views import JobDataViewSet

urlpatterns = [
    path('jobdata/', JobDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='jobdata-list'),
]
