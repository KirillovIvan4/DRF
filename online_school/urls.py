from django.urls import path

from online_school.apps import OnlineSchoolConfig
from rest_framework.routers import DefaultRouter

from online_school.views import (CourseViewSet, LessonCreateAPIView, \
                                 LessonListAPIView, LessonRetrieveAPIView, \
                                 LessonUpdateAPIView, LessonDestroyAPIView, PaymentsCreateAPIView, \
                                 PaymentsListAPIView, SubscriptionAPIView)

app_name = OnlineSchoolConfig.name

router = DefaultRouter()
router.register(r'cours', CourseViewSet, basename='cours')

urlpatterns = [
                  # Уроки
                  path(
                      'lesson/create/',
                      LessonCreateAPIView.as_view(),
                      name='lesson-create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
                  path(
                      'lesson/<int:pk>/',
                      LessonRetrieveAPIView.as_view(),
                      name='lesson-get'),
                  path(
                      'lesson/update/<int:pk>/',
                      LessonUpdateAPIView.as_view(),
                      name='lesson-update'),
                  path(
                      'lesson/delete/<int:pk>/',
                      LessonDestroyAPIView.as_view(),
                      name='lesson-delete'),
                  # Платежи
                  path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),
                  path(
                      'payments/create/',
                      PaymentsCreateAPIView.as_view(),
                      name='payments-create'),
                  path("subscription/", SubscriptionAPIView.as_view(), name="subscription"),
              ] + router.urls
