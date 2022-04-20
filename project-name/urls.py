from django.contrib import admin
from django.urls import path,include
from bonds_app.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,)

#farooque branch
#change #6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bonds_app/', include('bonds_app.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
