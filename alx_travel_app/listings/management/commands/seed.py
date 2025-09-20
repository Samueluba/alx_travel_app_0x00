from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_listings = [
            {
                "title": "Cozy Apartment in Lagos",
                "description": "A modern and cozy apartment in the heart of Lagos.",
                "price_per_night": 5000.00,
                "location": "Lagos, Nigeria"
            },
            {
                "title": "Beachfront Villa",
                "description": "Luxury villa with private beach access.",
                "price_per_night": 25000.00,
                "location": "Lekki, Nigeria"
            },
            {
                "title": "City Center Studio",
                "description": "Compact studio perfect for solo travelers.",
                "price_per_night": 3000.00,
                "location": "Abuja, Nigeria"
            }
        ]

        for listing_data in sample_listings:
            Listing.objects.create(**listing_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded listings!'))

