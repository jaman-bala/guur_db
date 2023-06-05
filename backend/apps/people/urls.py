from django.urls import path
from backend.apps.people.views import PeopleView

urlpatterns = [
    path('', PeopleView.as_view(), name='people'),
    # path('<int:pk>', PeopleDetail.as_view(), name='people_detail'),

]
