from django.urls import path
from .views import HashTagCloud

urlpatterns = [
    path('hashTag/<slug:hashTag_name>', HashTagCloud.as_view(), name='hashtags'),
]