from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAdminUser

from polls.models import Poll, Question
from polls.pagination import Pagination
from polls.serializers import (
    PollSerializer,
    PollUpdateSerializer,
    PollWithQuestionSerializer,
    QuestionSerializer,
)


class CreatePollView(CreateAPIView):
    serializer_class = PollSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.instance = Poll.objects.create(
            **serializer.validated_data, creator=self.request.user
        )


class CreatePollWithQuestionView(CreateAPIView):
    serializer_class = PollWithQuestionSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.instance = Poll.objects.create_with_questions(
            serializer.validated_data, creator=self.request.user
        )


class UpdatePollView(UpdateAPIView):
    serializer_class = PollUpdateSerializer
    permission_classes = (IsAdminUser,)
    queryset = Poll.objects.all()
    lookup_field = "guid"


class DeletePollView(DestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "guid"


class ListPollView(ListAPIView):
    serializer_class = PollSerializer
    pagination_class = Pagination
    queryset = Poll.objects.order_by("-id")


class DetailPollView(RetrieveAPIView):
    serializer_class = PollWithQuestionSerializer
    queryset = Poll.objects.all()
    lookup_field = "guid"


class CreateQuestionView(CreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.instance = Question.objects.create(
            **serializer.validated_data, creator=self.request.user
        )


class UpdateQuestionView(UpdateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser,)
    queryset = Question.objects.all()
    lookup_field = "guid"


class DeleteQuestionView(DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "guid"


class ListQuestionView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter(poll__guid=self.kwargs["guid"])


class DetailQuestionView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = "guid"
