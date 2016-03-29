from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
from views import *

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    
    url(r"^pantallas/(?P<pk>\d+)/$",PantallaDetailView.as_view(),name="pantalla_detail"),
    #~ url(r"^pantallas/new/",PantallaCreateView.as_view(),name="pantalla_new"),
    #~ url(r"^pantallas/",PantallaListView.as_view(),name="pantalla_list"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
