from django.urls import path
from . import views
urlpatterns = [
    path("", views.DataRow.as_view())
]
