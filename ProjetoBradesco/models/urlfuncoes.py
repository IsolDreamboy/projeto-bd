from django.urls import path
from .endpoints import RegistroView, LoginView, ValoresReceberView

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('valores-a-receber/', ValoresReceberView.as_view(), name='valores'),
]
