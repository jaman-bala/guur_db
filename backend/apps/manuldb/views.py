from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView

from backend.apps.manuldb.models import PeopleImage
from backend.apps.people.models import People


class IndexView(ListView):
    queryset = People.objects.all()
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    paginate_by = 70

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        people = People.objects.all()
        context = {
            "people": people,
        }
        return context


class IndexDetail(DetailView):
    model = People.objects.all()
    template_name = 'people_info.html'
    context_object_name = 'people_information'
    success_url = reverse_lazy('people_info')
    queryset = People.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        people_images = PeopleImage.objects.filter(people=self.object)
        context['people_images'] = people_images
        return context









