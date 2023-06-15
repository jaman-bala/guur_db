from django.urls import path

from backend.apps.car.views import CarView, CarDetail

urlpatterns = [
    path('', CarView.as_view(), name='car'),
    path('<int:pk>', CarDetail.as_view(), name='car_detail'),
]
