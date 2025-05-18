from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch  # Добавляем импорт mock

from online_school.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        # Подготовка данных перед каждым теcтом
        self.user = User.objects.create(email='admin@admin.com')
        self.course = Course.objects.create(
            name='Физика',
            description='Уроки по Физики',
            creator=self.user)
        self.lesson = Lesson.objects.create(
            name='Урок 1',
            description='Описание первого урока',
            link_video='http://www.youtube.com',
            course=self.course,
            creator=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('online_school:lesson-get', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.lesson.name
        )

    @patch('online_school.views.test_celery.delay')  # Мокаем Celery задачу
    def test_lesson_create(self, mock_celery):
        mock_celery.return_value = None  # Задаем возвращаемое значение

        url = reverse('online_school:lesson-create')
        data = {
            'name': 'Урок 2',
            'description': 'Продолжение',
            'course': self.course.pk,
            'link_video': 'http://www.youtube.com',
            'creator': self.user.pk
        }
        response = self.client.post(url, data=data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )
        mock_celery.assert_called_once()  # Проверяем, что задача была вызвана

    def test_lesson_update(self):
        url = reverse('online_school:lesson-update', args=(self.lesson.pk,))
        data = {'name': 'Урок 3'}
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.data.get('name'), 'Урок 3'
        )

    def test_lesson_delete(self):
        url = reverse('online_school:lesson-delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        print(response.data)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse('online_school:lesson-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(len(response.data['results']), 1)

        lesson_data = response.data['results'][0]
        self.assertEqual(lesson_data['id'], self.lesson.pk)
        self.assertEqual(lesson_data['name'], self.lesson.name)
        self.assertEqual(lesson_data['description'], self.lesson.description)
        self.assertEqual(lesson_data['link_video'], self.lesson.link_video)
        self.assertIsNone(lesson_data['preview'])
        self.assertEqual(lesson_data['course'], self.lesson.course.pk)
        self.assertEqual(lesson_data['creator'], self.lesson.creator.pk)

        if 'url' in lesson_data:
            self.assertIsNone(lesson_data['url'])


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.user = User.objects.create(email='admin@admin.com')
        self.course = Course.objects.create(
            name='Джанго',
            description='Уроки по Джанго',
            creator=self.user)
        self.lesson = Lesson.objects.create(
            name='Урок 1',
            description='Начало',
            course=self.course,
            creator=self.user)
        self.subscription = Subscription.objects.create(
            course=self.course, user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription(self):
        url = reverse("online_school:subscription")
        data = {
            "course": self.course.pk
        }
        response = self.client.post(url, data)
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data.get('message'), 'Подписка отключена'
        )