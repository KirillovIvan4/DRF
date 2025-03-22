from rest_framework import viewsets, generics

from online_school.models import Сourse, Lesson
from online_school.serializers import СourseSerializer, LessonSerializer


class СourseViewSet(viewsets.ModelViewSet):
    serializer_class = СourseSerializer
    queryset = Сourse.objects.all()

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
