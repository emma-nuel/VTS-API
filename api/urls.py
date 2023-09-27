from django.urls import path
from api import views

urlpatterns = [
    path('api/', views.VehicleList.as_view()),
    path('api/location/', views.GetCurrentVehicleDetails.as_view()),
    path('api/switch/', views.VehicleState.as_view())
]