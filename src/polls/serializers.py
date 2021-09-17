from rest_framework import serializers

from polls.models import Answer, Poll, Question, Vote


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


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(
        slug_field="guid", queryset=Question.objects.all()
    )

    class Meta:
        model = Answer
        fields = (
            "guid",
            "vote",
            "question",
            "choices",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("guid", "vote", "created_at", "updated_at")


class VoteWithAnswersSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, allow_null=False, allow_empty=False)
    poll = serializers.SlugRelatedField(
        slug_field="guid", queryset=Poll.objects.all()
    )

    class Meta:
        model = Vote
        fields = ("guid", "poll", "answers", "created_at", "updated_at")
        read_only_fields = ("guid", "created_at", "updated_at")


class VoteSerializer(serializers.ModelSerializer):
    poll = PollSerializer(read_only=True)

    class Meta:
        model = Vote
        fields = ("guid", "poll", "created_at", "updated_at")
