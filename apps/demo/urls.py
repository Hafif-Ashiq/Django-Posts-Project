# urls.py
from django.urls import path
from .views import PostListView, SignupView, LoginView

urlpatterns = [
    path("posts/", PostListView.as_view(), name="post-list"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
]
