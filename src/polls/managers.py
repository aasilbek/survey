from django.db import models


class PollManager(models.Manager):
    pass


class QuestionManager(models.Manager):
    pass


class VoteManager(models.Manager):
    pass


class AnswerManager(models.Manager):
    pass
