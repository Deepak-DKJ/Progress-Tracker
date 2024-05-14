from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='endpoint1'),
    # path('endpoint2/', views.endpoint2_view, name='endpoint2'),
]
