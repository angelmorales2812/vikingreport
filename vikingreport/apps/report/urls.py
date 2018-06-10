from django.conf.urls import url
from apps.report.views import index

urlpatterns = [
        url(r'^index$', index),
]
