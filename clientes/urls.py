from django.urls import path
from .views import persorns_list, persorns_new, persorns_update, persorns_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cli_list/', persorns_list, name='persorns_list'),
    path('cli_new/', persorns_new, name='persorns_new'),
    path('update/<int:id>', persorns_update, name='update'),
    path('cli_delete/<int:id>', persorns_delete, name='persorns_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
