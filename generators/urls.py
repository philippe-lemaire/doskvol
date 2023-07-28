from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "generators"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("/street", views.streetView, name="streets"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
