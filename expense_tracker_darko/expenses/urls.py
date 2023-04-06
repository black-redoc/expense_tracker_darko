from django.urls import path

from expense_tracker_darko.expenses.views import index

app_name = "expenses"
urlpatterns = [path("", index, name="index")]
