from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls.conf import include

from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include("myapp.urls", "myapp")),
]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()

    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
