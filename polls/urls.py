from django.urls import path
from .views import (
    polling_unit,
    sum_polling_unit,
    add_new_polling_unit,
)
from . import views


urlpatterns = [
    path("polling-unit/<int:polling_unit_id>/", polling_unit, name="polling_unit"),
    path("lga-results/", views.lga_results, name="lga_results"),
    path("polling-unit/new/", views.create_polling_unit, name="create_polling_unit"),
]
