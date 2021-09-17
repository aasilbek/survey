from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from polls.views import (
    CreatePollView,
    DeletePollView,
    DetailPollView,
    ListPollView,
    UpdatePollView,
)

poll_urls = [
    path("admin/", ListPollView.as_view(), name="admin_list"),
    path("create/", CreatePollView.as_view(), name="create"),
    path("<uuid:guid>/", DetailPollView.as_view(), name="detial"),
    path("<uuid:guid>/update/", UpdatePollView.as_view(), name="update"),
    path("<uuid:guid>/delete/", DeletePollView.as_view(), name="delete"),
]
urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("poll/", include(poll_urls), name="polls"),
]
