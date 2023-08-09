from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from auto_master_wizard_app.users.views import google_login, me, UsersViewSet, upload_profile_img, \
    upload_profile_img_url

router = DefaultRouter()
router.register('', UsersViewSet)

urlpatterns = [
    path('login', TokenObtainPairView.as_view()),
    path('login/refresh', TokenRefreshView.as_view()),
    path('google-auth', google_login),
    path('me', me),
    path('profile/img', upload_profile_img),
    path('profile/img/presigned', upload_profile_img_url)
]
urlpatterns.extend(router.urls)
