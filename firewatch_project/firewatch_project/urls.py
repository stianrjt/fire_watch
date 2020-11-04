from django.contrib import admin
from django.urls import path, include
from fire_app import views

urlpatterns = [
    path('', views.overview, name='FireApp'),
    path('overview/', views.overview, name="overview"),
    path('graphs/', views.graphs, name="graphs"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('load/', views.load_csv, name='Load CSV')
]
