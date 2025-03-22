from django.contrib import admin

from online_school.models import Сourse, Lesson


@admin.register(Сourse)
class СourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)
