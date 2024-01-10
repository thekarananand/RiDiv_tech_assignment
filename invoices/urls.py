from django.urls import path
from . import views

urlpatterns = [
    path("", views.invoices, name="invoices"),
    path("<int:pk>/", views.invoicesDetails, name="invoicesDetails")
]