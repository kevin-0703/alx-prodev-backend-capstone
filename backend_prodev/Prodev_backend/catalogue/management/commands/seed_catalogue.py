from django.core.management.base import BaseCommand
from faker import Faker
import random
import uuid
from django.utils.text import slugify

from catalogue.models import Category, Product  


class Command(BaseCommand):
    help = "Seed the database with mock category and product data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write("➡ Creating categories...")

        category_names = [
            "Electronics", "Fashion", "Home Appliances", "Phones",
            "Laptops", "Furniture", "Sports", "Groceries",
            "Gaming", "Health & Beauty"
        ]

        categories = []
        for name in category_names:
            category, _ = Category.objects.get_or_create(
                name=name,
                defaults={"slug": slugify(name)}
            )
            categories.append(category)

        self.stdout.write(self.style.SUCCESS("✔ Categories ready"))

        self.stdout.write("➡ Creating products...")

        for i in range(150):
            title = fake.sentence(nb_words=3)
            category = random.choice(categories)

            Product.objects.create(
                sku=str(uuid.uuid4()).replace("-", "")[:12].upper(),
                title=title,
                slug=slugify(title) + "-" + str(uuid.uuid4())[:6],
                description=fake.text(max_nb_chars=300),
                price=round(random.uniform(5, 2500), 2),
                available=random.choice([True, True, True, False]),
                category=category,
                inventory=random.randint(0, 150)
            )

        self.stdout.write(self.style.SUCCESS("✔ Created 150 products"))
        self.stdout.write(self.style.SUCCESS("🎉 Seeding complete"))
