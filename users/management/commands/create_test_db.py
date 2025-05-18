# from django.core.management.base import BaseCommand
# from django.db import connections
#
#
# class Command(BaseCommand):
#     help = 'Creates test database structure'
#
#     def handle(self, *args, **options):
#         """Create test database by cloning the main database"""
#         # Создаем тестовую БД на основе основной
#         with connections['default'].cursor() as cursor:
#             cursor.execute(
#                 "CREATE DATABASE test_test_db WITH TEMPLATE test_db OWNER postgres;"
#             )
#
#         self.stdout.write(self.style.SUCCESS('Successfully created test database'))
