from django.db import models, transaction


class PollManager(models.Manager):
    def create_with_questions(self, data, creator):
        with transaction.atomic():
            questions = data.pop("questions")
            instance = self.create(**data, creator=creator)
            instance.questions.create_questions(questions, creator)
        return instance


class QuestionManager(models.Manager):
    def create_questions(self, questions, creator):
        instances = []
        for question in questions:
            question[self.field.name] = self.instance
            question["creator"] = creator
            instances.append(self.model(**question))
        self.bulk_create(instances)


class VoteManager(models.Manager):
    pass


class AnswerManager(models.Manager):
    pass
