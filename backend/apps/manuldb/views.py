from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView

from backend.apps.weapons.models import Weapons
from backend.apps.manuldb.models import Vid, Category
from backend.apps.people.models import People


class IndexView(ListView):
    queryset = Weapons.objects.all()
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    paginate_by = 70

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        people = People.objects.all()
        weapons = Weapons.objects.all()
        vid = Vid.objects.all()
        city = Category.objects.all()
        context = {
            "people": people,
            "weapons": weapons,
            "vid": vid,
            "city": city,
        }
        return context


class IndexDetail(DetailView):
    model = People.objects.all()
    template_name = 'people_info.html'
    context_object_name = 'people_information'
    success_url = reverse_lazy('people_info')
    queryset = People.objects.all()




