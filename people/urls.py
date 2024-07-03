from django.urls import path

from .views import PeopleListView, AddPeople

urlpatterns = [
    path('', PeopleListView.as_view(), name='people'),
    path('add/', AddPeople.as_view(), name='add_people'),
]