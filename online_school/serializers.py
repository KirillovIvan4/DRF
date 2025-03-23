from rest_framework import serializers

from online_school.models import Сourse, Lesson, Payments

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class СourseSerializer(serializers.ModelSerializer):
    last_lesson = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True)
    class Meta:
        model = Сourse
        fields = '__all__'

    def get_last_lesson(self, instance):
        if instance.lesson.all():
            return instance.lesson.all().count()
        return 0


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'