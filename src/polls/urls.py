from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from polls.views import (
    CreatePollView,
    CreatePollWithQuestionView,
    CreateQuestionView,
    CreateVoteView,
    DeletePollView,
    DeleteQuestionView,
    DetailPollView,
    DetailQuestionView,
    DetailVoteView,
    ListActivePollView,
    ListPollView,
    ListQuestionView,
    ListVoteView,
    UpdatePollView,
    UpdateQuestionView,
)

question_url = [
    path("create/", CreateQuestionView.as_view(), name="create"),
    path("<uuid:guid>/poll/", ListQuestionView.as_view(), name="list"),
    path("<uuid:guid>/", DetailQuestionView.as_view(), name="detail"),
    path("<uuid:guid>/update/", UpdateQuestionView.as_view(), name="update"),
    path("<uuid:guid>/delete/", DeleteQuestionView.as_view(), name="delete"),
]

poll_urls = [
    path("admin/", ListPollView.as_view(), name="admin_list"),
    path("create/", CreatePollView.as_view(), name="create"),
    path(
        "create-with-question/",
        CreatePollWithQuestionView.as_view(),
        name="create_with_questions",
    ),
    path("<uuid:guid>/", DetailPollView.as_view(), name="detial"),
    path("<uuid:guid>/update/", UpdatePollView.as_view(), name="update"),
    path("<uuid:guid>/delete/", DeletePollView.as_view(), name="delete"),
]

vote_urls = [
    path("", ListVoteView.as_view(), name="list"),
    path("active-polls/", ListActivePollView.as_view(), name="active_polls"),
    path("create/", CreateVoteView.as_view(), name="create"),
    path("<uuid:guid>/", DetailVoteView.as_view(), name="detail"),
]

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("poll/", include(poll_urls), name="polls"),
    path("question/", include(question_url), name="questions"),
    path("vote/", include(vote_urls), name="votes"),
]
