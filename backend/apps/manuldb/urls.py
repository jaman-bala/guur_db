from django.urls import path
from backend.apps.manuldb.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('<int:pk>', IndexDetail.as_view(), name='code_detail'),

]
