from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload-file/', views.model_form_upload, name="upload-file"),
    path('packet-details/', views.packet_details, name="packet-details"),
    path('packetno-size/', views.packetno_size,name="packetno-size"),
    path('packetno-time/', views.packetno_time,name="packetno-time"),
    path('generate-plots/', views.Temp, name="temp"),
]