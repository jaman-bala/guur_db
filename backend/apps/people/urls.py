from django.urls import path
from backend.apps.people.views import PeopleView

urlpatterns = [
    path('', PeopleView.as_view(), name='people'),
    # path('<int:pk>', IndexDetail.as_view(), name='code_detail'),

]
