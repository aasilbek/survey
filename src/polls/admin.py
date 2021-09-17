from django.contrib import admin

from .models import Poll, Question


class PollAdmin(admin.ModelAdmin):
    model = Poll


admin.site.register(Poll, PollAdmin)


class QuestionAdmin(admin.ModelAdmin):
    model = Question


admin.site.register(Question, QuestionAdmin)
