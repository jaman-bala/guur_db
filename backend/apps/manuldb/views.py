from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView

from backend.apps.weapons.models import Weapons
from backend.apps.people.models import People


class IndexView(ListView):
    queryset = Weapons.objects.all()
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    paginate_by = 70

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['people'] = People.objects.all()
        return context



# class WeaponsView(ListView):
#         model = Weapons
#         template_name = 'weapons.html'
#         context_object_name = 'weapons'
#         paginate_by = 70
#
#
#
# class WeaponsDetailView(DetailView):
#         model = Weapons
#         template_name = 'details_weapons.html'
#         context_object_name = 'weaponsout'
#         queryset = Weapons.objects.all()
#
#
# class CartView(ListView):
#     model = Car
#     template_name = 'products.html'
#     context_object_name = 'products'
#     paginate_by = 70
#     queryset = Car.objects.all()


