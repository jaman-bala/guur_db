from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('pageadmin/', admin.site.urls),
    # path('', include('backend.apps.account.urls')),
    path('base/', include('backend.apps.manuldb.urls')),
    path('people/', include('backend.apps.people.urls')),
    path('car/', include('backend.apps.car.urls')),




]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

