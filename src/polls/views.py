from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAdminUser

from polls.models import Poll
from polls.pagination import Pagination
from polls.serializers import (
    DetailPollSerializer,
    PollSerializer,
    PollUpdateSerializer,
)


class CreatePollView(CreateAPIView):
    serializer_class = PollSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.instance = Poll.objects.create(
            **serializer.validated_data, creator=self.request.user
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
    serializer_class = DetailPollSerializer
    queryset = Poll.objects.all()
    lookup_field = "guid"
