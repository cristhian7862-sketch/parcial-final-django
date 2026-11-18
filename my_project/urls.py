from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # INCLUIR LAS RUTAS HIJAS
    path('programas/', include("myapp.urls")),
    path('', RedirectView.as_view(pattern_name='crear_programa', permanent=False)),
]
