from django.contrib import admin

from .models import Poll, Question


class PollAdmin(admin.ModelAdmin):
    model = Poll
    list_display = ("guid", "title")


admin.site.register(Poll, PollAdmin)


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ("guid", "text", "option_type", "options")


admin.site.register(Question, QuestionAdmin)
