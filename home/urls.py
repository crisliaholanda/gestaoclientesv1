from django.urls import path
from django.conf import settings
from .views import home, logout_page
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_page, name='logout'),
]

