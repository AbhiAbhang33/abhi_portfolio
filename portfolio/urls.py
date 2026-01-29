from portfolio import views
from django_distill import distill_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    distill_path('', views.get_index, name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

