from django.urls import path
from .views import (
    polling_unit,
    sum_polling_unit,
    add_new_polling_unit,
)
from . import views


urlpatterns = [
    path("", polling_unit, name="polling_unit"),
    path("sum_total", sum_polling_unit, name="sum_polling_unit"),
    path("add_new", add_new_polling_unit, name="add_new_polling_unit"),
]