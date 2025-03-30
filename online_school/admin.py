from django.contrib import admin

from online_school.models import Course, Lesson, Payments


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'payment_amount', 'method_payment',)
    list_filter = ('user',)
    search_fields = ('user',)