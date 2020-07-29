from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("class", views.ClassApiView.as_view(), name="class"),  # original class base
    path("function", views.function_api, name="function"),  # function base
]
