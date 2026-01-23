from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Видаляє всі записи про app "auth" з таблиці django_migrations'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM django_migrations WHERE app = 'auth';")
        self.stdout.write(self.style.SUCCESS('Готово! Записи про auth видалено з django_migrations.'))