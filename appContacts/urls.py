from django.urls import path
from . import views

urlpatterns = [
    path('p_contacts', views.func_p_contacts, name='p_contacts'),
    path('b_contacts', views.func_b_contacts, name='b_contacts'),
    path('add_p_contact', views.add_p_contact, name='add_p_contact'),
    path('add_b_contact', views.add_b_contact, name='add_b_contact'),
    path('add_business_type', views.add_business_type, name='add_business_type'),
    path('update_p_contact/<str:pk_p_contact_id>', views.update_p_contact, name='update_p_contact'),
    path('update_b_contact/<str:pk_b_contact_id>', views.update_b_contact, name='update_b_contact'),
    path('delete_p_contact/<str:pk_p_contact_id>', views.delete_p_contact, name='delete_p_contact'),
    path('delete_b_contact/<str:pk_b_contact_id>', views.delete_b_contact, name='delete_b_contact'),
]