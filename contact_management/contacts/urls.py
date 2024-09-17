from django.urls import path
from .views import home, add_contact, edit_contact, delete_contact, search_contacts, contact_details #instant_search

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_contact, name='add_contact'),
    path('edit/<int:contact_id>/', edit_contact, name='edit_contact'),
    path('delete/<int:contact_id>/', delete_contact, name='delete_contact'),
    path('details/<int:contact_id>/', contact_details, name='contact_details'),
    path('search/', search_contacts, name='search_contacts'),  # For search -using Button
    # path('instant-search/', instant_search, name='instant_search'), # For instant search
]