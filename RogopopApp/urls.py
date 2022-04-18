from django.conf import Settings
from django.contrib import admin
from django.urls import path, include, re_path
from django_registration.backends.one_step.views import RegistrationView
from accounts.forms import CustomUserForm
from django.conf.urls.static import static
from django.conf import settings

from core.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/',
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url='/'),
         name='django_registration_register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth', include("rest_framework.urls")),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('api/v1/', include("concerts.api.urls")),
    path('api/v1/', include("accounts.api.urls")),

    re_path(r"^(?!media).*$", IndexTemplateView.as_view(),
            name="spa-entry-point")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
