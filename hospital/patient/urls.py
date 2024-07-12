from django.urls import path
from .  import views

urlpatterns = [
    path('getPatient',views.getPatient),
    path('addPatient',views.addPatient),
    path('getSinglePatient/<str:pk>/',views.getSinglePatient),
    path('updatePatient/<str:pk>/',views.updatePatient),
    path('deletePatient/<str:pk>/',views.deletePatient),
]
