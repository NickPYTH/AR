from django.contrib import admin

from .models import Profile, Article, Test, Question, Answer, Achievement


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)


class TestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Test, TestAdmin)


class QuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Answer, AnswerAdmin)


class AchievementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Achievement, AchievementAdmin)