from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'), 
    path('eletronica/<str:nome_categoria>/', views.eletronica, name='eletronica'),
    path('casa/', views.casa, name='casa'),
    path('automotivo/', views.automotivo, name='automotivo'),
    path('ferramentas/', views.ferramentas, name='ferramentas'),
    path('esporte_lazer/', views.esporte_lazer, name='esporte_lazer'), 
    path('brinquedos/', views.brinquedos, name='brinquedos'), 
    path('eletrodomesticos/', views.eletrodomesticos, name='eletrodomesticos'),

      # Route for the index view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)