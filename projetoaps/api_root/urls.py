
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import routers
from api_rest.views import FilmesViewSet  # Assuming 'api_rest' is the correct app name

router = routers.DefaultRouter()
router.register(r'filmes', FilmesViewSet)  # Assuming you have a FilmesViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/", include(router.urls)),  # Include the router's URLs
]