from django.urls import path
from .views import *

urlpatterns = [
    path('get_Spares/', get_Spares),
    path('get_featured_products/', get_featured_products),
    path('get_helper/', get_helper),
    path('get_Partner/', get_Partner),
    path('get_Info/', get_Info),
    path('get_Debt/', get_Debt),
    path('get_Machine/', get_Machine),
    path('get_The_deliveryman/', get_The_deliveryman),
    path('get_Cleaner/', get_Cleaner),
]