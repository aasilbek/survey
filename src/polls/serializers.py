from rest_framework import serializers

from polls.models import Poll, Question


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = (
            "guid",
            "title",
            "description",
            "start_at",
            "created_at",
            "updated_at",
            "end_at",
        )
        read_only_fields = ("guid", "created_at", "updated_at")

    def validate_start_at(self, value):
        if self.instance and self.instance.start_at:
            raise serializers.ValidationError(
                "Not allowed to change stat_at after poll is started"
            )
        return value


class PollUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = (
            "guid",
            "title",
            "start_at",
            "description",
            "created_at",
            "updated_at",
            "end_at",
        )
        read_only_fields = ("guid", "start_at", "created_at", "updated_at")


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("guid", "text", "option_type", "options")


class DetailPollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = (
            "guid",
            "title",
            "description",
            "start_at",
            "created_at",
            "updated_at",
            "end_at",
            "questions",
        )
