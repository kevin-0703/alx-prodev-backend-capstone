from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model



User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with mock data"

    def handle(self, *args, **kwargs):
        # 1. Create Users
        if User.objects.count() < 5:
            for i in range(5):
                User.objects.create_user(
                    username=f"user{i}",
                    email=f"user{i}@example.com",
                    password="password123",
                    date_of_birth="1990-01-01"
                )
            self.stdout.write(self.style.SUCCESS("✔ Created test users"))
