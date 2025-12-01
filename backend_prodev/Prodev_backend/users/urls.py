from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from .views import register_page



urlpatterns = [
    path("forms/", register_page, name="register-page"),
    path('register/', RegisterView.as_view(), name='register'),
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]