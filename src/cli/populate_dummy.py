"""Populate dummy data for OTT Platform using Django ORM.
Creates sample rows for core tables.
"""

import sys
import os
import random
from datetime import datetime, timedelta
from decimal import Decimal

# Ensure project root is on sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.core.settings')
import django

django.setup()

from myproject.ott.models import (
    User,
    Language,
    Genre,
    SubscriptionPlan,
    UserSubscription,
    Payment,
    WatchHistory,
    Watchlist,
    ContentRating,
    HeroSlider,
    HeroSliderItem,
    HomeSection,
    SupportTicket,
)

def random_timestamp():
    return datetime.utcnow() - timedelta(days=random.randint(0, 365))

def create_users():
    for i in range(10):
        User.objects.create(
            uuid=f"{i}-{random.randint(1000,9999)}",
            name=f"User {i}",
            email=f"user{i}@example.com",
            email_verified_at=random_timestamp(),
            password='hashed',
            phone='1234567890',
            avatar=None,
            status='active',
            role='user',
            remember_token=None,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

def create_languages():
    langs = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('hi', 'Hindi'),
    ]
    for code, name in langs:
        Language.objects.create(code=code, name=name, is_active=True)

def create_genres():
    for i in range(10):
        Genre.objects.create(
            name=f"Genre {i}",
            slug=f"genre-{i}",
            description=f"Description for genre {i}",
            is_active=True,
            display_order=i,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

def create_subscription_plans():
    for i in range(3):
        SubscriptionPlan.objects.create(
            name=f"Plan {i}",
            slug=f"plan-{i}",
            price=Decimal('9.99') * (i + 1),
            currency='USD',
            billing_cycle='monthly',
            trial_days=14,
            max_screens=2,
            max_quality='1080p',
            allow_download=True,
            is_popular=bool(i % 2),
            is_active=True,
            sort_order=i,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

def main():
    create_users()
    create_languages()
    create_genres()
    create_subscription_plans()
    print('Dummy data inserted via Django ORM.')

if __name__ == '__main__':
    main()
