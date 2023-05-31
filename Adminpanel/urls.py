from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    #Spares
    path('add_spares/', add_spares, name='add_spares'),
    path('edit_spares/<int:pk>/', edit_spares, name='edit_spares'),
    path('spares_list/', spares_list, name='spares_list'),
    path('delete_spares/<int:pk>/', delete_spares, name='delete_spares'),
    #Login and register views
    path('login/', login_views, name='login'),
    path('register/', register, name='register'),
    path('logout_vews/', logout_vews, name='logout_vews'),
    #Featured Product
    path('add_featured_product/', add_featured_product, name='add_featured_product'),
    path('edit_featured_product/<int:pk>/', edit_featured_product, name='edit_featured_product'),
    path('featured_product_list/', featured_product_list, name='featured_product_list'),
    path('delete_featured_product/<int:pk>/', delete_featured_product, name='delete_featured_product'),
    #Helper
    path('add_helper/', add_helper, name='add_helper'),
    path('edit_helper/<int:pk>/', edit_helper, name='edit_helper'),
    path('helper_list/', helper_list, name='helper_list'),
    path('delete_helper/<int:pk>/', delete_helper, name='delete_helper'),
    #Partner
    path('add_partner/', add_partner, name='add_partner'),
    path('edit_partner/<int:pk>/', edit_partner, name='edit_partner'),
    path('partner_list/', partner_list, name='partner_list'),
    path('delete_partner/<int:pk>/', delete_partner, name='delete_partner'),
    #Info
    path('add_info/', add_info, name='add_info'),
    path('edit_info/<int:pk>/', edit_info, name='edit_info'),
    path('info_list/', info_list, name='info_list'),
    path('delete_info/<int:pk>/', delete_info, name='delete_info'),
    #Debt
    path('add_debt/', add_debt, name='add_debt'),
    path('edit_debt/<int:pk>/', edit_debt, name='edit_debt'),
    path('debt_list/', debt_list, name='debt_list'),
    path('delete_debt/<int:pk>/', delete_debt, name='delete_debt'),
    #Earning info
    path('add_earning_info/', add_earning_info, name='add_earning_info'),
    path('edit_earning_info/<int:pk>/', edit_earning_info, name='edit_earning_info'),
    path('earning_list/', earning_list, name='earning_list'),
    path('delete_earning_info/<int:pk>/', delete_earning_info, name='delete_earning_info'),
    #Machine
    path('add_machine/', add_machine, name='add_machine'),
    path('edit_machine/<int:pk>/', edit_machine, name='edit_machine'),
    path('machine_list/', machine_list, name='machine_list'),
    path('delete_machine/<int:pk>/', delete_machine, name='delete_machine'),
    #Deliveryman
    path('add_deliveryman/', add_deliveryman, name='add_deliveryman'),
    path('edit_deliveryman/<int:pk>/', edit_deliveryman, name='edit_deliveryman'),
    path('the_deliveryman_list/', the_deliveryman_list, name='the_deliveryman_list'),
    path('delete_deliveryman/<int:pk>/', delete_deliveryman, name='delete_deliveryman'),
    #Cleaner
    path('add_cleaner/', add_cleaner, name='add_cleaner'),
    path('edit_cleaner/<int:pk>/', edit_cleaner, name='edit_cleaner'),
    path('cleaner_list/', cleaner_list, name='cleaner_list'),
    path('delete_cleaner/<int:pk>/', delete_cleaner, name='delete_cleaner'),

]