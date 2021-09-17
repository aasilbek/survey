import datetime

from django.db import models, transaction


class PollManager(models.Manager):
    def create_with_questions(self, data, creator):
        with transaction.atomic():
            questions = data.pop("questions")
            instance = self.create(**data, creator=creator)
            instance.questions.create_questions(questions, creator)
        return instance

    def get_with_question(self):
        return self.prefetch_related("question").order_by("-id")

    def get_active_polls(self):
        current_time = datetime.datetime.now()
        return self.filter(
            start_at__lte=current_time, end_at__gte=current_time
        ).order_by("-id")


class QuestionManager(models.Manager):
    def create_questions(self, questions, creator):
        instances = []
        for question in questions:
            question[self.field.name] = self.instance
            question["creator"] = creator
            instances.append(self.model(**question))
        self.bulk_create(instances)


class VoteManager(models.Manager):
    def create_with_answers(self, data, user):
        if not user.is_authenticated:
            user = None
        with transaction.atomic():
            questions = data.pop("answers")
            instance = self.create(**data, user=user)
            instance.answers.create_answers(questions)
        return instance

    def get_with_answers(self):
        return self.select_related("poll").order_by("-id")


class AnswerManager(models.Manager):
    def create_answers(self, answers):
        instances = []
        for answer in answers:
            answer[self.field.name] = self.instance
            instances.append(self.model(**answer))
        self.bulk_create(instances)
