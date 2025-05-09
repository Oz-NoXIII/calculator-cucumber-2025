from django.urls import path
from .views import CalculatorAPIView

urlpatterns = [
    path('calculate/', CalculatorAPIView.as_view(), name='calculate'),
]