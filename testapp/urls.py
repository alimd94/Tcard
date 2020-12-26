from testapp.views import index
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .api import *

urlpatterns = [
    path('register/', RegisterApi.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('read/', ProductReadApi.as_view()),
    path('create/', ProductCreateApi.as_view()),
    path('update/<int:pk>/', ProductUpdateApi.as_view()),
    path('delete/<int:pk>/', ProductDeleteApi.as_view()),
    path('', index ),
]
