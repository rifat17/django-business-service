from polls import views

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("polls/", views.ProtectedDataView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)