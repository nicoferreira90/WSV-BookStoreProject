
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin, auth
from django.urls import path, include


urlpatterns = [
    path('anything-but-admin/', admin.site.urls),
    path('', include('pages.urls')),
    path("accounts/", include("allauth.urls")),
    path("books/", include("books.urls")),
] + static(
settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    import debug_toolbar.toolbar
    urlpatterns = urlpatterns + [path('__debug__/', include(debug_toolbar.urls))]
    

