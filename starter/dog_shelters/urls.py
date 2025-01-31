from django.urls import path
from . import views

urlpatterns = [
    path('shelters', views.shelter_list, name='shelter_list'),
    path('shelter/<int:pk>', views.shelter_detail, name='shelter_detail')
]
