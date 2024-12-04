from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView  # Import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('profiles.urls')),
    path('', RedirectView.as_view(url='/profile/', permanent=True)),  # Redirect root to profile
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
