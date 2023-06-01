from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView

from backend.apps.people.models import People, PeopleImage
from backend.apps.people.forms import PeopleForm


class PeopleView(FormView, ListView):
    model = People.objects.all()
    image = PeopleImage.objects.all()
    form_class = PeopleForm
    template_name = 'people.html'
    success_url = reverse_lazy('people')
    context_object_name = 'people'
    queryset = People.objects.all()

    def create(self, form):
        data = {}
        if self.request.method == 'POST':
            form = PeopleForm(self.request.POST)
            if form.is_valid():
                form.save()
        else:
            error = 'Формат был неверной'
            form = PeopleForm()
            data = {
                'form': form,
                'error': error
            }
        return render(self.request, 'people.html', data)


class PeopleDetailView(DetailView):
    model = People.objects.all()
    image = PeopleImage.objects.all()
    template_name = 'detail_products.html'
    context_object_name = 'peopleout'
    queryset = People.objects.all()
