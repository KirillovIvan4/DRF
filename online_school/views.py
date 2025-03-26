from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from online_school.models import Сourse, Lesson, Payments
from online_school.serializers import СourseSerializer, LessonSerializer, PaymentsSerializer
from rest_framework.permissions import IsAuthenticated, NOT

from users.permissions import IsModer, IsNotModer, IsCreator


class СourseViewSet(viewsets.ModelViewSet):
    serializer_class = СourseSerializer
    queryset = Сourse.objects.all()

    def get_permissions(self):
        if self.action in ["create"]:
            self.permission_classes = [ IsNotModer]
        elif self.action in ["destroy", "update"]:
            self.permission_classes = [IsCreator]
        elif self.action in [ "retrieve"]:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

    def perform_create(self,serializer):
        lesson = serializer.save()
        lesson.creator =self.request.user
        lesson.save()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [NOT(IsModer())]
        return super().get_permissions()

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsCreator]
        return super().get_permissions()

class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsCreator]
        return super().get_permissions()

class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer

    def perform_create(self, serializer):
        payments = serializer.save()
        payments.user = self.request.user
        payments.save()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [NOT(IsModer())]
        return super().get_permissions()

class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('lesson', 'course')
    search_fields = ('method_payment',)
    ordering_fields = ('payment_date',)