from django.contrib import admin
from django.urls import path, include

from Tivix.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('budgets/', include('budgets.urls')),
    path('auth/', include('users.urls')),
    path('admin/', admin.site.urls),
]
