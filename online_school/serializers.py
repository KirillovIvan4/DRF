from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.generics import  get_object_or_404
from rest_framework.response import Response

from online_school.models import Course, Lesson, Payments, Subscription
from online_school.validators import validate_youtube_link


class LessonSerializer(serializers.ModelSerializer):
    link_video = serializers.URLField(validators=[validate_youtube_link])
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    last_lesson = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True)
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'
    def get_subscription(self, instance):
        pass


    def get_last_lesson(self, instance):
        if instance.lesson.all():
            return instance.lesson.all().count()
        return 0




class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

