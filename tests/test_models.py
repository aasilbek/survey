import datetime

from django.contrib.auth import get_user_model

import pytest

from polls.models import Answer, Poll, Question, Vote


@pytest.mark.django_db
def test_poll():
    Poll.objects.create(
        title="Poll about university subjects",
        description="Give feedback for each subject",
        start_at=datetime.datetime.now(),
        end_at=datetime.datetime.now(),
    )

    assert Poll.objects.count() == 1


@pytest.mark.django_db
def test_question():
    poll = Poll.objects.create(
        title="Poll about university subjects",
        description="Give feedback for each subject",
        start_at=datetime.datetime.now(),
        end_at=datetime.datetime.now(),
    )
    user = get_user_model().objects.create_user(
        username="test", email="test@mail.ru", password="12345"
    )
    Question.objects.create(
        poll=poll,
        text="Give rate for subject Database Management",
        option_type=Question.OptionType.CHOICE,
        options=["1", "2", "3", "4"],
        creator=user,
    )

    assert Question.objects.count() == 1


@pytest.mark.django_db
def test_vote():
    poll = Poll.objects.create(
        title="Poll about university subjects",
        description="Give feedback for each subject",
        start_at=datetime.datetime.now(),
        end_at=datetime.datetime.now(),
    )
    Vote.objects.create(poll=poll)

    assert Vote.objects.count() == 1


@pytest.mark.django_db
def test_answer():
    poll = Poll.objects.create(
        title="Poll about university subjects",
        description="Give feedback for each subject",
        start_at=datetime.datetime.now(),
        end_at=datetime.datetime.now(),
    )
    vote = Vote.objects.create(poll=poll)
    user = get_user_model().objects.create_user(
        username="test", email="test@mail.ru", password="12345"
    )
    question = Question.objects.create(
        poll=poll,
        text="Give rate for subject Database Management",
        option_type=Question.OptionType.CHOICE,
        options=["1", "2", "3", "4"],
        creator=user,
    )
    Answer.objects.create(question=question, vote=vote, choices=["1"])

    assert Answer.objects.count() == 1


def create_user(email: str):
    User = get_user_model()
    return User.objects.create(email=email)


@pytest.mark.django_db
def test_create_user_adds_new_user(django_assert_num_queries):
    # Given
    email = "user@email.com"

    # When
    with django_assert_num_queries(1):
        user = create_user(email)

    # Then
    assert user.email == email


@pytest.mark.django_db
def test_create_user_raises_exception(django_assert_num_queries):
    with django_assert_num_queries(0), pytest.raises(TypeError):
        create_user()
