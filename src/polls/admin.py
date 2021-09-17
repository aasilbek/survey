from django.contrib import admin

from .models import Answer, Poll, Question, Vote


class QuestionAdmin(admin.TabularInline):
    model = Question
    list_display = ("guid", "text", "option_type", "options")


class PollAdmin(admin.ModelAdmin):
    inlines = [QuestionAdmin]
    model = Poll
    list_display = ("guid", "title")


admin.site.register(Poll, PollAdmin)


class AnswerAdmin(admin.TabularInline):
    model = Answer


class VoteAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]
    model = Vote
    list_display = ("guid", "poll", "user")


admin.site.register(Vote, VoteAdmin)
