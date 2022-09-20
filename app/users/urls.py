from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import LoginClassView, RegisterClassView

app_name = "users"

urlpatterns = [
    path('login/', LoginClassView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterClassView.as_view(), name='register'),
]
