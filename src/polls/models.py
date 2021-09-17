import uuid

from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

from .managers import AnswerManager, PollManager, QuestionManager, VoteManager


class BaseModel(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Poll(BaseModel):
    title = models.CharField(max_length=256, db_index=True)
    description = models.TextField(max_length=1024)
    start_at = models.DateField(editable=False)
    end_at = models.DateField()
    objects = PollManager()

    class Meta:
        db_table = "poll"
        verbose_name = "Poll"
        verbose_name_plural = "Polls"

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"Poll <{self.title} , {self.start_at}-{self.end_at}>"


class Question(BaseModel):
    class OptionType:
        TEXT = "text"
        CHOICE = "choice"
        MULTIPLECHOICE = "multiplechoice"

        choices = (
            (TEXT, "text"),
            (CHOICE, "choice"),
            (MULTIPLECHOICE, "multiplechoice"),
        )

    poll = models.ForeignKey("Poll", on_delete=models.CASCADE)
    text = models.CharField(max_length=256, db_index=True)
    option_type = models.CharField(
        max_length=20, choices=OptionType.choices, default=OptionType.TEXT
    )
    options = ArrayField(models.CharField(max_length=50))
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    objects = QuestionManager()

    class Meta:
        db_table = "question"
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return f"{self.text}"

    def __repr__(self):
        return f"Question <{self.text} , {self.option_type} ({self.options}-)>"


class Vote(BaseModel):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, blank=True, null=True
    )
    objects = VoteManager()

    class Meta:
        db_table = "vote"
        verbose_name = "Vote"
        verbose_name_plural = "Votes"

    def __str__(self):
        return f"{self.user}"

    def __repr__(self):
        return f"Vote <{self.user} , {self.poll}>"


class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote = models.ForeignKey(
        Vote, related_name="answers", on_delete=models.CASCADE
    )
    choices = ArrayField(models.CharField(max_length=50))
    objects = AnswerManager()

    class Meta:
        db_table = "answer"
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __str__(self):
        return f"{self.question} - {self.choices}"

    def __repr__(self):
        return f"Answer <{self.vote} , {self.question}, {self.choices}>"
