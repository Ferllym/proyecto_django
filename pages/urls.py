from django.urls import path
from .views import HomePageView, AboutPageView , LoginPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="base"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("login/", LoginPageView.as_view(), name="login"),
]
