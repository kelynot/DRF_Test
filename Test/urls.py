from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from DJ_DRF_Test.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tasks/', TaskCreateView.as_view()),
    path('api/v1/tasks/<int:pk>/', TaskUpdate.as_view()),
    path('api/v1/users/', UserCreateView.as_view()),
    path('api/v1/users/<int:pk>/', UserView.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]