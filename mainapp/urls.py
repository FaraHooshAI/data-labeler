from django.urls import path
from . import views
urlpatterns = [
    path("", views.DataRowView.as_view()),
    path("thank-you", views.index, name="nima"),
    path("data/<int:pk>", views.DataRowUpdateView.as_view(), name="data_row_update_view")
]
