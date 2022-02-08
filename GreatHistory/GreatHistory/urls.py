from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
import mainapp.views as mainapp
import authapp.views as authapp
router = DefaultRouter()
router.register('users', authapp.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('', include('mainapp.urls', namespace='main')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)