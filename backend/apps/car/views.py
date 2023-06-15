from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from backend.apps.car.models import Car


class CarView(ListView):
    queryset = Car.objects.all()
    template_name = 'car.html'
    context_name = 'car'
    success_url = reverse_lazy('car')
    paginate_by = 70

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = Car.objects.all()
        context = {
            "car": car,
        }
        return context


class CarDetail(DetailView):
    model = Car.objects.all()
    template_name = 'car_detail.html'
    contex_name = 'car_detail'
    success_url = reverse_lazy('car')
    queryset = Car.objects.all()

