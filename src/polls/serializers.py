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


class PollQuestionSerializer(serializers.ModelSerializer):
    options = serializers.ListSerializer(
        child=serializers.CharField(), required=True
    )
    option_type = serializers.ChoiceField(
        required=True, choices=Question.OptionType.choices
    )

    class Meta:
        model = Question
        fields = ("guid", "text", "option_type", "options")


class PollWithQuestionSerializer(serializers.ModelSerializer):
    questions = PollQuestionSerializer(
        many=True, allow_null=False, allow_empty=False
    )

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


class QuestionSerializer(serializers.ModelSerializer):
    poll = serializers.SlugRelatedField(
        slug_field="guid", queryset=Poll.objects.all()
    )
    options = serializers.ListSerializer(
        child=serializers.CharField(), required=True
    )
    option_type = serializers.ChoiceField(
        required=True, choices=Question.OptionType.choices
    )

    class Meta:
        model = Question
        fields = ("guid", "poll", "text", "option_type", "options")
