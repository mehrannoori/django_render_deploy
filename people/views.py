from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import People

class PeopleListView(ListView):
    model = People
    context_object_name = 'people_list'
    template_name = 'people.html'

class AddPeople(CreateView):
    model = People
    fields = ['firstname', 'lastname', 'age']
    success_url = reverse_lazy('people')
    template_name = 'add.html'