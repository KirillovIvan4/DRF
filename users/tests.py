# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
#
# from online_school.models import Course, Lesson, Payments, Subscription
# from users.models import User
#
#
# class LessonTestCase(APITestCase):
#
#     def setUp(self):
#         # Подготовка данных перед каждым теcтом
#         self.user = User.objects.create(email='admin@admin.com')
#         self.course = Course.objects.create(name='Физика', description='Уроки по Физики', creator=self.user)
#         self.lesson = Lesson.objects.create(name='Урок 1', description='Описание первого урока',link_video='www.youtube.com', course=self.course, creator=self.user)
#         self.client.force_authenticate(user=self.user)
#
#     def test_lesson_retrieve(self):
#         url = reverse('online_school:lesson-get', args=(self.lesson.pk,))
#         response = self.client.get(url)
#         data = response.json()
#         print(response.data)
#         self.assertEqual(
#             response.status_code, status.HTTP_200_OK
#         )
#         self.assertEqual(
#             data.get('name'), self.lesson.name
#         )
#
#     def test_lesson_create(self):
#         url = reverse('online_school:lesson-create')
#         data = {
#             'name': 'Урок 2',
#             'description': 'Продолжение',
#             'course': self.course.pk
#         }
#         response = self.client.post(url, data)
#         print(response.data)
#         self.assertEqual(
#             response.status_code, status.HTTP_201_CREATED
#         )
#         self.assertEqual(
#             Lesson.objects.all().count(), 2
#         )
#
#     def test_lesson_update(self):
#         url = reverse('online_school:lesson-update', args=(self.lesson.pk,))
#         data = {'name': 'Урок 3'}
#         response = self.client.patch(url, data)
#         print(response.data)
#
#         self.assertEqual(
#             response.status_code, status.HTTP_200_OK
#         )
#         self.assertEqual(
#             response.data.get('name'), 'Урок 3'
#         )
#
#     def test_lesson_delete(self):
#         url = reverse('online_school:lesson-delete', args=(self.lesson.pk,))
#         response = self.client.delete(url)
#         print(response.data)
#         self.assertEqual(
#             response.status_code, status.HTTP_204_NO_CONTENT
#         )
#         self.assertEqual(
#             Lesson.objects.all().count(), 0
#         )
#
#     def test_lesson_list(self):
#         url = reverse('online_school:lesson-list')
#         response = self.client.get(url)
#         print(response.data)
#
#         self.assertEqual(
#             response.status_code, status.HTTP_200_OK
#         )
#         self.assertEqual(
#             response.data,
#             {'count': 1, 'next': None, 'previous': None, 'results':
#                 [{'id': self.lesson.pk, 'name': self.lesson.name, 'description': self.lesson.description, 'link_video':self.lesson.link_video,
#                   'preview': None, 'url': None,
#                   'course': self.lesson.course.pk, 'creator': self.lesson.creator.pk}]}
#         )
#
#
# class SubscriptionTestCase(APITestCase):
#
#     def setUp(self):
#         # Подготовка данных перед каждым тестом
#         self.user = User.objects.create(email='admin@admin.com')
#         self.course = Course.objects.create(name='Джанго', description='Уроки по Джанго', creator=self.user)
#         self.lesson = Lesson.objects.create(name='Урок 1', description='Начало', course=self.course, creator=self.user)
#         self.subscription = Subscription.objects.create(course=self.course, user=self.user)
#         self.client.force_authenticate(user=self.user)
#
#     def test_subscription(self):
#         url = reverse("online_school:subscription")
#         data = {
#             "course": self.course.pk
#         }
#         response = self.client.post(url, data)
#         print(response.data)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data.get('message'), 'Подписка отключена'
#         )
